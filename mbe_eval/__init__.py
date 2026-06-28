from .core import (
    MBEEvaluator,
    MBEReport,
    audit_metric,
    audit_metrics,
    classify_effect,
    partial_rank_corr,
    spearman_corr,
)

__all__ = [
    "MBEEvaluator",
    "MBEReport",
    "audit_metric",
    "audit_metrics",
    "classify_effect",
    "partial_rank_corr",
    "spearman_corr",
    "simulate_mbe_evaluation",
]


def __getattr__(name):
    if name == "simulate_mbe_evaluation":
        from .sample_eval import simulate_mbe_evaluation

        return simulate_mbe_evaluation
    raise AttributeError(f"module 'mbe_eval' has no attribute {name!r}")
