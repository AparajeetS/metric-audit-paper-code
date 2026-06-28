from __future__ import annotations

import argparse
import copy
import csv
import json
import math
import os
import random
import subprocess
import sys
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path


if Path("/kaggle/working").exists() and os.environ.get("CEI_SKIP_TORCH_INSTALL") != "1":
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--quiet",
            "--force-reinstall",
            "--no-cache-dir",
            "torch==2.4.1",
            "torchvision==0.19.1",
            "--index-url",
            "https://download.pytorch.org/whl/cu118",
        ]
    )

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset, Subset, TensorDataset


OUT_DIR = Path.cwd()
CIFAR_MEAN = (0.4914, 0.4822, 0.4465)
CIFAR_STD = (0.2023, 0.1994, 0.2010)


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def device_name() -> str:
    return "cuda" if torch.cuda.is_available() else "cpu"


class SimpleCNN(nn.Module):
    def __init__(self, dropout: float = 0.0) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Dropout(dropout),
            nn.Conv2d(64, 128, 3, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Dropout(dropout),
            nn.Conv2d(128, 256, 3, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
        )
        self.fc = nn.Linear(256, 10)

    def forward(self, x: torch.Tensor, return_features: bool = False):
        z = self.features(x)
        logits = self.fc(z)
        return (logits, z) if return_features else logits


class BasicBlock(nn.Module):
    def __init__(self, in_planes: int, planes: int, stride: int = 1, dropout: float = 0.0) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(in_planes, planes, 3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(planes)
        self.conv2 = nn.Conv2d(planes, planes, 3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(planes)
        self.drop = nn.Dropout2d(dropout)
        self.shortcut = nn.Identity()
        if stride != 1 or in_planes != planes:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_planes, planes, 1, stride=stride, bias=False),
                nn.BatchNorm2d(planes),
            )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.drop(out)
        out = self.bn2(self.conv2(out))
        return F.relu(out + self.shortcut(x))


class CifarResNet(nn.Module):
    def __init__(self, width: int = 32, dropout: float = 0.0) -> None:
        super().__init__()
        self.in_planes = width
        self.conv1 = nn.Conv2d(3, width, 3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(width)
        self.layer1 = self._make_layer(width, 2, stride=1, dropout=dropout)
        self.layer2 = self._make_layer(width * 2, 2, stride=2, dropout=dropout)
        self.layer3 = self._make_layer(width * 4, 2, stride=2, dropout=dropout)
        self.fc = nn.Linear(width * 4, 10)

    def _make_layer(self, planes: int, blocks: int, stride: int, dropout: float) -> nn.Sequential:
        strides = [stride] + [1] * (blocks - 1)
        layers = []
        for s in strides:
            layers.append(BasicBlock(self.in_planes, planes, s, dropout))
            self.in_planes = planes
        return nn.Sequential(*layers)

    def forward(self, x: torch.Tensor, return_features: bool = False):
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = F.avg_pool2d(out, out.size(3))
        z = torch.flatten(out, 1)
        logits = self.fc(z)
        return (logits, z) if return_features else logits


class TinyViT(nn.Module):
    def __init__(self, dropout: float = 0.0, dim: int = 128, depth: int = 4, heads: int = 4) -> None:
        super().__init__()
        self.patch = nn.Conv2d(3, dim, kernel_size=4, stride=4)
        self.cls = nn.Parameter(torch.zeros(1, 1, dim))
        self.pos = nn.Parameter(torch.randn(1, 65, dim) * 0.02)
        enc_layer = nn.TransformerEncoderLayer(
            d_model=dim,
            nhead=heads,
            dim_feedforward=dim * 4,
            dropout=dropout,
            batch_first=True,
            activation="gelu",
            norm_first=True,
        )
        self.encoder = nn.TransformerEncoder(enc_layer, num_layers=depth)
        self.norm = nn.LayerNorm(dim)
        self.fc = nn.Linear(dim, 10)

    def forward(self, x: torch.Tensor, return_features: bool = False):
        z = self.patch(x).flatten(2).transpose(1, 2)
        cls = self.cls.expand(z.size(0), -1, -1)
        z = torch.cat([cls, z], dim=1) + self.pos[:, : z.size(1) + 1]
        z = self.encoder(z)
        feat = self.norm(z[:, 0])
        logits = self.fc(feat)
        return (logits, feat) if return_features else logits


class CharDataset(Dataset):
    def __init__(self, ids: torch.Tensor, block_size: int) -> None:
        self.ids = ids.long()
        self.block_size = block_size

    def __len__(self) -> int:
        return max(0, len(self.ids) - self.block_size - 1)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        x = self.ids[idx : idx + self.block_size]
        y = self.ids[idx + 1 : idx + self.block_size + 1]
        return x, y


class TinyCharTransformer(nn.Module):
    def __init__(self, vocab_size: int, block_size: int, dropout: float = 0.0, dim: int = 128) -> None:
        super().__init__()
        self.block_size = block_size
        self.token_emb = nn.Embedding(vocab_size, dim)
        self.pos_emb = nn.Embedding(block_size, dim)
        enc_layer = nn.TransformerEncoderLayer(
            d_model=dim,
            nhead=4,
            dim_feedforward=dim * 4,
            dropout=dropout,
            batch_first=True,
            activation="gelu",
            norm_first=True,
        )
        self.encoder = nn.TransformerEncoder(enc_layer, num_layers=3)
        self.norm = nn.LayerNorm(dim)
        self.head = nn.Linear(dim, vocab_size)

    def forward(self, x: torch.Tensor, return_features: bool = False):
        positions = torch.arange(x.size(1), device=x.device)
        z = self.token_emb(x) + self.pos_emb(positions)[None, :, :]
        z = self.encoder(z)
        feat = self.norm(z)
        logits = self.head(feat)
        pooled = feat.mean(dim=1)
        return (logits, pooled) if return_features else logits


def make_model(arch: str, dropout: float, vocab_size: int | None = None, block_size: int = 96) -> nn.Module:
    if arch == "cnn":
        return SimpleCNN(dropout=dropout)
    if arch == "resnet":
        return CifarResNet(width=32, dropout=dropout)
    if arch == "wide_resnet":
        return CifarResNet(width=48, dropout=dropout)
    if arch == "vit":
        return TinyViT(dropout=dropout)
    if arch == "char_transformer":
        if vocab_size is None:
            raise ValueError("vocab_size is required for char_transformer")
        return TinyCharTransformer(vocab_size=vocab_size, block_size=block_size, dropout=dropout)
    raise ValueError(f"Unknown architecture: {arch}")


def load_cifar(batch_size: int, n_train: int, n_test: int, seed: int):
    try:
        import torchvision.transforms as T
        import torchvision.datasets as datasets

        transform = T.Compose([T.ToTensor(), T.Normalize(CIFAR_MEAN, CIFAR_STD)])
        root = "/kaggle/working/data" if Path("/kaggle/working").exists() else str(OUT_DIR / "data")
        train_ds = datasets.CIFAR10(root, train=True, download=True, transform=transform)
        test_ds = datasets.CIFAR10(root, train=False, download=True, transform=transform)
        rng = np.random.default_rng(seed)
        train_idx = rng.choice(len(train_ds), size=min(n_train, len(train_ds)), replace=False)
        test_idx = rng.choice(len(test_ds), size=min(n_test, len(test_ds)), replace=False)
        train_subset = Subset(train_ds, train_idx)
        test_subset = Subset(test_ds, test_idx)
    except Exception:
        base = OUT_DIR.parent / "05_kaggle" / "data" / "cifar-10-batches-py"
        if not base.exists():
            base = Path("C:/Research/cei/metric-audit-paper-code/experiments/05_kaggle/data/cifar-10-batches-py")
        train_x, train_y, test_x, test_y = load_cifar_pickles(base)
        rng = np.random.default_rng(seed)
        train_idx = rng.choice(len(train_x), size=min(n_train, len(train_x)), replace=False)
        test_idx = rng.choice(len(test_x), size=min(n_test, len(test_x)), replace=False)
        train_subset = TensorDataset(torch.from_numpy(train_x[train_idx]), torch.from_numpy(train_y[train_idx]))
        test_subset = TensorDataset(torch.from_numpy(test_x[test_idx]), torch.from_numpy(test_y[test_idx]))

    train_loader = DataLoader(train_subset, batch_size=batch_size, shuffle=True, num_workers=2, pin_memory=torch.cuda.is_available())
    eval_loader = DataLoader(test_subset, batch_size=batch_size, shuffle=False, num_workers=2, pin_memory=torch.cuda.is_available())
    metric_loader = DataLoader(train_subset, batch_size=batch_size, shuffle=False, num_workers=2, pin_memory=torch.cuda.is_available())
    return train_loader, eval_loader, metric_loader, 10


def load_cifar_pickles(cifar_dir: Path):
    import pickle

    xs, ys = [], []
    for i in range(1, 6):
        with (cifar_dir / f"data_batch_{i}").open("rb") as handle:
            batch = pickle.load(handle, encoding="latin1")
        xs.append(batch["data"])
        ys.extend(batch["labels"])
    with (cifar_dir / "test_batch").open("rb") as handle:
        test = pickle.load(handle, encoding="latin1")
    train_x = np.concatenate(xs).reshape(-1, 3, 32, 32).astype("float32") / 255.0
    test_x = test["data"].reshape(-1, 3, 32, 32).astype("float32") / 255.0
    mean = np.asarray(CIFAR_MEAN, dtype="float32").reshape(1, 3, 1, 1)
    std = np.asarray(CIFAR_STD, dtype="float32").reshape(1, 3, 1, 1)
    return (train_x - mean) / std, np.asarray(ys, dtype="int64"), (test_x - mean) / std, np.asarray(test["labels"], dtype="int64")


def load_char_data(batch_size: int, n_train: int, n_test: int, seed: int, block_size: int):
    path = OUT_DIR / "tinyshakespeare.txt"
    if not path.exists():
        try:
            urllib.request.urlretrieve(
                "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt",
                path,
            )
        except Exception:
            fallback = ("To be, or not to be, that is the question.\n" * 5000)
            path.write_text(fallback, encoding="utf-8")
    text = path.read_text(encoding="utf-8", errors="ignore")
    chars = sorted(set(text))
    stoi = {ch: i for i, ch in enumerate(chars)}
    ids = torch.tensor([stoi[ch] for ch in text], dtype=torch.long)
    split = int(0.9 * len(ids))
    train_ids, test_ids = ids[:split], ids[split:]
    train_ds = CharDataset(train_ids[: min(len(train_ids), n_train + block_size + 1)], block_size)
    test_ds = CharDataset(test_ids[: min(len(test_ids), n_test + block_size + 1)], block_size)
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, num_workers=0)
    eval_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False, num_workers=0)
    metric_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=False, num_workers=0)
    return train_loader, eval_loader, metric_loader, len(chars)


