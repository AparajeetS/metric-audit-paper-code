import os

import sys
import math
import copy
import numpy as np
import pingouin as pg
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as T
from torch.utils.data import DataLoader, Subset
from rich.progress import track
from rich.console import Console

console = Console()

# --- CIFAR10 Model (CNN with Batch Normalization) ---
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),

            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(128, 10)
        )
    def forward(self, x):
        return self.net(x)

# --- Metrics ---
def compute_fim_norm(model, loss_fn, inputs, targets):
    N = inputs.shape[0]
    grads = []
    model.eval()
    for i in range(N):
        x = inputs[i:i+1]
        y = targets[i:i+1]
        loss = loss_fn(model(x), y)
        model.zero_grad()
        loss.backward()
        g_vec = torch.cat([p.grad.flatten() for p in model.parameters() if p.grad is not None])
        grads.append(g_vec.detach())
    G = torch.stack(grads)
    S_dual = (1.0 / N) * torch.matmul(G, G.T)
    eigenvalues = torch.linalg.eigvalsh(S_dual)
    eigenvalues = torch.clamp(eigenvalues, min=1e-12)
    p = eigenvalues / eigenvalues.sum()
    H = -(p * torch.log(p)).sum().item()
    erank = math.exp(H)
    return erank / N

def compute_sam_sharpness(model, criterion, X, y, rho=0.05):
    """Computes SAM sharpness without floating point drift by restoring state_dict."""
    backup = copy.deepcopy(model.state_dict())
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
    model.load_state_dict(backup) # Perfect restoration
    return perturbed_loss - loss.item()

def compute_asam_sharpness(model, criterion, X, y, rho=0.5):
    """Computes Adaptive SAM (ASAM) sharpness without drift."""
    backup = copy.deepcopy(model.state_dict())
    model.eval()
    loss = criterion(model(X), y)
    model.zero_grad()
    loss.backward()
    grad_norm = torch.norm(torch.stack([torch.norm(p.grad * torch.abs(p), p=2) for p in model.parameters() if p.grad is not None]), p=2)
    if grad_norm < 1e-12:
        return 0.0
    scale = rho / grad_norm
    with torch.no_grad():
        for p in model.parameters():
            if p.grad is not None:
                p.add_(p.grad * (torch.abs(p) ** 2) * scale)
    perturbed_loss = criterion(model(X), y).item()
    model.load_state_dict(backup) # Perfect restoration
    return perturbed_loss - loss.item()

def compute_fisher_trace(model, criterion, X, y):
    model.eval()
    trace = 0.0
    for i in range(len(X)):
        loss = criterion(model(X[i:i+1]), y[i:i+1])
        model.zero_grad()
        loss.backward()
        g_norm_sq = sum(param.grad.norm(p=2)**2 for param in model.parameters() if param.grad is not None)
        trace += g_norm_sq.item()
    return trace / len(X)

def compute_gradient_norm(model, criterion, X, y):
    model.eval()
    loss = criterion(model(X), y)
    model.zero_grad()
    loss.backward()
    return torch.norm(torch.stack([param.grad.norm(p=2) for param in model.parameters() if param.grad is not None]), p=2).item()

def compute_weight_norm(model):
    return torch.norm(torch.stack([param.norm(p=2) for param in model.parameters()]), p=2).item()

