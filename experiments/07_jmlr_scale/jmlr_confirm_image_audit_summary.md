# JMLR-Scale Metric Audit

- summary csv: `experiments\07_jmlr_scale\jmlr_confirm_image_audit_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed`

## pooled

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 320 | -0.171 | -0.271 | hidden-after-control |
| brier | 320 | -0.731 | -0.429 | survives |
| confidence_mean | 320 | +0.724 | +0.309 | survives |
| distance_from_init_l2 | 320 | +0.439 | +0.149 | weak-or-mixed |
| ece | 320 | -0.687 | -0.346 | survives |
| entropy_mean | 320 | -0.721 | -0.302 | survives |
| feature_cosine_mean | 320 | +0.409 | +0.115 | weak-or-mixed |
| feature_erank | 320 | -0.430 | +0.184 | weak-or-mixed |
| feature_erank_norm | 320 | -0.430 | +0.184 | weak-or-mixed |
| feature_norm_mean | 320 | +0.527 | +0.214 | survives |
| fim_erank | 320 | -0.651 | -0.199 | weak-or-mixed |
| fim_norm | 320 | -0.651 | -0.199 | weak-or-mixed |
| fisher_condition | 320 | +0.646 | +0.125 | weak-or-mixed |
| fisher_entropy | 320 | -0.651 | -0.199 | weak-or-mixed |
| fisher_spectral | 320 | -0.406 | -0.175 | weak-or-mixed |
| fisher_stable_rank | 320 | -0.575 | -0.168 | weak-or-mixed |
| fisher_trace | 320 | -0.494 | -0.210 | survives |
| grad_l1 | 320 | -0.367 | -0.261 | survives |
| grad_linf | 320 | -0.445 | -0.279 | survives |
| grad_mean_abs | 320 | -0.469 | -0.243 | survives |
| grad_noise_scale | 320 | +0.078 | +0.158 | weak-or-mixed |
| grad_norm | 320 | -0.501 | -0.243 | survives |
| logit_norm_mean | 320 | +0.718 | +0.378 | survives |
| margin_mean | 320 | +0.730 | +0.312 | survives |
| metric_batch_acc | 320 | +0.695 | +0.344 | survives |
| metric_batch_loss | 320 | -0.737 | -0.422 | survives |
| per_sample_grad_norm_mean | 320 | -0.577 | -0.252 | survives |
| per_sample_grad_norm_std | 320 | -0.376 | -0.154 | weak-or-mixed |
| random_metric | 320 | +0.004 | -0.047 | weak-or-mixed |
| relative_distance_from_init | 320 | +0.417 | +0.093 | washout |
| sam_sharpness | 320 | -0.127 | -0.172 | weak-or-mixed |
| train_acc | 320 | +0.778 | +0.454 | survives |
| train_loss | 320 | -0.782 | -0.485 | survives |
| update_to_weight_ratio | 320 | +0.407 | +0.027 | washout |
| val_loss | 320 | -0.822 | -0.736 | survives |
| weight_l1 | 320 | +0.120 | +0.133 | weak-or-mixed |
| weight_l2 | 320 | +0.114 | +0.106 | weak-or-mixed |
| weight_linf | 320 | +0.506 | +0.133 | weak-or-mixed |
| weight_rms | 320 | -0.135 | +0.137 | weak-or-mixed |

