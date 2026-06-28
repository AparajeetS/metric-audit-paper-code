from __future__ import annotations

import math


def _require_torch():
    try:
        import torch
    except ImportError as exc:
        raise ImportError(
            "compute_fim_norm requires PyTorch. Install with `pip install mbe-eval[torch]`."
        ) from exc
    return torch


def compute_fim_norm(model, loss_fn, inputs, targets) -> float:
    """Compute normalized gradient/Fisher effective rank.

    The estimator forms the dual per-sample-gradient Gram matrix
    `G G^T / N`, computes its effective rank, and normalizes by `N`.
    It is intentionally simple and exact for small metric batches; production
    experiments can replace the per-sample loop with `torch.func` or `vmap`.
    """

    torch = _require_torch()
    n_samples = int(inputs.shape[0])
    if n_samples <= 0:
        raise ValueError("inputs must contain at least one sample")

    grads = []
    was_training = getattr(model, "training", False)
    model.eval()
    try:
        for i in range(n_samples):
            model.zero_grad(set_to_none=True)
            loss = loss_fn(model(inputs[i : i + 1]), targets[i : i + 1])
            loss.backward()
            pieces = [p.grad.flatten() for p in model.parameters() if p.grad is not None]
            if not pieces:
                raise ValueError("model produced no parameter gradients")
            grads.append(torch.cat(pieces).detach())
    finally:
        if was_training:
            model.train()

    grad_matrix = torch.stack(grads)
    dual = (grad_matrix @ grad_matrix.T) / n_samples
    eigenvalues = torch.linalg.eigvalsh(dual).clamp_min(1e-12)
    probabilities = eigenvalues / eigenvalues.sum()
    entropy = -(probabilities * torch.log(probabilities)).sum().item()
    return float(math.exp(entropy) / n_samples)


__all__ = ["compute_fim_norm"]
