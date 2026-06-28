# Independent Artifact Audit

This report ignores manuscript intent and recomputes rank-based correlations directly from saved CSV artifacts.

## mlp_large_grid_v3_asam

- file: `C:\Research\cei\metric-audit-paper-code\experiments\04_falsification\out\large_grid_v3_asam.csv`
- shape: `1000 x 11`
- family: `mlp`
- mean final accuracy: `0.9408`

| metric | abs_r | partial_r | narrative |
|---|---:|---:|---|
| sam_sharpness | -0.382 | +0.425 | sign-inversion |
| asam_sharpness | +0.160 | +0.519 | weak-or-mixed |
| fim_norm | -0.815 | +0.033 | washout-after-control |
| fisher_trace | +0.077 | +0.522 | weak-or-mixed |
| grad_norm | -0.396 | +0.415 | sign-inversion |
| weight_norm | +0.814 | -0.034 | washout-after-control |

## mlp_unified_grid_current

- file: `C:\Research\cei\metric-audit-paper-code\experiments\04_falsification\out\unified_grid.csv`
- shape: `1000 x 27`
- family: `mlp`
- mean final accuracy: `0.9422`

| metric | abs_r | partial_r | narrative |
|---|---:|---:|---|
| sam_sharpness | -0.439 | +0.399 | sign-inversion |
| asam_sharpness | +0.144 | +0.581 | weak-or-mixed |
| fim_norm | -0.803 | +0.056 | washout-after-control |
| fisher_trace | +0.139 | +0.553 | weak-or-mixed |
| grad_norm | -0.445 | +0.389 | sign-inversion |
| weight_norm | +0.808 | -0.057 | washout-after-control |

| temporal metric | partial_r |
|---|---:|
| sam_sharpness_ep5 | -0.064 |
| sam_sharpness_ep10 | +0.321 |
| sam_sharpness_ep20 | +0.399 |
| sam_sharpness_ep50 | +0.074 |
| asam_sharpness_ep5 | -0.351 |
| asam_sharpness_ep10 | +0.282 |
| asam_sharpness_ep20 | +0.581 |
| asam_sharpness_ep50 | +0.270 |

## cnn_kaggle_local_50

- file: `C:\Research\cei\metric-audit-paper-code\experiments\05_kaggle\kaggle_cifar10_results.csv`
- shape: `50 x 9`
- family: `cnn`
- mean final accuracy: `0.4985`

| metric | abs_r | partial_r | narrative |
|---|---:|---:|---|
| sam_sharpness | +0.648 | +0.331 | positive-signal-survives |
| grad_norm | +0.636 | +0.310 | positive-signal-survives |
| weight_norm | +0.927 | +0.396 | positive-signal-survives |
| fisher_trace | +0.480 | +0.450 | positive-signal-survives |
| fim_norm | +0.376 | +0.445 | positive-signal-survives |
| val_loss | -0.892 | -0.513 | negative-signal-survives |

## cnn_kaggle_download_250

- file: `C:\Users\apara\Downloads\kaggle_cifar10_results (2).csv`
- shape: `250 x 22`
- family: `cnn`
- mean final accuracy: `0.5801`

| metric | abs_r | partial_r | narrative |
|---|---:|---:|---|
| sam_sharpness | -0.105 | -0.167 | weak-or-mixed |
| asam_sharpness | -0.125 | -0.099 | washout-after-control |
| grad_norm | -0.190 | -0.191 | weak-or-mixed |
| weight_norm | -0.018 | +0.087 | washout-after-control |
| fisher_trace | -0.058 | -0.136 | weak-or-mixed |
| fim_norm | -0.051 | -0.069 | washout-after-control |
| val_loss | -0.095 | -0.049 | washout-after-control |

| temporal metric | partial_r |
|---|---:|
| sam_sharpness_ep5 | -0.188 |
| sam_sharpness_ep10 | -0.228 |
| sam_sharpness_ep20 | -0.167 |
| sam_sharpness_ep50 | -0.438 |
| asam_sharpness_ep5 | -0.105 |
| asam_sharpness_ep10 | -0.173 |
| asam_sharpness_ep20 | -0.099 |
| asam_sharpness_ep50 | -0.538 |
