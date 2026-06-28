# Metric Audit Paper Code

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/mbe-eval.svg)](https://pypi.org/project/mbe-eval/)

Code and Python package for experiments on **Marginal Baseline Evaluation (MBE)**: an audit protocol for testing whether a proposed generalization metric keeps predictive signal after ordinary training baselines and experimental design variables are controlled.

The current research direction is deliberately empirical. A metric can look useful under raw correlation, weaken after controls, invert sign, or survive in some architectures/tasks but not others. MBE is the framework for making those cases visible instead of treating one pooled correlation as the whole story.

## What This Repository Contains

- `mbe_eval/`: lightweight package for raw and partial rank-correlation audits.
- `examples/`: small demonstrations using FIM_norm and synthetic data.
- `experiments/`: paper-scale and exploratory experiments, including CIFAR-10, transformers/language-model probes, and Kaggle-scale runs.
- Public Kaggle walkthrough: [Audit ML Training Metrics with MBE](https://www.kaggle.com/code/aparajeetshadangi/audit-ml-training-metrics-with-mbe).
- `PAPER.md` and `JMLR_STRATEGY.md`: evolving paper notes and publication strategy.

## Installation

Install the core MBE audit library:

```bash
pip install mbe-eval
```

Current PyPI release: [`mbe-eval==0.2.0`](https://pypi.org/project/mbe-eval/0.2.0/).

For local development from this repository:

```bash
git clone https://github.com/AparajeetS/metric-audit-paper-code.git
cd metric-audit-paper-code
pip install -e .
```

The core install only requires NumPy, pandas, and SciPy. FIM_norm extraction uses PyTorch and is optional:

```bash
pip install "mbe-eval[torch]"
```

## Basic Usage

Audit several candidate metrics in one dataframe:

```python
import pandas as pd
from mbe_eval import audit_metrics

df = pd.DataFrame(
    {
        "fim_norm": [0.42, 0.51, 0.37, 0.65],
        "val_loss_ep20": [1.2, 0.9, 1.4, 0.7],
        "learning_rate": [1e-3, 1e-3, 3e-4, 3e-4],
        "weight_decay": [1e-4, 1e-5, 1e-4, 1e-5],
        "test_accuracy": [0.71, 0.78, 0.68, 0.82],
    }
)

report = audit_metrics(
    df,
    metrics=["fim_norm", "val_loss_ep20"],
    target="test_accuracy",
    controls=["learning_rate", "weight_decay"],
)

print(report[["metric", "raw_r", "partial_r", "classification"]])
```

Use the backward-compatible single-metric API:

```python
from mbe_eval import MBEEvaluator

evaluator = MBEEvaluator(metric_name="FIM_norm", baseline_name="Validation Loss")
report = evaluator.evaluate(metric_vals, baseline_vals, target_vals)
print(report.partial_r, report.classification)
```

## Reproducing Current Experiments

The current paper-scale audit lives in:

```bash
python experiments/07_jmlr_scale/analyze_jmlr_scale.py
```

Earlier falsification experiments are in:

```bash
python experiments/04_falsification/fim_unified_grid.py
python experiments/04_falsification/extract_tables.py
```

The Kaggle-scale scripts under `experiments/07_jmlr_scale/` train and audit image and text models. Their outputs are summarized in `jmlr_scale_v2_audit_summary.md` when downloaded.

## Current Result Snapshot

The current confirmed evidence set contains 680 trained models: 480 CIFAR-10 image models and 200 character-transformer language models.

FIM_norm is the motivating case study:

| Audit | n | Raw rho | MBE partial rho | Class |
|---|---:|---:|---:|---|
| Image only, default controls | 480 | -0.662 | -0.218 | survives |
| Text only, default controls | 200 | -0.291 | +0.014 | washout |
| Full image+text pool | 680 | +0.225 | -0.203 | reverse-inversion |
| Full pool, also controlling validation loss | 680 | +0.225 | -0.300 | reverse-inversion |

The key point is selectivity: MBE weakens fragile pooled artifacts such as FIM_norm, feature rank, weight norms, and distance/update metrics, while several predictors survive, including validation loss, gradient/Fisher magnitude metrics, logit confidence metrics, and metric-batch accuracy.

See [JMLR_RUN_PROGRESS_LOG_2026-06-28.md](JMLR_RUN_PROGRESS_LOG_2026-06-28.md) for the run ledger and [experiments/07_jmlr_scale/ARTIFACTS.md](experiments/07_jmlr_scale/ARTIFACTS.md) for result artifact hashes.

For a public, runnable introduction to the method, see the Kaggle notebook:
[Audit ML Training Metrics with MBE](https://www.kaggle.com/code/aparajeetshadangi/audit-ml-training-metrics-with-mbe).

## Repository Structure

```text
metric-audit-paper-code/
+-- mbe_eval/
|   +-- __init__.py
|   +-- core.py
|   +-- utils.py
|   +-- sample_eval.py
+-- examples/
|   +-- 01_run_acid_test.py
|   +-- 02_run_heterogeneous_grid.py
+-- experiments/
|   +-- 04_falsification/
|   +-- 05_kaggle/
|   +-- 06_independent_audit/
|   +-- 07_jmlr_scale/
+-- JMLR_RUN_PROGRESS_LOG_2026-06-28.md
+-- tests/
+-- pyproject.toml
+-- setup.py
+-- README.md
```

## Citation

```bibtex
@article{shadangi2026mbe,
  title={Marginal Baseline Evaluation for Auditing Generalization Metrics},
  author={Shadangi, Aparajeet},
  year={2026},
  note={Preprint}
}
```

## License

MIT License. See [LICENSE](LICENSE) for details.