## suite=image

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 320 | -0.171 | -0.271 | hidden-after-control |
| brier | 320 | -0.731 | -0.429 | survives |
| confidence_mean | 320 | +0.724 | +0.309 | survives |
| distance_from_init_l2 | 320 | +0.439 | +0.149 | weak-or-mixed |
| ece | 320 | -0.687 | -0.346 | survives |
| entropy_mean | 320 | -0.721 | -0.302 | survives |
| feature_cosine_mean | 320 | +0.409 | +0.115 | weak-or-mixed |
| feature_erank | 320 | -0.430 | +0.184 | weak-or-mixed |
| feature_erank_norm | 320 | -0.430 | +0.184 | weak-or-mixed |
| feature_norm_mean | 320 | +0.527 | +0.214 | survives |
| fim_erank | 320 | -0.651 | -0.199 | weak-or-mixed |
| fim_norm | 320 | -0.651 | -0.199 | weak-or-mixed |
| fisher_condition | 320 | +0.646 | +0.125 | weak-or-mixed |
| fisher_entropy | 320 | -0.651 | -0.199 | weak-or-mixed |
| fisher_spectral | 320 | -0.406 | -0.175 | weak-or-mixed |
| fisher_stable_rank | 320 | -0.575 | -0.168 | weak-or-mixed |
| fisher_trace | 320 | -0.494 | -0.210 | survives |
| grad_l1 | 320 | -0.367 | -0.261 | survives |
| grad_linf | 320 | -0.445 | -0.279 | survives |
| grad_mean_abs | 320 | -0.469 | -0.243 | survives |
| grad_noise_scale | 320 | +0.078 | +0.158 | weak-or-mixed |
| grad_norm | 320 | -0.501 | -0.243 | survives |
| logit_norm_mean | 320 | +0.718 | +0.378 | survives |
| margin_mean | 320 | +0.730 | +0.312 | survives |
| metric_batch_acc | 320 | +0.695 | +0.344 | survives |
| metric_batch_loss | 320 | -0.737 | -0.422 | survives |
| per_sample_grad_norm_mean | 320 | -0.577 | -0.252 | survives |
| per_sample_grad_norm_std | 320 | -0.376 | -0.154 | weak-or-mixed |
| random_metric | 320 | +0.004 | -0.047 | weak-or-mixed |
| relative_distance_from_init | 320 | +0.417 | +0.093 | washout |
| sam_sharpness | 320 | -0.127 | -0.172 | weak-or-mixed |
| train_acc | 320 | +0.778 | +0.454 | survives |
| train_loss | 320 | -0.782 | -0.485 | survives |
| update_to_weight_ratio | 320 | +0.407 | +0.027 | washout |
| val_loss | 320 | -0.822 | -0.736 | survives |
| weight_l1 | 320 | +0.120 | +0.133 | weak-or-mixed |
| weight_l2 | 320 | +0.114 | +0.106 | weak-or-mixed |
| weight_linf | 320 | +0.506 | +0.133 | weak-or-mixed |
| weight_rms | 320 | -0.135 | +0.137 | weak-or-mixed |

## arch=cnn

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 80 | +0.040 | -0.432 | hidden-after-control |
| brier | 80 | -0.842 | -0.693 | survives |
| confidence_mean | 80 | +0.652 | +0.073 | washout |
| distance_from_init_l2 | 80 | +0.778 | +0.157 | weak-or-mixed |
| ece | 80 | -0.609 | -0.472 | survives |
| entropy_mean | 80 | -0.643 | -0.052 | washout |
| feature_cosine_mean | 80 | +0.336 | -0.094 | washout |
| feature_erank | 80 | +0.627 | +0.189 | weak-or-mixed |
| feature_erank_norm | 80 | +0.627 | +0.189 | weak-or-mixed |
| feature_norm_mean | 80 | +0.539 | +0.019 | washout |
| fim_erank | 80 | -0.470 | +0.023 | washout |
| fim_norm | 80 | -0.470 | +0.023 | washout |
| fisher_condition | 80 | +0.501 | -0.124 | weak-or-mixed |
| fisher_entropy | 80 | -0.470 | +0.023 | washout |
| fisher_spectral | 80 | -0.391 | -0.268 | survives |
| fisher_stable_rank | 80 | -0.262 | +0.096 | washout |
| fisher_trace | 80 | -0.430 | -0.261 | survives |
| grad_l1 | 80 | -0.489 | -0.317 | survives |
| grad_linf | 80 | -0.235 | -0.395 | survives |
| grad_mean_abs | 80 | -0.489 | -0.317 | survives |
| grad_noise_scale | 80 | +0.150 | +0.330 | hidden-after-control |
| grad_norm | 80 | -0.427 | -0.347 | survives |
| logit_norm_mean | 80 | +0.740 | +0.056 | washout |
| margin_mean | 80 | +0.666 | +0.113 | weak-or-mixed |
| metric_batch_acc | 80 | +0.759 | +0.582 | survives |
| metric_batch_loss | 80 | -0.834 | -0.662 | survives |
| per_sample_grad_norm_mean | 80 | -0.522 | -0.271 | survives |
| per_sample_grad_norm_std | 80 | -0.247 | -0.215 | survives |
| random_metric | 80 | -0.051 | -0.002 | weak-or-mixed |
| relative_distance_from_init | 80 | +0.778 | +0.157 | weak-or-mixed |
| sam_sharpness | 80 | -0.380 | -0.241 | survives |
| train_acc | 80 | +0.967 | +0.938 | survives |
| train_loss | 80 | -0.974 | -0.932 | survives |
| update_to_weight_ratio | 80 | +0.762 | +0.115 | weak-or-mixed |
| val_loss | 80 | -0.880 | -0.875 | survives |
| weight_l1 | 80 | +0.758 | +0.198 | weak-or-mixed |
| weight_l2 | 80 | +0.757 | +0.083 | washout |
| weight_linf | 80 | +0.766 | +0.176 | weak-or-mixed |
| weight_rms | 80 | +0.757 | +0.081 | washout |

