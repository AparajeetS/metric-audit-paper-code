from __future__ import annotations

import argparse
import csv
import math
import pickle
import random
import time
import warnings
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CIFAR_DIR = REPO_ROOT / "experiments" / "05_kaggle" / "data" / "cifar-10-batches-py"
OUT_DIR = Path(__file__).resolve().parent


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, in_planes: int, planes: int, stride: int = 1) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(in_planes, planes, 3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(planes)
        self.conv2 = nn.Conv2d(planes, planes, 3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(planes)
        self.shortcut = nn.Identity()
        if stride != 1 or in_planes != planes:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_planes, planes, 1, stride=stride, bias=False),
                nn.BatchNorm2d(planes),
            )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out = out + self.shortcut(x)
        return F.relu(out)


class TinyCifarResNet(nn.Module):
    """Small CIFAR ResNet for CPU smoke tests."""

    def __init__(self, num_classes: int = 10) -> None:
        super().__init__()
        self.in_planes = 16
        self.conv1 = nn.Conv2d(3, 16, 3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(16)
        self.layer1 = self._make_layer(16, blocks=2, stride=1)
        self.layer2 = self._make_layer(32, blocks=2, stride=2)
        self.layer3 = self._make_layer(64, blocks=2, stride=2)
        self.fc = nn.Linear(64, num_classes)

    def _make_layer(self, planes: int, blocks: int, stride: int) -> nn.Sequential:
        strides = [stride] + [1] * (blocks - 1)
        layers = []
        for block_stride in strides:
            layers.append(BasicBlock(self.in_planes, planes, block_stride))
            self.in_planes = planes
        return nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = F.avg_pool2d(out, out.size(3))
        out = torch.flatten(out, 1)
        return self.fc(out)


def _load_pickle(path: Path) -> dict:
    with path.open("rb") as handle:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=Warning, message=".*dtype.*")
            return pickle.load(handle, encoding="latin1")


