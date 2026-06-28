import os
import sys
import numpy as np
import pingouin as pg
import pandas as pd
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
    model.eval()
    loss = criterion(model(X), y)
    model.zero_grad()
    loss.backward()
    grad_norm = torch.norm(torch.stack([p.grad.norm(p=2) for p in model.parameters() if p.grad is not None]), p=2)
    if grad_norm < 1e-12: return 0.0
    scale = rho / grad_norm
    with torch.no_grad():
        for p in model.parameters():
            if p.grad is not None: p.add_(p.grad * scale)
    perturbed_loss = criterion(model(X), y).item()
    with torch.no_grad():
        for p in model.parameters():
            if p.grad is not None: p.sub_(p.grad * scale)
    return perturbed_loss - loss.item()

def train_model(X_train, y_train, X_val, y_val, lr, weight_decay):
    model = SimpleMLP()
    optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    criterion = nn.CrossEntropyLoss()

    X_tr = torch.FloatTensor(X_train)
    y_tr = torch.LongTensor(y_train)
    X_v  = torch.FloatTensor(X_val)
    y_v  = torch.LongTensor(y_val)

    metrics = {'lr': lr, 'wd': weight_decay}

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
                metrics['train_loss'] = criterion(model(X_tr), y_tr).item()

            N = min(100, len(X_v))
            X_batch, y_batch = X_v[:N], y_v[:N]
            metrics['sam_sharpness'] = compute_sam_sharpness(model, criterion, X_batch, y_batch)

    model.eval()
    with torch.no_grad():
        preds = model(X_v).argmax(dim=1)
        metrics['final_acc'] = (preds == y_v).float().mean().item()

    return metrics

def main():
    console.print("\n[bold yellow]Loading Dataset...[/bold yellow]")
    digits = load_digits()
    X, y = digits.data, digits.target
    X = (X - X.mean(axis=0)) / (X.std(axis=0) + 1e-8)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    n_runs = 100
    results = []

    console.print(f"[bold yellow]Training Grid ({n_runs} models)[/bold yellow]")

    np.random.seed(42)
    torch.manual_seed(42)

    for i in range(n_runs):
        lr = np.exp(np.random.uniform(np.log(1e-4), np.log(1e-2)))
        wd = np.exp(np.random.uniform(np.log(1e-5), np.log(1e-3)))

        m = train_model(X_train, y_train, X_val, y_val, lr, wd)
        results.append(m)

    df = pd.DataFrame(results)

    console.print("\n=== Correlations ===")
    abs_rho = pg.corr(df['sam_sharpness'], df['final_acc'], method='spearman')
    console.print(f"Absolute: rho = {abs_rho['r'].values[0]:+.3f} (p = {abs_rho['p_val'].values[0]:.2e})")

    mbe_loss = pg.partial_corr(data=df, x='sam_sharpness', y='final_acc', covar='train_loss', method='spearman')
    console.print(f"Partial (controlling Train Loss): rho = {mbe_loss['r'].values[0]:+.3f} (p = {mbe_loss['p_val'].values[0]:.2e})")

    mbe_hyp = pg.partial_corr(data=df, x='sam_sharpness', y='final_acc', covar=['lr', 'wd'], method='spearman')
    console.print(f"Partial (controlling LR, WD): rho = {mbe_hyp['r'].values[0]:+.3f} (p = {mbe_hyp['p_val'].values[0]:.2e})")

if __name__ == "__main__":
    main()