## arch=resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 80 | -0.538 | -0.406 | survives |
| brier | 80 | -0.413 | -0.384 | survives |
| confidence_mean | 80 | +0.425 | +0.375 | survives |
| distance_from_init_l2 | 80 | +0.773 | +0.405 | survives |
| ece | 80 | -0.390 | -0.358 | survives |
| entropy_mean | 80 | -0.449 | -0.377 | survives |
| feature_cosine_mean | 80 | +0.162 | +0.269 | hidden-after-control |
| feature_erank | 80 | +0.343 | +0.175 | weak-or-mixed |
| feature_erank_norm | 80 | +0.343 | +0.175 | weak-or-mixed |
| feature_norm_mean | 80 | -0.019 | +0.110 | weak-or-mixed |
| fim_erank | 80 | -0.467 | -0.256 | survives |
| fim_norm | 80 | -0.467 | -0.256 | survives |
| fisher_condition | 80 | +0.440 | +0.061 | washout |
| fisher_entropy | 80 | -0.467 | -0.256 | survives |
| fisher_spectral | 80 | -0.584 | -0.241 | survives |
| fisher_stable_rank | 80 | -0.384 | -0.198 | weak-or-mixed |
| fisher_trace | 80 | -0.637 | -0.330 | survives |
| grad_l1 | 80 | -0.649 | -0.382 | survives |
| grad_linf | 80 | -0.559 | -0.305 | survives |
| grad_mean_abs | 80 | -0.649 | -0.382 | survives |
| grad_noise_scale | 80 | +0.282 | +0.249 | survives |
| grad_norm | 80 | -0.649 | -0.374 | survives |
| logit_norm_mean | 80 | +0.653 | +0.458 | survives |
| margin_mean | 80 | +0.423 | +0.393 | survives |
| metric_batch_acc | 80 | +0.421 | +0.329 | survives |
| metric_batch_loss | 80 | -0.423 | -0.387 | survives |
| per_sample_grad_norm_mean | 80 | -0.668 | -0.398 | survives |
| per_sample_grad_norm_std | 80 | -0.592 | -0.264 | survives |
| random_metric | 80 | -0.040 | +0.217 | hidden-after-control |
| relative_distance_from_init | 80 | +0.773 | +0.405 | survives |
| sam_sharpness | 80 | -0.741 | -0.317 | survives |
| train_acc | 80 | +0.452 | +0.526 | survives |
| train_loss | 80 | -0.465 | -0.547 | survives |
| update_to_weight_ratio | 80 | +0.749 | +0.248 | survives |
| val_loss | 80 | -0.381 | -0.642 | survives |
| weight_l1 | 80 | +0.700 | +0.489 | survives |
| weight_l2 | 80 | +0.632 | +0.418 | survives |
| weight_linf | 80 | +0.599 | +0.264 | survives |
| weight_rms | 80 | +0.632 | +0.418 | survives |