def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    console.print(f"[bold yellow]Running on device: {device}[/bold yellow]")

    transform = T.Compose([
        T.ToTensor(),
        T.Normalize((0.4914,0.4822,0.4465), (0.2023,0.1994,0.2010))
    ])

    # We use a 10,000 train / 2,000 test subset of CIFAR10.
    # This design choice allows us to scale the hyperparameter grid search
    # to 250 models x 50 epochs while completing within reasonable GPU limits.
    ds_tr = torchvision.datasets.CIFAR10('/kaggle/working/data', train=True, download=True, transform=transform)
    ds_te = torchvision.datasets.CIFAR10('/kaggle/working/data', train=False, download=True, transform=transform)

    rng = np.random.RandomState(42)
    train_idx = rng.choice(len(ds_tr), 10000, replace=False)
    test_idx = rng.choice(len(ds_te), 2000, replace=False)

    train_subset = Subset(ds_tr, train_idx)
    test_subset = Subset(ds_te, test_idx)

    train_loader = DataLoader(train_subset, batch_size=256, shuffle=True, pin_memory=True)
    test_loader = DataLoader(test_subset, batch_size=256, shuffle=False, pin_memory=True)

    # Pre-extract training batch for metric calculation (N=100)
    X_train_batch = []
    y_train_batch = []
    for x, y in train_loader:
        X_train_batch.append(x)
        y_train_batch.append(y)
        if sum(len(b) for b in X_train_batch) >= 100:
            break
    X_train_batch = torch.cat(X_train_batch)[:100].to(device)
    y_train_batch = torch.cat(y_train_batch)[:100].to(device)

    n_runs = 2
    results = []

    console.print(f"[bold yellow]Training Large Heterogeneous Grid ({n_runs} models)[/bold yellow]")

    snapshots = [1]

    for i in range(n_runs):
        np.random.seed(42 + i)
        torch.manual_seed(42 + i)

        lr = np.exp(np.random.uniform(np.log(1e-4), np.log(1e-2)))
        wd = np.exp(np.random.uniform(np.log(1e-5), np.log(1e-3)))

        model = SimpleCNN().to(device)
        optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=wd)
        criterion = nn.CrossEntropyLoss()

        metrics = {'lr': lr, 'wd': wd}

        for epoch in range(1, 2): # 1 epochs per model
            model.train()
            for x, y in train_loader:
                x, y = x.to(device), y.to(device)
                optimizer.zero_grad()
                loss = criterion(model(x), y)
                loss.backward()
                optimizer.step()

            if epoch in snapshots:
                model.eval()
                with torch.no_grad():
                    val_loss = sum(criterion(model(x.to(device)), y.to(device)).item() for x, y in test_loader) / len(test_loader)
                    metrics[f'val_loss_ep{epoch}'] = val_loss

                # We always compute SAM and ASAM at all snapshots
                metrics[f'sam_sharpness_ep{epoch}'] = compute_sam_sharpness(model, criterion, X_train_batch, y_train_batch)
                metrics[f'asam_sharpness_ep{epoch}'] = compute_asam_sharpness(model, criterion, X_train_batch, y_train_batch)

                # For computationally heavy metrics, we only do them at epoch 20 to match the main text
                if epoch == 1:
                    metrics['fim_norm'] = compute_fim_norm(model, criterion, X_train_batch, y_train_batch)
                    metrics['fisher_trace'] = compute_fisher_trace(model, criterion, X_train_batch, y_train_batch)
                    metrics['grad_norm'] = compute_gradient_norm(model, criterion, X_train_batch, y_train_batch)
                    metrics['weight_norm'] = compute_weight_norm(model)

                    # For Table 3 absolute correlations
                    metrics['sam_sharpness'] = metrics[f'sam_sharpness_ep{epoch}']
                    metrics['asam_sharpness'] = metrics[f'asam_sharpness_ep{epoch}']
                    metrics['val_loss'] = metrics[f'val_loss_ep{epoch}']

        # Final eval at epoch 50
        model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for x, y in test_loader:
                x, y = x.to(device), y.to(device)
                preds = model(x).argmax(dim=1)
                correct += (preds == y).sum().item()
                total += len(y)
        metrics['final_acc'] = correct / total
        results.append(metrics)
        console.print(f"Model {i+1}/{n_runs} | Val Loss E50: {metrics['val_loss_ep50']:.3f} | Final Acc: {metrics['final_acc']:.3f}")

    df = pd.DataFrame(results)
    df.to_csv('kaggle_cifar10_results.csv', index=False)

    metrics_to_test = ['fim_norm', 'sam_sharpness', 'asam_sharpness', 'fisher_trace', 'grad_norm', 'weight_norm']

    console.print("\n[bold green]Absolute Correlations with Final Accuracy (Evaluated at Epoch 20)[/bold green]")
    for m in metrics_to_test:
        rho = pg.corr(df[m], df['final_acc'], method='spearman')
        console.print(f"{m} Absolute rho: {rho['r'].values[0]:.3f} (p={rho['p_val'].values[0]:.2e})")

    console.print("\n[bold cyan]MBE Partial Correlation Control (Controlling for LR, WD)[/bold cyan]")
    for m in metrics_to_test:
        mbe = pg.partial_corr(data=df, x=m, y='final_acc', covar=['lr', 'wd'], method='spearman')
        console.print(f"{m} Partial rho: {mbe['r'].values[0]:.3f} (p={mbe['p_val'].values[0]:.2e})")

    console.print("\n[bold cyan]=== CIFAR-10 Temporal Ablation: SAM & ASAM ===[/bold cyan]")
    for ep in snapshots:
        mbe_sam = pg.partial_corr(data=df, x=f'sam_sharpness_ep{ep}', y='final_acc', covar=['lr', 'wd'], method='spearman')
        mbe_asam = pg.partial_corr(data=df, x=f'asam_sharpness_ep{ep}', y='final_acc', covar=['lr', 'wd'], method='spearman')
        console.print(f"Epoch {ep:>2} SAM : partial rho = {mbe_sam['r'].values[0]:+.3f} (p = {mbe_sam['p_val'].values[0]:.2e})")
        console.print(f"Epoch {ep:>2} ASAM: partial rho = {mbe_asam['r'].values[0]:+.3f} (p = {mbe_asam['p_val'].values[0]:.2e})")

if __name__ == "__main__":
    main()
