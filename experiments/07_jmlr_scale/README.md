# JMLR-Scale Metric Audit

This folder contains the scaled evidence harness for auditing `FIM_norm` and a broad metric battery under Marginal Baseline Evaluation (MBE).

## Runners

- `jmlr_scale_experiment.py`
  - Image suite: CIFAR-10 with CNN, ResNet, wider ResNet, and compact ViT-style Transformer.
  - Text suite: character-level Transformer language model on Tiny Shakespeare, with a fallback corpus if download fails.
  - Restartable CSV output: completed `(suite, arch, run_id)` rows are skipped on rerun.

- `analyze_jmlr_scale.py`
  - Merges CSV shards.
  - Computes raw Spearman metric-to-accuracy correlations.
  - Computes MBE partial-rank correlations controlling `lr`, `wd`, `dropout`, `optimizer`, `arch`, `task`, and `seed`.
  - Labels results as `survives`, `washout`, `sign-inversion`, `reverse-inversion`, `hidden-after-control`, or `weak-or-mixed`.

## Metric Battery

The runner computes more than 20 metrics from the same metric batch:

- FIM/Fisher: `fim_norm`, `fim_erank`, `fisher_trace`, `fisher_spectral`, `fisher_stable_rank`, `fisher_entropy`, `fisher_condition`
- Gradient/noise: `grad_norm`, `grad_l1`, `grad_linf`, `grad_mean_abs`, `grad_noise_scale`, per-sample gradient norm mean/std
- Sharpness: `sam_sharpness`, `asam_sharpness`
- Hessian approximations: `hessian_trace_hutchinson`, `hessian_top_eig_power`
- Parameter/update: `weight_l2`, `weight_l1`, `weight_linf`, `weight_rms`, `distance_from_init_l2`, `relative_distance_from_init`, `update_to_weight_ratio`
- Prediction/calibration: `confidence_mean`, `entropy_mean`, `margin_mean`, `brier`, `ece`, `logit_norm_mean`
- Representation: `feature_erank`, `feature_erank_norm`, `feature_norm_mean`, `feature_cosine_mean`
- Controls: `train_loss`, `train_acc`, `val_loss`, `random_metric`

## Suggested 30-Hour Shards

Kaggle notebooks can time out, so treat the 30-hour budget as multiple restartable shards.

Image shard:

```powershell
$env:CEI_SUITE="image"
$env:CEI_ARCHS="cnn,resnet,wide_resnet,vit"
$env:CEI_MODELS_PER_ARCH="40"
$env:CEI_EPOCHS="25"
$env:CEI_N_TRAIN="20000"
$env:CEI_N_TEST="5000"
$env:CEI_METRIC_N="16"
python jmlr_scale_experiment.py
```

Text/LM shard:

```powershell
$env:CEI_SUITE="text"
$env:CEI_MODELS_PER_ARCH="80"
$env:CEI_EPOCHS="12"
$env:CEI_N_TRAIN="80000"
$env:CEI_N_TEST="12000"
$env:CEI_METRIC_N="12"
$env:CEI_BATCH_SIZE="64"
python jmlr_scale_experiment.py
```

Analysis:

```powershell
python analyze_jmlr_scale.py . --out-prefix jmlr_scale_audit
```

## Interpretation

This is not designed to prove that any metric is universally bad. The intended evidence is a matrix of failure modes:

- metrics that survive MBE,
- metrics that wash out,
- metrics that invert after controlling training determinants,
- metrics that only look useful because the hyperparameter grid induced a marginal association.

That is the JMLR-grade story: MBE as a stress test for metric claims, with `FIM_norm` included as our own good-faith metric that may pass ordinary checks and then fail under a stricter audit.