def load_cifar(cifar_dir: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    xs: list[np.ndarray] = []
    ys: list[int] = []
    for i in range(1, 6):
        batch = _load_pickle(cifar_dir / f"data_batch_{i}")
        xs.append(batch["data"])
        ys.extend(batch["labels"])
    train_x = np.concatenate(xs, axis=0).reshape(-1, 3, 32, 32).astype("float32") / 255.0
    train_y = np.asarray(ys, dtype="int64")

    test = _load_pickle(cifar_dir / "test_batch")
    test_x = test["data"].reshape(-1, 3, 32, 32).astype("float32") / 255.0
    test_y = np.asarray(test["labels"], dtype="int64")

    mean = np.asarray([0.4914, 0.4822, 0.4465], dtype="float32").reshape(1, 3, 1, 1)
    std = np.asarray([0.2023, 0.1994, 0.2010], dtype="float32").reshape(1, 3, 1, 1)
    return (train_x - mean) / std, train_y, (test_x - mean) / std, test_y


def subset_tensors(
    train_x: np.ndarray,
    train_y: np.ndarray,
    test_x: np.ndarray,
    test_y: np.ndarray,
    n_train: int,
    n_test: int,
    seed: int,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    rng = np.random.default_rng(seed)
    tr_idx = rng.choice(len(train_x), size=n_train, replace=False)
    te_idx = np.arange(min(n_test, len(test_x)))
    return (
        torch.from_numpy(train_x[tr_idx]),
        torch.from_numpy(train_y[tr_idx]),
        torch.from_numpy(test_x[te_idx]),
        torch.from_numpy(test_y[te_idx]),
    )


def evaluate(model: nn.Module, x: torch.Tensor, y: torch.Tensor, batch_size: int) -> tuple[float, float]:
    model.eval()
    total_loss = 0.0
    total_correct = 0
    crit = nn.CrossEntropyLoss(reduction="sum")
    with torch.no_grad():
        for start in range(0, len(x), batch_size):
            xb = x[start : start + batch_size]
            yb = y[start : start + batch_size]
            logits = model(xb)
            total_loss += float(crit(logits, yb))
            total_correct += int((logits.argmax(1) == yb).sum())
    return total_loss / len(x), total_correct / len(x)


def effective_rank(values: np.ndarray) -> float:
    vals = np.maximum(np.asarray(values, dtype=float), 0.0)
    total = vals.sum()
    if total <= 0:
        return 0.0
    probs = vals / total
    probs = probs[probs > 0]
    return float(np.exp(-(probs * np.log(probs)).sum()))


def fim_norm(model: nn.Module, x: torch.Tensor, y: torch.Tensor, metric_n: int, seed: int) -> float:
    model.eval()
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(x), size=min(metric_n, len(x)), replace=False)
    grads = []
    crit = nn.CrossEntropyLoss()
    for i in idx:
        model.zero_grad(set_to_none=True)
        loss = crit(model(x[i : i + 1]), y[i : i + 1])
        loss.backward()
        vec = torch.cat([p.grad.detach().flatten().cpu() for p in model.parameters() if p.grad is not None])
        grads.append(vec.numpy())
    grad_matrix = np.stack(grads, axis=0)
    dual_fim = (grad_matrix @ grad_matrix.T) / len(idx)
    eigvals = np.linalg.eigvalsh(dual_fim)
    return effective_rank(eigvals) / len(idx)


@dataclass(frozen=True)
class Config:
    lr: float
    wd: float
    seed: int


def train_one(
    cfg: Config,
    train_x: np.ndarray,
    train_y: np.ndarray,
    test_x: np.ndarray,
    test_y: np.ndarray,
    n_train: int,
    n_test: int,
    epochs: int,
    batch_size: int,
    metric_n: int,
) -> dict[str, float | int]:
    set_seed(cfg.seed)
    xtr, ytr, xte, yte = subset_tensors(train_x, train_y, test_x, test_y, n_train, n_test, cfg.seed)
    model = TinyCifarResNet()
    opt = torch.optim.SGD(model.parameters(), lr=cfg.lr, momentum=0.9, weight_decay=cfg.wd, nesterov=True)
    crit = nn.CrossEntropyLoss()
    start = time.time()

    for _ in range(epochs):
        model.train()
        perm = torch.randperm(len(xtr))
        for batch_start in range(0, len(xtr), batch_size):
            batch_idx = perm[batch_start : batch_start + batch_size]
            opt.zero_grad(set_to_none=True)
            loss = crit(model(xtr[batch_idx]), ytr[batch_idx])
            loss.backward()
            opt.step()

    train_loss, train_acc = evaluate(model, xtr, ytr, batch_size)
    val_loss, final_acc = evaluate(model, xte, yte, batch_size)
    fim = fim_norm(model, xtr, ytr, metric_n=metric_n, seed=cfg.seed + 1000)
    elapsed = time.time() - start
    print(
        f"seed={cfg.seed:3d} lr={cfg.lr:.4g} wd={cfg.wd:.1e} "
        f"acc={final_acc:.3f} loss={val_loss:.3f} fim={fim:.4f} ({elapsed:.1f}s)",
        flush=True,
    )
    return {
        "seed": cfg.seed,
        "lr": cfg.lr,
        "wd": cfg.wd,
        "epochs": epochs,
        "n_train": n_train,
        "n_test": n_test,
        "metric_n": metric_n,
        "train_loss": train_loss,
        "train_acc": train_acc,
        "val_loss": val_loss,
        "final_acc": final_acc,
        "fim_norm": fim,
        "elapsed_s": elapsed,
    }


def rank_values(values: np.ndarray) -> np.ndarray:
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=float)
    sorted_values = values[order]
    start = 0
    while start < len(values):
        end = start + 1
        while end < len(values) and sorted_values[end] == sorted_values[start]:
            end += 1
        avg_rank = 0.5 * (start + end - 1) + 1.0
        ranks[order[start:end]] = avg_rank
        start = end
    return ranks


def pearson(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) < 2:
        return math.nan
    if np.std(a) == 0 or np.std(b) == 0:
        return math.nan
    return float(np.corrcoef(a, b)[0, 1])


def spearman(rows: list[dict[str, float | int]], x: str, y: str) -> float:
    xv = np.asarray([float(row[x]) for row in rows], dtype=float)
    yv = np.asarray([float(row[y]) for row in rows], dtype=float)
    return pearson(rank_values(xv), rank_values(yv))


