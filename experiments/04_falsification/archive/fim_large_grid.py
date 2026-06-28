import os
import sys
import numpy as np
import pingouin as pg
import pandas as pd
from rich.progress import track
from rich.console import Console
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from mbe_eval.core import MBEEvaluator
from mbe_eval.utils import compute_fim_norm
import torch
import torch.nn as nn
import torch.optim as optim

console = Console()

class SimpleMLP(nn.Module):
    def __init__(self, input_dim=64, hidden_dim=64, num_classes=10):
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

def compute_sam_sharpness(model, criterion, X, y, rho=0.05):
    """Computes SAM sharpness (loss diff after ascending gradient step) for PyTorch models."""
    model.eval()
    loss = criterion(model(X), y)
    model.zero_grad()
    loss.backward()
    grad_norm = torch.norm(torch.stack([p.grad.norm(p=2) for p in model.parameters() if p.grad is not None]), p=2)
    if grad_norm < 1e-12:
        return 0.0
    scale = rho / grad_norm
    with torch.no_grad():
        for p in model.parameters():
            if p.grad is not None:
                p.add_(p.grad * scale)
    perturbed_loss = criterion(model(X), y).item()
    with torch.no_grad():
        for p in model.parameters():
            if p.grad is not None:
                p.sub_(p.grad * scale)
    return perturbed_loss - loss.item()

def compute_fisher_trace(model, criterion, X, y):
    """Computes the trace of the uncentered Empirical Fisher (sum of squared gradient norms)."""
    model.eval()
    trace = 0.0
    for i in range(len(X)):
        loss = criterion(model(X[i:i+1]), y[i:i+1])
        model.zero_grad()
        loss.backward()
        g_norm_sq = sum(p.grad.norm(p=2)**2 for p in model.parameters() if p.grad is not None)
        trace += g_norm_sq.item()
    return trace / len(X)

def compute_gradient_norm(model, criterion, X, y):
    """Computes the gradient norm over the batch."""
    model.eval()
    loss = criterion(model(X), y)
    model.zero_grad()
    loss.backward()
    return torch.norm(torch.stack([p.grad.norm(p=2) for p in model.parameters() if p.grad is not None]), p=2).item()

def compute_weight_norm(model):
    """Computes the L2 norm of the model weights."""
    return torch.norm(torch.stack([p.norm(p=2) for p in model.parameters()]), p=2).item()

def train_model(X_train, y_train, X_val, y_val, lr, weight_decay):
    model = SimpleMLP()
    optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    criterion = nn.CrossEntropyLoss()

    X_tr = torch.FloatTensor(X_train)
    y_tr = torch.LongTensor(y_train)
    X_v  = torch.FloatTensor(X_val)
    y_v  = torch.LongTensor(y_val)

    metrics = {}

    for epoch in range(1, 201):
        model.train()
        optimizer.zero_grad()
        loss = criterion(model(X_tr), y_tr)
        loss.backward()
        optimizer.step()

        if epoch == 20:
            model.eval()
            with torch.no_grad():
                metrics['val_loss'] = criterion(model(X_v), y_v).item()

            N = min(100, len(X_v))
            X_batch, y_batch = X_v[:N], y_v[:N]
            metrics['fim_norm'] = compute_fim_norm(model, criterion, X_batch, y_batch)
            metrics['sam_sharpness'] = compute_sam_sharpness(model, criterion, X_batch, y_batch)
            metrics['fisher_trace'] = compute_fisher_trace(model, criterion, X_batch, y_batch)
            metrics['grad_norm'] = compute_gradient_norm(model, criterion, X_batch, y_batch)
            metrics['weight_norm'] = compute_weight_norm(model)

    model.eval()
    with torch.no_grad():
        preds = model(X_v).argmax(dim=1)
        metrics['final_acc'] = (preds == y_v).float().mean().item()

    return metrics

def main():
    console.print("\n[bold yellow]Loading UCI Digits Dataset...[/bold yellow]")
    digits = load_digits()
    X, y = digits.data, digits.target
    X = (X - X.mean(axis=0)) / (X.std(axis=0) + 1e-8)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    n_runs = 1000
    results = []

    console.print(f"[bold yellow]Training Large Heterogeneous Grid ({n_runs} models)[/bold yellow]")
    console.print("Running completely on CPU... Expected time: ~10-20 minutes")

    np.random.seed(42)
    torch.manual_seed(42)

    for i in track(range(n_runs), description="Training models..."):
        lr = np.exp(np.random.uniform(np.log(1e-4), np.log(1e-2)))
        wd = np.exp(np.random.uniform(np.log(1e-5), np.log(1e-3)))

        m = train_model(X_train, y_train, X_val, y_val, lr, wd)
        results.append(m)

    df = pd.DataFrame(results)

    os.makedirs(os.path.join(os.path.dirname(__file__), "out"), exist_ok=True)
    out_path = os.path.join(os.path.dirname(__file__), "out", "large_grid_results_multimetric.csv")
    df.to_csv(out_path, index=False)
    console.print(f"Results saved to {out_path}")

    metrics_to_test = ['fim_norm', 'sam_sharpness', 'fisher_trace', 'grad_norm', 'weight_norm']

    console.print("\n[bold green]Absolute Correlations with Epoch 200 Accuracy[/bold green]")
    rho_val = pg.corr(df['val_loss'], df['final_acc'], method='spearman')
    console.print(f"Validation Loss Absolute rho: {rho_val['r'].values[0]:.3f} (p={rho_val['p_val'].values[0]:.2e})")

    for m in metrics_to_test:
        rho = pg.corr(df[m], df['final_acc'], method='spearman')
        console.print(f"{m} Absolute rho: {rho['r'].values[0]:.3f} (p={rho['p_val'].values[0]:.2e})")

    console.print("\n[bold cyan]MBE Partial Correlation Control (Controlling for Val Loss)[/bold cyan]")
    for m in metrics_to_test:
        mbe = pg.partial_corr(data=df, x=m, y='final_acc', covar='val_loss', method='spearman')
        console.print(f"{m} Partial rho: {mbe['r'].values[0]:.3f} (p={mbe['p_val'].values[0]:.2e})")

if __name__ == "__main__":
    main()
