import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from rich.progress import track
from rich.console import Console

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mbe_eval import MBEEvaluator
from mbe_eval.utils import compute_fim_norm

console = Console()

# 1. Define a simple MLP
class SimpleMLP(nn.Module):
    def __init__(self, input_dim=20, hidden_dim=64, num_classes=2):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, num_classes)
        )
    def forward(self, x):
        return self.net(x)

def train_model(X_train, y_train, X_val, y_val, lr, weight_decay):
    """Trains a model and returns FIM_norm at epoch 20, val_loss at epoch 20, and final accuracy."""
    model = SimpleMLP()
    optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    criterion = nn.CrossEntropyLoss()
    
    X_tr = torch.FloatTensor(X_train)
    y_tr = torch.LongTensor(y_train)
    X_v  = torch.FloatTensor(X_val)
    y_v  = torch.LongTensor(y_val)
    
    fim_norm_epoch20 = None
    val_loss_epoch20 = None
    
    for epoch in range(1, 101):
        model.train()
        optimizer.zero_grad()
        loss = criterion(model(X_tr), y_tr)
        loss.backward()
        optimizer.step()
        
        # Checkpoint at Epoch 20
        if epoch == 20:
            model.eval()
            with torch.no_grad():
                val_loss_epoch20 = criterion(model(X_v), y_v).item()
            
            # Compute proposed representation metric
            # Use a subset of 100 validation samples to compute the dual gram matrix
            N = min(100, len(X_v))
            fim_norm_epoch20 = compute_fim_norm(model, criterion, X_v[:N], y_v[:N])
            
    # Final Evaluation
    model.eval()
    with torch.no_grad():
        preds = model(X_v).argmax(dim=1)
        final_acc = (preds == y_v).float().mean().item()
        
    return fim_norm_epoch20, val_loss_epoch20, final_acc

def main():
    console.print("\n[bold yellow]Generating Synthetic Dataset...[/bold yellow]")
    X, y = make_classification(n_samples=2000, n_features=20, n_informative=10, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    n_runs = 20
    metric_vals = []
    baseline_vals = []
    target_vals = []
    
    console.print(f"[bold yellow]Training Heterogeneous Grid ({n_runs} models)[/bold yellow]")
    
    for i in track(range(n_runs), description="Training models..."):
        # Randomize hyperparameters to break trivial collinearity
        lr = np.random.uniform(1e-4, 1e-2)
        wd = np.random.uniform(1e-5, 1e-3)
        
        fim, val_loss, final_acc = train_model(X_train, y_train, X_val, y_val, lr, wd)
        
        metric_vals.append(fim)
        baseline_vals.append(val_loss)
        target_vals.append(final_acc)
        
    metric_vals = np.array(metric_vals)
    baseline_vals = np.array(baseline_vals)
    target_vals = np.array(target_vals)
    
    # Run the MBE framework
    evaluator = MBEEvaluator(metric_name="Gradient Effective Rank (FIM_norm)", baseline_name="Epoch 20 Val Loss")
    report = evaluator.evaluate(metric_vals, baseline_vals, target_vals)
    
if __name__ == "__main__":
    main()
