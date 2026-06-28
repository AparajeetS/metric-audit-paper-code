# JMLR-Style Evidence Check for FIM_norm

## Question

Could `FIM_norm` pass the kind of empirical evidence normally used for new metric or measure papers, before applying MBE?

Short answer:

Yes. Under ordinary metric evaluation, `FIM_norm` looks strong enough to motivate a serious paper. That is what makes the MBE failure useful.

## JMLR Metric/Measure Paper Pattern

Recent JMLR examples show that the journal does accept papers centered on metrics, measures, or evaluation metrics:

- "Towards Explainable Evaluation Metrics for Machine Translation" is explicitly about evaluation metrics and argues that strong correlations with human judgments are not enough when metric decisions are opaque.
- "Linear Distance Metric Learning with Noisy Labels" centers on learning a Mahalanobis metric. Its abstract and introduction emphasize theory plus synthetic and real-data experiments.
- "Kernel Partial Correlation Coefficient -- a Measure of Conditional Dependence" introduces a new conditional-dependence measure and reports extensive simulations plus real-data examples against existing procedures.
- "The Weighted Generalised Covariance Measure" introduces a new conditional-independence test statistic and compares it to GCM using simulations and real data.

Common evidence pattern:

1. A clean mathematical definition.
2. Synthetic or controlled experiments where the expected direction is known.
3. Robustness to noise or misspecification.
4. Comparison with existing baselines.
5. Real-data or architecture-transfer examples.
6. Uncertainty estimates or repeated trials.
7. A clear limitation/failure analysis.

## FIM_norm Against That Pattern

### 1. Definition

Pass.

`FIM_norm` is the normalized effective rank of the empirical Fisher dual Gram matrix:

```text
G[i] = per-sample gradient vector
S_dual = G G^T / N
FIM_norm = erank(S_dual) / N
```

This is simple, computable, and interpretable as concentration/spread of per-sample gradient energy.

### 2. Controlled Direction Tests

Pass.

From `C:\Research\cei\cei_v2\fim_norm_summary.txt`:

| Probe | Expected behavior | Observed rho | p-value |
|---|---|---:|---:|
| Label noise, fixed n=400 | more noise -> higher FIM_norm, lower accuracy | -0.770 | 3.41e-03 |
| Capacity, fixed noise=0 | more data -> lower FIM_norm, higher accuracy | -0.937 | 6.99e-06 |

This is a strong normal-evaluation result. The sign is consistent across two orthogonal probes.

### 3. Robustness to Normalization and Architecture

Mostly pass.

From `C:\Research\cei\cei_v2\fim_cnn_summary.txt`:

| Architecture | Probe | rho | p-value | Result |
|---|---|---:|---:|---|
| CNN + BatchNorm | noise | -0.956 | 1.20e-06 | pass |
| CNN + BatchNorm | n_train | -0.837 | 6.93e-04 | pass |

From `C:\Research\cei\cei_v2\fim_transformer_summary.txt`:

| Architecture | Probe | rho | p-value | Result |
|---|---|---:|---:|---|
| Transformer + LayerNorm | noise | -0.476 | 1.18e-01 | correct sign, not significant |
| Transformer + LayerNorm | n_train | -0.951 | 2.04e-06 | pass |

Normal read:

`FIM_norm` transfers better than activation-space CEI because it operates in gradient/parameter space.

### 4. Baseline Metric Comparison

Pass with caveat.

From `C:\Research\cei\cei_v2\fim_baselines_summary.txt`:

| Metric | noise rho | n_train rho | Consistent | Both significant |
|---|---:|---:|---|---|
| FIM_norm | -0.691 | -0.942 | YES | YES |
| trace_norm | -0.765 | -0.781 | YES | YES |
| stable_rank_n | -0.688 | -0.893 | YES | YES |
| spectral_n | -0.222 | -0.308 | YES | NO |
| grad_norm | -0.765 | -0.935 | YES | YES |
| weight_norm | +0.702 | +0.939 | YES | YES |

Normal read:

`FIM_norm` is part of a family of strong gradient-energy metrics. It is not alone, but it is competitive and more theoretically interpretable than raw gradient norm.

Caveat:

This also foreshadows the MBE failure. Several related magnitude metrics pass the same normal tests, suggesting the family may be tracking loss/gradient energy rather than independent geometry.

### 5. Repeated Trials and Confidence Intervals

Pass.

From `C:\Research\cei\cei_v2\fim_bootstrap_ci.txt`:

| Experiment | rho | 95 percent CI |
|---|---:|---|
| MLP n_train FIM_norm | -0.881 | [-0.993, -0.538] |
| MLP epoch-20 FIM_norm | -0.727 | [-0.971, -0.150] |
| CNN noise FIM_norm | -0.956 | [-1.000, -0.780] |
| CNN n_train FIM_norm | -0.837 | [-0.980, -0.413] |

Normal read:

Several confidence intervals exclude zero, so the raw signal is not just a point-estimate artifact.

### 6. Failure Analysis

Pass, and this is where the paper becomes interesting.

From `C:\Research\cei\cei_v2\fim_review_followup.txt`:

| Probe | Raw FIM vs accuracy | Loss vs accuracy | FIM vs accuracy controlling loss |
|---|---:|---:|---:|
| Noise | -0.728 | -0.666 | -0.395, p=8.51e-02 |
| n_train | -0.924 | -0.922 | -0.523, p=1.80e-02 |

The unit-normalized gradient variant also weakens badly:

| Probe | unit-normalized FIM rho |
|---|---:|
| Noise | -0.534 |
| n_train | +0.374 |

Interpretation:

The useful signal appears to be heavily magnitude-driven. That is a mechanism, not a mystery.

## MBE Result

Under later hyperparameter MBE:

| Artifact | raw FIM_norm rho | controlled rho | Result |
|---|---:|---:|---|
| `large_grid_v3_asam.csv` | -0.815 | +0.033 | washout |
| `unified_grid.csv` | -0.803 | +0.056 | washout |
| downloaded 250-row CIFAR CSV | -0.051 | -0.069 | washout |

This is the core story:

`FIM_norm` passes normal evaluation, then fails marginal-baseline evaluation.

## Verdict

Under ordinary JMLR-style metric evidence, `FIM_norm` passes a surprising amount:

- clear definition
- controlled monotonic probes
- architecture transfer
- comparisons to baselines
- bootstrap confidence intervals
- mechanistic follow-up

The claim should not be:

> FIM_norm was obviously bad.

The claim should be:

> FIM_norm was good enough to fool normal metric validation. MBE exposed that its apparent generalization signal was largely derivative of simpler training quantities.

This gives us stronger ammunition than an external critique, because we built the metric, validated it conventionally, and then falsified it ourselves.

## Next FIM_norm Experiments Worth Running

For a JMLR-strength version, run:

1. Three independent replications of the MLP dual-acid test with fixed scripts and saved seeds.
2. A large heterogeneous MLP grid with explicit reports for raw, loss-controlled, and hyperparameter-controlled correlations.
3. A CNN+BatchNorm replication with the same dual-acid design, not just the Kaggle heterogeneous grid.
4. A unit-gradient ablation at the same scale as the positive tests.
5. A positive-control comparison against validation loss and a negative-control comparison against random/permuted metrics.

If these hold, the FIM_norm section can be a very strong "standard validation passes, MBE breaks it" case study.