## arch=vit

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 80 | -0.180 | +0.079 | weak-or-mixed |
| brier | 80 | -0.430 | -0.372 | survives |
| confidence_mean | 80 | +0.483 | +0.461 | survives |
| distance_from_init_l2 | 80 | +0.478 | +0.125 | weak-or-mixed |
| ece | 80 | -0.097 | -0.012 | weak-or-mixed |
| entropy_mean | 80 | -0.472 | -0.464 | survives |
| feature_cosine_mean | 80 | -0.064 | -0.318 | hidden-after-control |
| feature_erank | 80 | -0.149 | +0.333 | hidden-after-control |
| feature_erank_norm | 80 | -0.149 | +0.333 | hidden-after-control |
| feature_norm_mean | 80 | +0.110 | +0.292 | hidden-after-control |
| fim_erank | 80 | -0.343 | -0.206 | survives |
| fim_norm | 80 | -0.343 | -0.206 | survives |
| fisher_condition | 80 | +0.439 | +0.276 | survives |
| fisher_entropy | 80 | -0.343 | -0.206 | survives |
| fisher_spectral | 80 | -0.080 | +0.240 | hidden-after-control |
| fisher_stable_rank | 80 | -0.238 | -0.079 | washout |
| fisher_trace | 80 | -0.221 | +0.123 | weak-or-mixed |
| grad_l1 | 80 | -0.222 | +0.233 | sign-inversion |
| grad_linf | 80 | -0.257 | -0.233 | survives |
| grad_mean_abs | 80 | -0.222 | +0.233 | sign-inversion |
| grad_noise_scale | 80 | +0.031 | -0.030 | weak-or-mixed |
| grad_norm | 80 | -0.206 | +0.146 | weak-or-mixed |
| logit_norm_mean | 80 | +0.344 | +0.382 | survives |
| margin_mean | 80 | +0.481 | +0.469 | survives |
| metric_batch_acc | 80 | +0.386 | +0.307 | survives |
| metric_batch_loss | 80 | -0.435 | -0.366 | survives |
| per_sample_grad_norm_mean | 80 | -0.341 | -0.025 | washout |
| per_sample_grad_norm_std | 80 | -0.026 | +0.321 | hidden-after-control |
| random_metric | 80 | +0.178 | +0.162 | weak-or-mixed |
| relative_distance_from_init | 80 | +0.478 | +0.126 | weak-or-mixed |
| sam_sharpness | 80 | -0.265 | +0.134 | weak-or-mixed |
| train_acc | 80 | +0.503 | +0.560 | survives |
| train_loss | 80 | -0.492 | -0.548 | survives |
| update_to_weight_ratio | 80 | +0.464 | +0.072 | washout |
| val_loss | 80 | -0.446 | -0.471 | survives |
| weight_l1 | 80 | +0.343 | +0.010 | washout |
| weight_l2 | 80 | +0.340 | +0.004 | washout |
| weight_linf | 80 | +0.334 | +0.056 | washout |
| weight_rms | 80 | +0.340 | +0.004 | washout |

## arch=wide_resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 80 | -0.672 | -0.543 | survives |
| brier | 80 | -0.526 | -0.543 | survives |
| confidence_mean | 80 | +0.548 | +0.570 | survives |
| distance_from_init_l2 | 80 | +0.760 | +0.125 | weak-or-mixed |
| ece | 80 | -0.553 | -0.571 | survives |
| entropy_mean | 80 | -0.570 | -0.586 | survives |
| feature_cosine_mean | 80 | +0.143 | +0.159 | weak-or-mixed |
| feature_erank | 80 | +0.327 | +0.164 | weak-or-mixed |
| feature_erank_norm | 80 | +0.327 | +0.164 | weak-or-mixed |
| feature_norm_mean | 80 | +0.082 | +0.245 | hidden-after-control |
| fim_erank | 80 | -0.413 | -0.095 | washout |
| fim_norm | 80 | -0.413 | -0.095 | washout |
| fisher_condition | 80 | +0.524 | +0.070 | washout |
| fisher_entropy | 80 | -0.413 | -0.095 | washout |
| fisher_spectral | 80 | -0.709 | -0.538 | survives |
| fisher_stable_rank | 80 | -0.383 | -0.148 | weak-or-mixed |
| fisher_trace | 80 | -0.736 | -0.602 | survives |
| grad_l1 | 80 | -0.752 | -0.600 | survives |
| grad_linf | 80 | -0.599 | -0.522 | survives |
| grad_mean_abs | 80 | -0.752 | -0.600 | survives |
| grad_noise_scale | 80 | +0.053 | +0.100 | weak-or-mixed |
| grad_norm | 80 | -0.746 | -0.608 | survives |
| logit_norm_mean | 80 | +0.810 | +0.446 | survives |
| margin_mean | 80 | +0.547 | +0.563 | survives |
| metric_batch_acc | 80 | +0.484 | +0.286 | survives |
| metric_batch_loss | 80 | -0.559 | -0.585 | survives |
| per_sample_grad_norm_mean | 80 | -0.755 | -0.631 | survives |
| per_sample_grad_norm_std | 80 | -0.709 | -0.546 | survives |
| random_metric | 80 | -0.161 | -0.190 | weak-or-mixed |
| relative_distance_from_init | 80 | +0.760 | +0.125 | weak-or-mixed |
| sam_sharpness | 80 | -0.755 | -0.417 | survives |
| train_acc | 80 | +0.376 | +0.508 | survives |
| train_loss | 80 | -0.510 | -0.594 | survives |
| update_to_weight_ratio | 80 | +0.721 | +0.006 | washout |
| val_loss | 80 | -0.465 | -0.660 | survives |
| weight_l1 | 80 | +0.759 | +0.352 | survives |
| weight_l2 | 80 | +0.672 | +0.235 | survives |
| weight_linf | 80 | +0.660 | +0.210 | survives |
| weight_rms | 80 | +0.672 | +0.235 | survives |
