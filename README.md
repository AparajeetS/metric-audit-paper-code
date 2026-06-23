# The Marginal Baseline Eval (MBE)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the **Marginal Baseline Eval (MBE)** repository! 

This repository provides the formal implementation of the MBE protocol — a strict, 4-stage validation methodology designed to rigorously audit representation metrics in deep neural networks. 

It was originally built during a massive case study that mathematically falsified the Gradient Effective Rank (FIM_norm) metric.

## Why Do We Need MBE?

The AI safety and interpretability communities frequently propose internal structural metrics (e.g., representation geometry, effective rank, gradient coherence) to predict generalization or track model health. 

However, many of these metrics are secretly **Loss Proxies**. Because early validation loss trivially predicts final test accuracy, any metric that mathematically correlates with the *magnitude* of the loss will automatically correlate with generalization. Such a metric provides **zero independent structural insight**.

The MBE protocol catches these false positive metrics using a rigorous **partial-correlation baseline control**.

## Installation

```bash
git clone https://github.com/AparajeetS/metric-audit-paper-code.git
cd metric-audit-paper-code
pip install -r requirements.txt
```

## Quickstart: The Sample Eval

We provide a plug-and-play Python script that simulates exactly how MBE detects a disguised loss proxy.

```bash
cd mbe_eval
python sample_eval.py
```

### What happens in `sample_eval.py`?

1. It simulates 30 heterogeneous training runs with varying hyperparameters.
2. It generates a "Proposed Metric" that is secretly just a noisy copy of the early validation loss.
3. **Stage 1 (Absolute Correlation):** It checks if the metric predicts final generalization. It will **PASS**, appearing to be a breakthrough discovery.
4. **Stage 2 (MBE Control):** It runs the partial-correlation control against the trivial baseline (early validation loss). It will instantly **FAIL**, revealing the metric offers zero marginal signal.

### Expected Output

```
==================================================
Marginal Baseline Eval (MBE) - Sample Test Run
==================================================

[Stage 1] Absolute Correlation Check:
  Correlation of Proposed Metric with Final Accuracy: r = -0.952 (p = 1.23e-15)
  -> RESULT: PASS. Metric correlates significantly with generalization.

[Stage 2] The MBE Baseline Control (Partial Correlation):
  Marginal Correlation (Controlling for Early Val Loss): r = 0.087 (p = 0.654)
  -> RESULT: FAIL. The metric offers NO independent predictive signal.
  -> DIAGNOSIS: The proposed metric is a disguised Loss Proxy.
```

## The MBE Protocol (4 Stages)

| Stage | Name | What It Tests |
|-------|------|--------------|
| 1 | **Acid Test** | Monotonic correlations with orthogonal drivers (data size ↑, noise ↑) |
| 2 | **Architectural Invariance** | Survives BatchNorm, LayerNorm without collapsing |
| 3 | **Heterogeneous Grid** | Evaluated across randomized hyperparameters to break collinearity |
| 4 | **Baseline Control** | Partial correlation against trivial baseline (early validation loss) |

## The Full 12-Test Falsification (Case Study)

If you wish to explore the original case study that proved why MBE is necessary — the complete falsification of the Gradient Effective Rank metric (FIM_norm) across MLPs, CNNs, and Transformers — all scripts are preserved in the `experiments/` directory.

See `PAPER.md` for the full technical writeup of the math, the origin story, and the mechanistic autopsy.

## Repository Structure

```
metric-audit-paper-code/
├── mbe_eval/               # The MBE evaluation framework
│   ├── __init__.py
│   └── sample_eval.py      # Plug-and-play sample test
├── experiments/             # All 12 original experiment scripts
│   ├── 01_acid_tests/
│   ├── 02_architecture_tests/
│   └── 03_falsification/
├── metric_audit/            # Core FIM_norm computation library
├── docs/
│   └── RESULTS.md           # Raw numerical results for all 12 tests
├── PAPER.md                 # Full technical writeup
├── requirements.txt
├── LICENSE
└── README.md
```

## Citation

If you use the Marginal Baseline Eval in your own representation evaluation, please cite the accompanying manuscript:

```
Shadangi, A. (2026). Does It Beat the Baseline? A Comprehensive Negative Result 
on Gradient Effective Rank as a Generalization Predictor. arXiv preprint.
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
