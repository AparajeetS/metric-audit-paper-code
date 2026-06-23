"""
Marginal Baseline Eval (MBE) — A rigorous evaluation protocol for
auditing representation metrics in deep neural networks.
"""

from .sample_eval import simulate_mbe_evaluation

__all__ = ["simulate_mbe_evaluation"]
