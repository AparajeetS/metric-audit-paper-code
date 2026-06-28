import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mbe_eval.utils import compute_fim_norm

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

def train_and_get_fim(X_train, y_train, X_val, y_val):
    model = SimpleMLP()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    X_tr = torch.FloatTensor(X_train)
    y_tr = torch.LongTensor(y_train)
    X_v  = torch.FloatTensor(X_val)
    y_v  = torch.LongTensor(y_val)

    for epoch in range(1, 41):
        model.train()
        optimizer.zero_grad()
        loss = criterion(model(X_tr), y_tr)
        loss.backward()
        optimizer.step()

    model.eval()
    N = min(100, len(X_v))
    fim_norm = compute_fim_norm(model, criterion, X_v[:N], y_v[:N])

    with torch.no_grad():
        preds = model(X_v).argmax(dim=1)
        acc = (preds == y_v).float().mean().item()

    return fim_norm, acc

def main():
    print("\nStage 1: Metric sanity probes")

    X, y = make_classification(n_samples=2000, n_features=20, n_informative=10, random_state=42)
    X_train_full, X_val, y_train_full, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # 1. Capacity Probe (Varying Data Size)
    print("\nRunning capacity probe (varying training size)...")
    sizes = [100, 300, 600, 1000]
    for size in sizes:
        idx = np.random.choice(len(X_train_full), size, replace=False)
        X_tr = X_train_full[idx]
        y_tr = y_train_full[idx]

        fim, acc = train_and_get_fim(X_tr, y_tr, X_val, y_val)
        print(f"Data Size: {size:4d} | FIM_norm: {fim:.4f} | Final Acc: {acc:.3f}")

    # 2. Noise Probe (Varying Label Corruption)
    print("\nRunning noise probe (varying label corruption)...")
    noise_levels = [0.0, 0.15, 0.30, 0.50]
    X_tr = X_train_full[:800]
    y_tr_clean = y_train_full[:800]

    for noise in noise_levels:
        y_tr = y_tr_clean.copy()
        n_corrupt = int(noise * len(y_tr))
        corrupt_idx = np.random.choice(len(y_tr), n_corrupt, replace=False)
        y_tr[corrupt_idx] = np.random.randint(0, 2, n_corrupt)

        fim, acc = train_and_get_fim(X_tr, y_tr, X_val, y_val)
        print(f"Noise: {noise*100:3.0f}% | FIM_norm: {fim:.4f} | Final Acc: {acc:.3f}")

    print("\nMetric probes complete.")
    print("If a metric tracks both data size and label noise, the next step is an MBE audit.")
    print("Run 02_run_heterogeneous_grid.py to control for ordinary training baselines.")

if __name__ == "__main__":
    main()
