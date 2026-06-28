# FIM_norm Under Normal Metric Evaluation

This note separates two questions:

1. Would `FIM_norm` look publishable under ordinary metric-evaluation practice?
2. What happens when it faces marginal-baseline auditing?

The answer is useful for the paper narrative: `FIM_norm` looked good enough that a normal metric paper could plausibly have stopped there. MBE is the stronger test that broke it.

## What Normal Evaluation Would Say

### Dual Acid Test

From `C:\Research\cei\cei_v2\fim_norm_summary.txt`:

| Probe | Raw Spearman rho | p-value | Direction |
|---|---:|---:|---|
| Label noise, fixed n=400 | -0.770 | 3.41e-03 | lower `FIM_norm` is better |
| Capacity, fixed noise=0 | -0.937 | 6.99e-06 | lower `FIM_norm` is better |

This is a strong result by ordinary standards. The metric keeps the same sign across two orthogonal probes:

- more label noise raises `FIM_norm` and lowers test accuracy
- more data lowers `FIM_norm` and raises test accuracy

That is exactly the kind of sign-consistency many proposed metric papers use as evidence.

### Condition Means

From the same summary:

| Condition | `FIM_norm` | Test accuracy |
|---|---:|---:|
| noise=0% | 0.2817 | 0.887 |
| noise=15% | 0.3525 | 0.883 |
| noise=30% | 0.4724 | 0.872 |
| noise=50% | 0.6149 | 0.805 |
| n=40 | 0.6418 | 0.585 |
| n=200 | 0.3870 | 0.830 |
| n=400 | 0.2817 | 0.887 |
| n=800 | 0.1426 | 0.918 |

This is visually and statistically compelling: `FIM_norm` behaves monotonically in both stress directions.

### Cross-Architecture Harness

From `C:\Research\cei\cei_v2\fim_cnn_summary.txt`:

| Architecture | Probe | rho | p-value | Verdict |
|---|---|---:|---:|---|
| CNN + BatchNorm | noise | -0.956 | 1.20e-06 | pass |
| CNN + BatchNorm | n_train | -0.837 | 6.93e-04 | pass |

From `C:\Research\cei\cei_v2\fim_transformer_summary.txt`:

| Architecture | Probe | rho | p-value | Verdict |
|---|---|---:|---:|---|
| Transformer + LayerNorm | noise | -0.476 | 1.18e-01 | correct sign, not significant |
| Transformer + LayerNorm | n_train | -0.951 | 2.04e-06 | pass |

Ordinary read:

> Unlike activation-space CEI, `FIM_norm` survives normalization layers and transfers across MLP, CNN+BatchNorm, and Transformer+LayerNorm settings.

That is a serious positive story before MBE.

### Baseline Metric Comparison

From `C:\Research\cei\cei_v2\fim_baselines_summary.txt`:

| Metric | noise rho | n_train rho | Consistent | Both significant |
|---|---:|---:|---|---|
| `fim_norm` | -0.691 | -0.942 | YES | YES |
| `trace_norm` | -0.765 | -0.781 | YES | YES |
| `stable_rank_n` | -0.688 | -0.893 | YES | YES |
| `spectral_n` | -0.222 | -0.308 | YES | NO |
| `grad_norm` | -0.765 | -0.935 | YES | YES |
| `weight_norm` | +0.702 | +0.939 | YES | YES |

Normal read:

> `FIM_norm` is not the only good-looking metric, but it sits inside a coherent family of gradient-energy metrics that pass conventional tests.

This matters because the later MBE story should not pretend `FIM_norm` was weak. It was strong enough to be dangerous.

### Bootstrap Checks

From `C:\Research\cei\cei_v2\fim_bootstrap_ci.txt`:

| Experiment | rho | 95% CI |
|---|---:|---|
| MLP n_train `FIM_norm` | -0.881 | [-0.993, -0.538] |
| MLP epoch-20 `FIM_norm` | -0.727 | [-0.971, -0.150] |
| CNN noise `FIM_norm` | -0.956 | [-1.000, -0.780] |
| CNN n_train `FIM_norm` | -0.837 | [-0.980, -0.413] |

Normal read:

> The signal is not just a point-estimate artifact; several confidence intervals exclude zero.

## Where MBE Breaks It

The later MBE artifacts show that this positive story is not enough.

From the independent audit:

| Artifact | Raw `FIM_norm` rho | Controlled rho | Result |
|---|---:|---:|---|
| `large_grid_v3_asam.csv` | -0.815 | +0.033 | washout |
| `unified_grid.csv` | -0.803 | +0.056 | washout |
| downloaded 250-row CIFAR CSV | -0.051 | -0.069 | washout |

And from the earlier loss-baseline falsification:

| Test | Result |
|---|---|
| epoch-20 raw `FIM_norm` vs accuracy | -0.514 |
| validation loss vs accuracy | -0.924 |
| `FIM_norm` vs accuracy controlling validation loss | +0.216, p=0.25 |
| validation loss vs accuracy controlling `FIM_norm` | -0.900, p=1.3e-11 |

Interpretation:

> `FIM_norm` passes normal metric tests but fails the marginal question. It tracks a real training-state property, but much of that property is already explained by simpler quantities such as loss, learning rate, weight decay, or gradient magnitude.

## Best Narrative

The story should be:

> We developed `FIM_norm` as a serious candidate metric. Under standard evaluation, it looked promising: it passed dual acid tests, transferred across architectures, beat or matched familiar geometric baselines in several probes, and had bootstrap-supported correlations. Then we applied MBE. The independent signal collapsed. This is the point: ordinary metric validation can certify a metric that is mostly a proxy. MBE catches that failure.

This is stronger than saying "`FIM_norm` is bad."

It says:

> `FIM_norm` is a good-looking metric that our own audit falsified.

That is a clean methodological contribution.

## Suggested Manuscript Role

Use `FIM_norm` as the motivating case study.

Paper structure:

1. Build the candidate metric from a reasonable hypothesis.
2. Show it passes normal metric evaluation.
3. Show it fails MBE.
4. Generalize the lesson to SAM, ASAM, weight norm, Fisher trace, and CNN checkpoint instability.
5. Present MBE as the contribution.

This gives the paper a narrative arc:

> We did not invent MBE to attack other people's metrics. We needed it because it broke our own.