def partial_rank_corr(rows: list[dict[str, float | int]], x: str, y: str, covars: list[str]) -> float:
    xr = rank_values(np.asarray([float(row[x]) for row in rows], dtype=float))
    yr = rank_values(np.asarray([float(row[y]) for row in rows], dtype=float))
    design = [np.ones(len(rows))]
    for covar in covars:
        design.append(rank_values(np.asarray([float(row[covar]) for row in rows], dtype=float)))
    mat = np.column_stack(design)
    x_res = xr - mat @ np.linalg.lstsq(mat, xr, rcond=None)[0]
    y_res = yr - mat @ np.linalg.lstsq(mat, yr, rcond=None)[0]
    return pearson(x_res, y_res)


def render_report(rows: list[dict[str, float | int]], out_csv: Path) -> str:
    metrics = ["fim_norm", "val_loss", "train_acc", "train_loss"]
    lines = [
        "# ResNet FIM_norm MBE Smoke Test",
        "",
        f"- csv: `{out_csv}`",
        f"- rows: `{len(rows)}`",
        "- model: compact CIFAR ResNet with BatchNorm, trained on CPU",
        "- MBE control covariates: rank(`lr`), rank(`wd`)",
        "",
        "| metric | raw Spearman vs final_acc | partial rank, lr+wd | partial rank, lr+wd+seed |",
        "|---|---:|---:|---:|",
    ]
    for metric in metrics:
        raw = spearman(rows, metric, "final_acc")
        part = partial_rank_corr(rows, metric, "final_acc", ["lr", "wd"])
        part_seed = partial_rank_corr(rows, metric, "final_acc", ["lr", "wd", "seed"])
        lines.append(f"| {metric} | {raw:+.3f} | {part:+.3f} | {part_seed:+.3f} |")
    lines.extend(
        [
            "",
            "Interpretation guardrail: this is a CPU smoke test for direction and plumbing, not a publishable-scale ResNet result.",
            "",
        ]
    )
    return "\n".join(lines)


def build_configs(quick: bool) -> list[Config]:
    seeds = [11, 22] if quick else [11, 22, 33]
    lrs = [0.003, 0.01] if quick else [0.001, 0.003, 0.01]
    wds = [0.0, 1e-4]
    return [Config(lr=lr, wd=wd, seed=seed) for seed in seeds for lr in lrs for wd in wds]


def main() -> None:
    parser = argparse.ArgumentParser(description="CPU ResNet smoke test for FIM_norm under MBE.")
    parser.add_argument("--cifar-dir", type=Path, default=DEFAULT_CIFAR_DIR)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--n-train", type=int, default=None)
    parser.add_argument("--n-test", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--metric-n", type=int, default=None)
    args = parser.parse_args()

    quick = bool(args.quick)
    epochs = args.epochs if args.epochs is not None else (1 if quick else 3)
    n_train = args.n_train if args.n_train is not None else (384 if quick else 1200)
    n_test = args.n_test if args.n_test is not None else (256 if quick else 500)
    metric_n = args.metric_n if args.metric_n is not None else (8 if quick else 24)

    print(f"Loading CIFAR from {args.cifar_dir}", flush=True)
    train_x, train_y, test_x, test_y = load_cifar(args.cifar_dir)
    rows = []
    for cfg in build_configs(quick):
        rows.append(
            train_one(
                cfg,
                train_x,
                train_y,
                test_x,
                test_y,
                n_train=n_train,
                n_test=n_test,
                epochs=epochs,
                batch_size=args.batch_size,
                metric_n=metric_n,
            )
        )

    suffix = "quick" if quick else "standard"
    out_csv = OUT_DIR / f"resnet_fim_mbe_{suffix}.csv"
    out_report = OUT_DIR / f"resnet_fim_mbe_{suffix}_report.md"
    with out_csv.open("w", newline="", encoding="ascii") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    out_report.write_text(render_report(rows, out_csv), encoding="ascii")
    print()
    print(out_report.read_text(encoding="ascii"), flush=True)
    print(f"Saved CSV to {out_csv}", flush=True)
    print(f"Saved report to {out_report}", flush=True)


if __name__ == "__main__":
    main()