def loss_for_logits(logits: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    if logits.ndim == 3:
        return F.cross_entropy(logits.reshape(-1, logits.size(-1)), y.reshape(-1))
    return F.cross_entropy(logits, y)


def flatten_logits_targets(logits: torch.Tensor, y: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    if logits.ndim == 3:
        return logits.reshape(-1, logits.size(-1)), y.reshape(-1)
    return logits, y


def collect_batch(loader: DataLoader, n: int, device: str) -> tuple[torch.Tensor, torch.Tensor]:
    xs, ys = [], []
    total = 0
    for x, y in loader:
        xs.append(x)
        ys.append(y)
        total += len(x)
        if total >= n:
            break
    x = torch.cat(xs)[:n].to(device)
    y = torch.cat(ys)[:n].to(device)
    return x, y


def evaluate(model: nn.Module, loader: DataLoader, device: str, max_batches: int | None = None) -> dict[str, float]:
    model.eval()
    total_loss, total_correct, total_seen = 0.0, 0, 0
    with torch.no_grad():
        for batch_i, (x, y) in enumerate(loader):
            if max_batches is not None and batch_i >= max_batches:
                break
            x, y = x.to(device), y.to(device)
            logits = model(x)
            flat_logits, flat_y = flatten_logits_targets(logits, y)
            loss = F.cross_entropy(flat_logits, flat_y, reduction="sum")
            total_loss += float(loss)
            total_correct += int((flat_logits.argmax(1) == flat_y).sum())
            total_seen += int(flat_y.numel())
    return {"loss": total_loss / max(1, total_seen), "acc": total_correct / max(1, total_seen)}


def effective_rank_from_eigs(eigs: torch.Tensor | np.ndarray) -> float:
    vals = torch.as_tensor(eigs, dtype=torch.float64).clamp_min(0)
    total = vals.sum()
    if float(total) <= 0:
        return 0.0
    probs = vals / total
    probs = probs[probs > 0]
    return float(torch.exp(-(probs * torch.log(probs)).sum()))


def feature_metrics(model: nn.Module, x: torch.Tensor) -> dict[str, float]:
    model.eval()
    with torch.no_grad():
        _, z = model(x, return_features=True)
        z = z.detach().float()
        zc = z - z.mean(dim=0, keepdim=True)
        gram = zc @ zc.T / max(1, zc.size(1))
        eigs = torch.linalg.eigvalsh(gram.cpu()).clamp_min(0)
        norms = z.norm(dim=1)
        zn = F.normalize(z, dim=1)
        sim = zn @ zn.T
        off_diag = sim[~torch.eye(sim.size(0), dtype=torch.bool, device=sim.device)]
    return {
        "feature_erank": effective_rank_from_eigs(eigs),
        "feature_erank_norm": effective_rank_from_eigs(eigs) / max(1, len(x)),
        "feature_norm_mean": float(norms.mean().cpu()),
        "feature_cosine_mean": float(off_diag.mean().cpu()) if off_diag.numel() else 0.0,
    }


def prediction_metrics(model: nn.Module, x: torch.Tensor, y: torch.Tensor, n_bins: int = 15) -> dict[str, float]:
    model.eval()
    with torch.no_grad():
        logits = model(x)
        flat_logits, flat_y = flatten_logits_targets(logits, y)
        probs = flat_logits.softmax(dim=1)
        conf, pred = probs.max(dim=1)
        correct = (pred == flat_y).float()
        entropy = -(probs.clamp_min(1e-12) * probs.clamp_min(1e-12).log()).sum(dim=1)
        top2 = probs.topk(k=min(2, probs.size(1)), dim=1).values
        margin = top2[:, 0] - (top2[:, 1] if top2.size(1) > 1 else 0)
        one_hot = F.one_hot(flat_y, num_classes=probs.size(1)).float()
        brier = ((probs - one_hot) ** 2).sum(dim=1).mean()
        logit_norm = flat_logits.norm(dim=1).mean()
        ece = torch.tensor(0.0, device=flat_logits.device)
        edges = torch.linspace(0, 1, n_bins + 1, device=flat_logits.device)
        for i in range(n_bins):
            mask = (conf > edges[i]) & (conf <= edges[i + 1])
            if mask.any():
                ece += mask.float().mean() * (conf[mask].mean() - correct[mask].mean()).abs()
    return {
        "confidence_mean": float(conf.mean().cpu()),
        "entropy_mean": float(entropy.mean().cpu()),
        "margin_mean": float(margin.mean().cpu()),
        "brier": float(brier.cpu()),
        "ece": float(ece.cpu()),
        "logit_norm_mean": float(logit_norm.cpu()),
        "metric_batch_acc": float(correct.mean().cpu()),
        "metric_batch_loss": float(F.cross_entropy(flat_logits, flat_y).cpu()),
    }


def parameter_vector(model: nn.Module) -> torch.Tensor:
    return torch.cat([p.detach().flatten().cpu().float() for p in model.parameters()])


def parameter_metrics(model: nn.Module, init_vec: torch.Tensor) -> dict[str, float]:
    vec = parameter_vector(model)
    delta = vec - init_vec
    weight_l2 = float(vec.norm())
    return {
        "weight_l2": weight_l2,
        "weight_l1": float(vec.abs().sum()),
        "weight_linf": float(vec.abs().max()),
        "weight_rms": float(torch.sqrt((vec.square()).mean())),
        "distance_from_init_l2": float(delta.norm()),
        "relative_distance_from_init": float(delta.norm() / (init_vec.norm() + 1e-12)),
        "update_to_weight_ratio": float(delta.norm() / (vec.norm() + 1e-12)),
    }


def grad_vector(model: nn.Module, loss: torch.Tensor, create_graph: bool = False) -> torch.Tensor:
    grads = torch.autograd.grad(loss, [p for p in model.parameters() if p.requires_grad], create_graph=create_graph, retain_graph=create_graph, allow_unused=True)
    flat = [g.flatten() for g in grads if g is not None]
    return torch.cat(flat) if flat else torch.zeros(1, device=loss.device)


def gradient_metrics(model: nn.Module, x: torch.Tensor, y: torch.Tensor) -> dict[str, float]:
    model.eval()
    logits = model(x)
    loss = loss_for_logits(logits, y)
    g = grad_vector(model, loss, create_graph=False).detach()
    return {
        "grad_norm": float(g.norm().cpu()),
        "grad_l1": float(g.abs().sum().cpu()),
        "grad_linf": float(g.abs().max().cpu()),
        "grad_mean_abs": float(g.abs().mean().cpu()),
    }


def fisher_metrics(model: nn.Module, x: torch.Tensor, y: torch.Tensor) -> dict[str, float]:
    model.eval()
    rows = []
    for i in range(len(x)):
        model.zero_grad(set_to_none=True)
        logits = model(x[i : i + 1])
        yi = y[i : i + 1]
        loss = loss_for_logits(logits, yi)
        loss.backward()
        rows.append(torch.cat([p.grad.detach().flatten().cpu().float() for p in model.parameters() if p.grad is not None]))
    if not rows:
        return {}
    G = torch.stack(rows)
    norms_sq = G.square().sum(dim=1)
    dual = (G @ G.T) / len(rows)
    eigs = torch.linalg.eigvalsh(dual).clamp_min(0)
    trace = float(eigs.sum())
    spectral = float(eigs.max()) if eigs.numel() else 0.0
    erank = effective_rank_from_eigs(eigs)
    stable_rank = trace / (spectral + 1e-12)
    condition = float(spectral / (eigs[eigs > 1e-12].min() + 1e-12)) if (eigs > 1e-12).any() else math.nan
    mean_g = G.mean(dim=0)
    per_sample_var = ((G - mean_g) ** 2).sum(dim=1).mean()
    noise_scale = float(per_sample_var / (mean_g.square().sum() + 1e-12))
    p = eigs / (eigs.sum() + 1e-12)
    entropy = float(-(p[p > 0] * p[p > 0].log()).sum())
    return {
        "fisher_trace": trace,
        "fisher_spectral": spectral,
        "fisher_stable_rank": float(stable_rank),
        "fisher_entropy": entropy,
        "fim_erank": erank,
        "fim_norm": erank / len(rows),
        "fisher_condition": condition,
        "grad_noise_scale": noise_scale,
        "per_sample_grad_norm_mean": float(norms_sq.sqrt().mean()),
        "per_sample_grad_norm_std": float(norms_sq.sqrt().std(unbiased=False)),
    }


def sharpness_metric(model: nn.Module, x: torch.Tensor, y: torch.Tensor, rho: float, adaptive: bool = False) -> float:
    backup = copy.deepcopy(model.state_dict())
    model.eval()
    logits = model(x)
    loss0 = loss_for_logits(logits, y)
    model.zero_grad(set_to_none=True)
    loss0.backward()
    if adaptive:
        pieces = [(p.grad * p.detach().abs()).norm() for p in model.parameters() if p.grad is not None]
    else:
        pieces = [p.grad.norm() for p in model.parameters() if p.grad is not None]
    norm = torch.norm(torch.stack(pieces)) if pieces else torch.tensor(0.0, device=x.device)
    if float(norm) <= 1e-12:
        model.load_state_dict(backup)
        return 0.0
    scale = rho / norm
    with torch.no_grad():
        for p in model.parameters():
            if p.grad is None:
                continue
            if adaptive:
                p.add_(p.grad * p.detach().abs().square() * scale)
            else:
                p.add_(p.grad * scale)
    with torch.no_grad():
        loss1 = loss_for_logits(model(x), y)
    model.load_state_dict(backup)
    return float((loss1 - loss0).detach().cpu())


def hessian_metrics(model: nn.Module, x: torch.Tensor, y: torch.Tensor, probes: int = 2, power_steps: int = 4) -> dict[str, float]:
    params = [p for p in model.parameters() if p.requires_grad]
    model.eval()
    logits = model(x)
    loss = loss_for_logits(logits, y)
    grads = torch.autograd.grad(loss, params, create_graph=True, retain_graph=True)
    flat_grad = torch.cat([g.contiguous().view(-1) for g in grads])
    n = flat_grad.numel()
    trace_estimates = []
    for _ in range(probes):
        v = torch.randint(0, 2, (n,), device=x.device, dtype=flat_grad.dtype) * 2 - 1
        hv = torch.autograd.grad((flat_grad * v).sum(), params, retain_graph=True, allow_unused=True)
        flat_hv = torch.cat([h.contiguous().view(-1) for h in hv if h is not None])
        trace_estimates.append(float((v[: flat_hv.numel()] * flat_hv).sum().detach().cpu()))
    v = F.normalize(torch.randn(n, device=x.device), dim=0)
    eig = torch.tensor(0.0, device=x.device)
    for _ in range(power_steps):
        hv = torch.autograd.grad((flat_grad * v).sum(), params, retain_graph=True, allow_unused=True)
        flat_hv = torch.cat([h.contiguous().view(-1) for h in hv if h is not None])
        eig = (v[: flat_hv.numel()] * flat_hv).sum()
        v = F.normalize(flat_hv.detach(), dim=0)
    return {
        "hessian_trace_hutchinson": float(np.mean(trace_estimates)),
        "hessian_top_eig_power": float(eig.detach().cpu()),
    }


def all_metrics(model: nn.Module, init_vec: torch.Tensor, x: torch.Tensor, y: torch.Tensor, heavy: bool = True) -> dict[str, float]:
    out: dict[str, float] = {}
    out.update(prediction_metrics(model, x, y))
    out.update(feature_metrics(model, x))
    out.update(parameter_metrics(model, init_vec))
    out.update(gradient_metrics(model, x, y))
    out.update(fisher_metrics(model, x, y))
    out["sam_sharpness"] = sharpness_metric(model, x, y, rho=0.05, adaptive=False)
    out["asam_sharpness"] = sharpness_metric(model, x, y, rho=0.5, adaptive=True)
    if heavy:
        try:
            out.update(hessian_metrics(model, x[: min(8, len(x))], y[: min(8, len(y))]))
        except Exception as exc:
            out["hessian_error"] = str(exc)[:160]
    out["random_metric"] = float(torch.randn(()))
    return out


@dataclass
class RunConfig:
    suite: str
    arch: str
    run_id: int
    seed: int
    lr: float
    wd: float
    dropout: float
    optimizer: str


def sample_configs(suite: str, architectures: list[str], n_per_arch: int, seed: int) -> list[RunConfig]:
    rng = np.random.default_rng(seed)
    configs = []
    optimizers = ["adamw", "sgd"] if suite == "image" else ["adamw"]
    run_id = 0
    for arch in architectures:
        for _ in range(n_per_arch):
            opt = str(rng.choice(optimizers))
            lr_low, lr_high = (5e-4, 3e-2) if opt == "sgd" else (3e-5, 3e-3)
            configs.append(
                RunConfig(
                    suite=suite,
                    arch=arch,
                    run_id=run_id,
                    seed=int(rng.integers(1, 10_000_000)),
                    lr=float(np.exp(rng.uniform(np.log(lr_low), np.log(lr_high)))),
                    wd=float(np.exp(rng.uniform(np.log(1e-6), np.log(3e-3)))),
                    dropout=float(rng.choice([0.0, 0.05, 0.1, 0.2])),
                    optimizer=opt,
                )
            )
            run_id += 1
    return configs


def make_optimizer(model: nn.Module, cfg: RunConfig):
    if cfg.optimizer == "sgd":
        return torch.optim.SGD(model.parameters(), lr=cfg.lr, momentum=0.9, nesterov=True, weight_decay=cfg.wd)
    return torch.optim.AdamW(model.parameters(), lr=cfg.lr, weight_decay=cfg.wd)


def train_run(
    cfg: RunConfig,
    epochs: int,
    batch_size: int,
    n_train: int,
    n_test: int,
    metric_n: int,
    block_size: int,
    heavy_metrics: bool,
    device: str,
) -> dict[str, float | int | str]:
    set_seed(cfg.seed)
    if cfg.suite == "text":
        train_loader, eval_loader, metric_loader, vocab_size = load_char_data(batch_size, n_train, n_test, cfg.seed, block_size)
        model = make_model("char_transformer", cfg.dropout, vocab_size=vocab_size, block_size=block_size).to(device)
        task = "char_lm"
    else:
        train_loader, eval_loader, metric_loader, vocab_size = load_cifar(batch_size, n_train, n_test, cfg.seed)
        model = make_model(cfg.arch, cfg.dropout).to(device)
        task = "cifar10"
    init_vec = parameter_vector(model)
    optimizer = make_optimizer(model, cfg)
    started = time.time()
    snapshots = sorted(set([max(1, epochs // 2), epochs]))

    row: dict[str, float | int | str] = {
        "suite": cfg.suite,
        "task": task,
        "arch": cfg.arch,
        "run_id": cfg.run_id,
        "seed": cfg.seed,
        "lr": cfg.lr,
        "wd": cfg.wd,
        "dropout": cfg.dropout,
        "optimizer": cfg.optimizer,
        "epochs": epochs,
        "batch_size": batch_size,
        "n_train": n_train,
        "n_test": n_test,
        "metric_n": metric_n,
        "device": device,
    }

    for epoch in range(1, epochs + 1):
        model.train()
        for x, y in train_loader:
            x, y = x.to(device), y.to(device)
            optimizer.zero_grad(set_to_none=True)
            loss = loss_for_logits(model(x), y)
            loss.backward()
            optimizer.step()
        if epoch in snapshots:
            ev = evaluate(model, eval_loader, device)
            row[f"val_loss_ep{epoch}"] = ev["loss"]
            row[f"val_acc_ep{epoch}"] = ev["acc"]

    train_ev = evaluate(model, train_loader, device, max_batches=8)
    val_ev = evaluate(model, eval_loader, device)
    metric_x, metric_y = collect_batch(metric_loader, metric_n, device)
    row["train_loss"] = train_ev["loss"]
    row["train_acc"] = train_ev["acc"]
    row["val_loss"] = val_ev["loss"]
    row["final_acc"] = val_ev["acc"]
    row.update(all_metrics(model, init_vec, metric_x, metric_y, heavy=heavy_metrics))
    row["elapsed_s"] = time.time() - started
    return row


def append_row(path: Path, row: dict[str, float | int | str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists()
    if exists:
        with path.open("r", newline="", encoding="utf-8") as handle:
            fieldnames = next(csv.reader(handle))
    else:
        fieldnames = list(row.keys())
    missing = [k for k in row.keys() if k not in fieldnames]
    if missing and exists:
        rows = []
        with path.open("r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
        fieldnames = fieldnames + missing
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if not exists:
            writer.writeheader()
        writer.writerow({k: row.get(k, "") for k in fieldnames})


def main() -> None:
    parser = argparse.ArgumentParser(description="JMLR-scale MBE metric battery runner.")
    parser.add_argument("--suite", choices=["image", "text"], default=os.environ.get("CEI_SUITE", "image"))
    parser.add_argument("--architectures", default=os.environ.get("CEI_ARCHS", "cnn,resnet,wide_resnet,vit"))
    parser.add_argument("--models-per-arch", type=int, default=int(os.environ.get("CEI_MODELS_PER_ARCH", "80")))
    parser.add_argument("--epochs", type=int, default=int(os.environ.get("CEI_EPOCHS", "25")))
    parser.add_argument("--batch-size", type=int, default=int(os.environ.get("CEI_BATCH_SIZE", "128")))
    parser.add_argument("--n-train", type=int, default=int(os.environ.get("CEI_N_TRAIN", "20000")))
    parser.add_argument("--n-test", type=int, default=int(os.environ.get("CEI_N_TEST", "5000")))
    parser.add_argument("--metric-n", type=int, default=int(os.environ.get("CEI_METRIC_N", "16")))
    parser.add_argument("--block-size", type=int, default=int(os.environ.get("CEI_BLOCK_SIZE", "96")))
    parser.add_argument("--seed", type=int, default=int(os.environ.get("CEI_SEED", "20260627")))
    parser.add_argument("--out", default=os.environ.get("CEI_OUT", "jmlr_confirm_image_results.csv"))
    parser.add_argument("--no-heavy", action="store_true")
    args = parser.parse_args()

    device = device_name()
    archs = ["char_transformer"] if args.suite == "text" else [a.strip() for a in args.architectures.split(",") if a.strip()]
    configs = sample_configs(args.suite, archs, args.models_per_arch, args.seed)
    out_path = Path(args.out)
    done = set()
    if out_path.exists():
        with out_path.open("r", newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                done.add((row.get("suite"), row.get("arch"), int(float(row.get("run_id", -1)))))

    meta = {
        "suite": args.suite,
        "architectures": archs,
        "models_per_arch": args.models_per_arch,
        "epochs": args.epochs,
        "n_train": args.n_train,
        "n_test": args.n_test,
        "metric_n": args.metric_n,
        "device": device,
        "metrics": [
            "fim_norm",
            "fim_erank",
            "fisher_trace",
            "fisher_spectral",
            "fisher_stable_rank",
            "fisher_entropy",
            "fisher_condition",
            "grad_noise_scale",
            "grad_norm",
            "grad_l1",
            "grad_linf",
            "sam_sharpness",
            "asam_sharpness",
            "hessian_trace_hutchinson",
            "hessian_top_eig_power",
            "weight_l2",
            "weight_l1",
            "weight_linf",
            "distance_from_init_l2",
            "relative_distance_from_init",
            "update_to_weight_ratio",
            "confidence_mean",
            "entropy_mean",
            "margin_mean",
            "brier",
            "ece",
            "logit_norm_mean",
            "feature_erank",
            "feature_erank_norm",
            "feature_norm_mean",
            "feature_cosine_mean",
            "random_metric",
        ],
    }
    Path("jmlr_scale_manifest.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta, indent=2), flush=True)

    for i, cfg in enumerate(configs, start=1):
        key = (cfg.suite, cfg.arch, cfg.run_id)
        if key in done:
            print(f"Skipping completed {key}", flush=True)
            continue
        try:
            row = train_run(
                cfg,
                epochs=args.epochs,
                batch_size=args.batch_size,
                n_train=args.n_train,
                n_test=args.n_test,
                metric_n=args.metric_n,
                block_size=args.block_size,
                heavy_metrics=False,
                device=device,
            )
            append_row(out_path, row)
            print(
                f"[{i}/{len(configs)}] {cfg.suite}/{cfg.arch} run={cfg.run_id} "
                f"acc={float(row['final_acc']):.4f} fim={float(row.get('fim_norm', float('nan'))):.4f} "
                f"elapsed={float(row['elapsed_s']):.1f}s",
                flush=True,
            )
        except Exception as exc:
            err = {
                "suite": cfg.suite,
                "task": "error",
                "arch": cfg.arch,
                "run_id": cfg.run_id,
                "seed": cfg.seed,
                "lr": cfg.lr,
                "wd": cfg.wd,
                "dropout": cfg.dropout,
                "optimizer": cfg.optimizer,
                "error": repr(exc),
            }
            append_row(out_path, err)
            print(f"ERROR {cfg}: {exc!r}", flush=True)


if __name__ == "__main__":
    main()
