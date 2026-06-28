# JMLR-Scale Metric Audit

- summary csv: `experiments\07_jmlr_scale\jmlr_image_combined_480_strict_loss_mbe_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed, val_loss`

## pooled

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 480 | -0.161 | -0.114 | weak-or-mixed |
| brier | 480 | -0.731 | -0.484 | survives |
| confidence_mean | 480 | +0.720 | +0.503 | survives |
| distance_from_init_l2 | 480 | +0.438 | +0.325 | survives |
| ece | 480 | -0.693 | -0.494 | survives |
| entropy_mean | 480 | -0.720 | -0.531 | survives |
| feature_cosine_mean | 480 | +0.412 | -0.073 | washout |
| feature_erank | 480 | -0.424 | +0.228 | sign-inversion |
| feature_erank_norm | 480 | -0.424 | +0.228 | sign-inversion |
| feature_norm_mean | 480 | +0.539 | +0.348 | survives |
| fim_erank | 480 | -0.662 | -0.383 | survives |
| fim_norm | 480 | -0.662 | -0.383 | survives |
| fisher_condition | 480 | +0.658 | +0.308 | survives |
| fisher_entropy | 480 | -0.662 | -0.383 | survives |
| fisher_spectral | 480 | -0.379 | -0.292 | survives |
| fisher_stable_rank | 480 | -0.588 | -0.345 | survives |
| fisher_trace | 480 | -0.475 | -0.359 | survives |
| grad_l1 | 480 | -0.336 | -0.398 | survives |
| grad_linf | 480 | -0.422 | -0.385 | survives |
| grad_mean_abs | 480 | -0.454 | -0.374 | survives |
| grad_noise_scale | 480 | +0.047 | +0.009 | weak-or-mixed |
| grad_norm | 480 | -0.476 | -0.350 | survives |
| hessian_top_eig_power | 120 | -0.501 | -0.525 | survives |
| hessian_trace_hutchinson | 120 | -0.588 | -0.434 | survives |
| logit_norm_mean | 480 | +0.733 | +0.466 | survives |
| margin_mean | 480 | +0.724 | +0.493 | survives |
| metric_batch_acc | 480 | +0.701 | +0.394 | survives |
| metric_batch_loss | 480 | -0.733 | -0.495 | survives |
| per_sample_grad_norm_mean | 480 | -0.570 | -0.429 | survives |
| per_sample_grad_norm_std | 480 | -0.351 | -0.304 | survives |
| random_metric | 480 | -0.013 | -0.016 | weak-or-mixed |
| relative_distance_from_init | 480 | +0.416 | +0.304 | survives |
| sam_sharpness | 480 | -0.115 | -0.222 | hidden-after-control |
| train_acc | 480 | +0.783 | +0.525 | survives |
| train_loss | 480 | -0.785 | -0.566 | survives |
| update_to_weight_ratio | 480 | +0.404 | +0.185 | weak-or-mixed |
| weight_l1 | 480 | +0.131 | +0.253 | hidden-after-control |
| weight_l2 | 480 | +0.128 | +0.215 | hidden-after-control |
| weight_linf | 480 | +0.509 | +0.205 | survives |
| weight_rms | 480 | -0.129 | +0.241 | hidden-after-control |

## suite=image

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 480 | -0.161 | -0.114 | weak-or-mixed |
| brier | 480 | -0.731 | -0.484 | survives |
| confidence_mean | 480 | +0.720 | +0.503 | survives |
| distance_from_init_l2 | 480 | +0.438 | +0.325 | survives |
| ece | 480 | -0.693 | -0.494 | survives |
| entropy_mean | 480 | -0.720 | -0.531 | survives |
| feature_cosine_mean | 480 | +0.412 | -0.073 | washout |
| feature_erank | 480 | -0.424 | +0.228 | sign-inversion |
| feature_erank_norm | 480 | -0.424 | +0.228 | sign-inversion |
| feature_norm_mean | 480 | +0.539 | +0.348 | survives |
| fim_erank | 480 | -0.662 | -0.383 | survives |
| fim_norm | 480 | -0.662 | -0.383 | survives |
| fisher_condition | 480 | +0.658 | +0.308 | survives |
| fisher_entropy | 480 | -0.662 | -0.383 | survives |
| fisher_spectral | 480 | -0.379 | -0.292 | survives |
| fisher_stable_rank | 480 | -0.588 | -0.345 | survives |
| fisher_trace | 480 | -0.475 | -0.359 | survives |
| grad_l1 | 480 | -0.336 | -0.398 | survives |
| grad_linf | 480 | -0.422 | -0.385 | survives |
| grad_mean_abs | 480 | -0.454 | -0.374 | survives |
| grad_noise_scale | 480 | +0.047 | +0.009 | weak-or-mixed |
| grad_norm | 480 | -0.476 | -0.350 | survives |
| hessian_top_eig_power | 120 | -0.501 | -0.525 | survives |
| hessian_trace_hutchinson | 120 | -0.588 | -0.434 | survives |
| logit_norm_mean | 480 | +0.733 | +0.466 | survives |
| margin_mean | 480 | +0.724 | +0.493 | survives |
| metric_batch_acc | 480 | +0.701 | +0.394 | survives |
| metric_batch_loss | 480 | -0.733 | -0.495 | survives |
| per_sample_grad_norm_mean | 480 | -0.570 | -0.429 | survives |
| per_sample_grad_norm_std | 480 | -0.351 | -0.304 | survives |
| random_metric | 480 | -0.013 | -0.016 | weak-or-mixed |
| relative_distance_from_init | 480 | +0.416 | +0.304 | survives |
| sam_sharpness | 480 | -0.115 | -0.222 | hidden-after-control |
| train_acc | 480 | +0.783 | +0.525 | survives |
| train_loss | 480 | -0.785 | -0.566 | survives |
| update_to_weight_ratio | 480 | +0.404 | +0.185 | weak-or-mixed |
| weight_l1 | 480 | +0.131 | +0.253 | hidden-after-control |
| weight_l2 | 480 | +0.128 | +0.215 | hidden-after-control |
| weight_linf | 480 | +0.509 | +0.205 | survives |
| weight_rms | 480 | -0.129 | +0.241 | hidden-after-control |

## arch=cnn

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 120 | +0.042 | -0.136 | weak-or-mixed |
| brier | 120 | -0.838 | -0.328 | survives |
| confidence_mean | 120 | +0.672 | +0.154 | weak-or-mixed |
| distance_from_init_l2 | 120 | +0.803 | +0.398 | survives |
| ece | 120 | -0.606 | -0.387 | survives |
| entropy_mean | 120 | -0.665 | -0.185 | weak-or-mixed |
| feature_cosine_mean | 120 | +0.351 | +0.117 | weak-or-mixed |
| feature_erank | 120 | +0.605 | +0.136 | weak-or-mixed |
| feature_erank_norm | 120 | +0.605 | +0.136 | weak-or-mixed |
| feature_norm_mean | 120 | +0.551 | +0.162 | weak-or-mixed |
| fim_erank | 120 | -0.478 | -0.112 | weak-or-mixed |
| fim_norm | 120 | -0.478 | -0.112 | weak-or-mixed |
| fisher_condition | 120 | +0.523 | +0.233 | survives |
| fisher_entropy | 120 | -0.478 | -0.112 | weak-or-mixed |
| fisher_spectral | 120 | -0.391 | -0.356 | survives |
| fisher_stable_rank | 120 | -0.264 | -0.032 | washout |
| fisher_trace | 120 | -0.415 | -0.414 | survives |
| grad_l1 | 120 | -0.474 | -0.358 | survives |
| grad_linf | 120 | -0.210 | -0.115 | weak-or-mixed |
| grad_mean_abs | 120 | -0.474 | -0.358 | survives |
| grad_noise_scale | 120 | +0.141 | +0.063 | weak-or-mixed |
| grad_norm | 120 | -0.414 | -0.355 | survives |
| hessian_top_eig_power | 40 | -0.216 | -0.144 | weak-or-mixed |
| hessian_trace_hutchinson | 40 | -0.315 | -0.438 | survives |
| logit_norm_mean | 120 | +0.774 | +0.290 | survives |
| margin_mean | 120 | +0.676 | +0.143 | weak-or-mixed |
| metric_batch_acc | 120 | +0.758 | +0.143 | weak-or-mixed |
| metric_batch_loss | 120 | -0.833 | -0.299 | survives |
| per_sample_grad_norm_mean | 120 | -0.512 | -0.466 | survives |
| per_sample_grad_norm_std | 120 | -0.238 | -0.237 | survives |
| random_metric | 120 | -0.066 | +0.084 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.803 | +0.398 | survives |
| sam_sharpness | 120 | -0.357 | -0.410 | survives |
| train_acc | 120 | +0.970 | +0.845 | survives |
| train_loss | 120 | -0.974 | -0.722 | survives |
| update_to_weight_ratio | 120 | +0.785 | +0.394 | survives |
| weight_l1 | 120 | +0.765 | +0.234 | survives |
| weight_l2 | 120 | +0.772 | +0.181 | weak-or-mixed |
| weight_linf | 120 | +0.780 | +0.210 | survives |
| weight_rms | 120 | +0.772 | +0.181 | weak-or-mixed |

## arch=resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 120 | -0.411 | -0.351 | survives |
| brier | 120 | -0.454 | -0.344 | survives |
| confidence_mean | 120 | +0.485 | +0.376 | survives |
| distance_from_init_l2 | 120 | +0.796 | +0.438 | survives |
| ece | 120 | -0.463 | -0.380 | survives |
| entropy_mean | 120 | -0.513 | -0.418 | survives |
| feature_cosine_mean | 120 | +0.171 | +0.154 | weak-or-mixed |
| feature_erank | 120 | +0.382 | +0.111 | weak-or-mixed |
| feature_erank_norm | 120 | +0.382 | +0.111 | weak-or-mixed |
| feature_norm_mean | 120 | -0.038 | +0.173 | weak-or-mixed |
| fim_erank | 120 | -0.512 | -0.309 | survives |
| fim_norm | 120 | -0.512 | -0.309 | survives |
| fisher_condition | 120 | +0.529 | +0.196 | weak-or-mixed |
| fisher_entropy | 120 | -0.512 | -0.309 | survives |
| fisher_spectral | 120 | -0.552 | -0.311 | survives |
| fisher_stable_rank | 120 | -0.447 | -0.257 | survives |
| fisher_trace | 120 | -0.619 | -0.377 | survives |
| grad_l1 | 120 | -0.618 | -0.418 | survives |
| grad_linf | 120 | -0.507 | -0.209 | survives |
| grad_mean_abs | 120 | -0.618 | -0.418 | survives |
| grad_noise_scale | 120 | +0.115 | +0.062 | weak-or-mixed |
| grad_norm | 120 | -0.610 | -0.392 | survives |
| hessian_top_eig_power | 40 | -0.625 | -0.412 | survives |
| hessian_trace_hutchinson | 40 | -0.643 | -0.350 | survives |
| logit_norm_mean | 120 | +0.696 | +0.541 | survives |
| margin_mean | 120 | +0.481 | +0.376 | survives |
| metric_batch_acc | 120 | +0.428 | +0.250 | survives |
| metric_batch_loss | 120 | -0.467 | -0.379 | survives |
| per_sample_grad_norm_mean | 120 | -0.669 | -0.439 | survives |
| per_sample_grad_norm_std | 120 | -0.549 | -0.352 | survives |
| random_metric | 120 | -0.086 | +0.130 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.796 | +0.438 | survives |
| sam_sharpness | 120 | -0.684 | -0.443 | survives |
| train_acc | 120 | +0.500 | +0.420 | survives |
| train_loss | 120 | -0.519 | -0.465 | survives |
| update_to_weight_ratio | 120 | +0.777 | +0.258 | survives |
| weight_l1 | 120 | +0.741 | +0.551 | survives |
| weight_l2 | 120 | +0.656 | +0.438 | survives |
| weight_linf | 120 | +0.627 | +0.328 | survives |
| weight_rms | 120 | +0.656 | +0.438 | survives |

## arch=vit

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 120 | -0.168 | +0.037 | weak-or-mixed |
| brier | 120 | -0.452 | -0.541 | survives |
| confidence_mean | 120 | +0.527 | +0.687 | survives |
| distance_from_init_l2 | 120 | +0.505 | +0.490 | survives |
| ece | 120 | -0.199 | -0.362 | hidden-after-control |
| entropy_mean | 120 | -0.513 | -0.709 | survives |
| feature_cosine_mean | 120 | -0.112 | -0.439 | hidden-after-control |
| feature_erank | 120 | -0.118 | +0.381 | hidden-after-control |
| feature_erank_norm | 120 | -0.118 | +0.381 | hidden-after-control |
| feature_norm_mean | 120 | +0.175 | +0.556 | hidden-after-control |
| fim_erank | 120 | -0.407 | -0.470 | survives |
| fim_norm | 120 | -0.407 | -0.470 | survives |
| fisher_condition | 120 | +0.438 | +0.529 | survives |
| fisher_entropy | 120 | -0.407 | -0.470 | survives |
| fisher_spectral | 120 | -0.091 | +0.205 | hidden-after-control |
| fisher_stable_rank | 120 | -0.337 | -0.367 | survives |
| fisher_trace | 120 | -0.261 | -0.031 | washout |
| grad_l1 | 120 | -0.283 | +0.044 | washout |
| grad_linf | 120 | -0.246 | -0.360 | survives |
| grad_mean_abs | 120 | -0.283 | +0.044 | washout |
| grad_noise_scale | 120 | +0.027 | +0.003 | weak-or-mixed |
| grad_norm | 120 | -0.257 | -0.031 | washout |
| logit_norm_mean | 120 | +0.351 | +0.655 | survives |
| margin_mean | 120 | +0.528 | +0.678 | survives |
| metric_batch_acc | 120 | +0.428 | +0.492 | survives |
| metric_batch_loss | 120 | -0.465 | -0.563 | survives |
| per_sample_grad_norm_mean | 120 | -0.379 | -0.275 | survives |
| per_sample_grad_norm_std | 120 | -0.048 | +0.260 | hidden-after-control |
| random_metric | 120 | +0.021 | +0.115 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.507 | +0.495 | survives |
| sam_sharpness | 120 | -0.241 | +0.078 | washout |
| train_acc | 120 | +0.549 | +0.806 | survives |
| train_loss | 120 | -0.544 | -0.807 | survives |
| update_to_weight_ratio | 120 | +0.483 | +0.342 | survives |
| weight_l1 | 120 | +0.385 | +0.261 | survives |
| weight_l2 | 120 | +0.379 | +0.236 | survives |
| weight_linf | 120 | +0.383 | +0.305 | survives |
| weight_rms | 120 | +0.379 | +0.236 | survives |

## arch=wide_resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 120 | -0.682 | -0.341 | survives |
| brier | 120 | -0.490 | -0.619 | survives |
| confidence_mean | 120 | +0.488 | +0.624 | survives |
| distance_from_init_l2 | 120 | +0.719 | +0.231 | survives |
| ece | 120 | -0.491 | -0.631 | survives |
| entropy_mean | 120 | -0.507 | -0.648 | survives |
| feature_cosine_mean | 120 | +0.176 | +0.288 | hidden-after-control |
| feature_erank | 120 | +0.308 | +0.288 | survives |
| feature_erank_norm | 120 | +0.308 | +0.288 | survives |
| feature_norm_mean | 120 | +0.054 | +0.385 | hidden-after-control |
| fim_erank | 120 | -0.390 | -0.111 | weak-or-mixed |
| fim_norm | 120 | -0.390 | -0.111 | weak-or-mixed |
| fisher_condition | 120 | +0.387 | +0.090 | washout |
| fisher_entropy | 120 | -0.390 | -0.111 | weak-or-mixed |
| fisher_spectral | 120 | -0.673 | -0.647 | survives |
| fisher_stable_rank | 120 | -0.333 | -0.066 | washout |
| fisher_trace | 120 | -0.701 | -0.673 | survives |
| grad_l1 | 120 | -0.702 | -0.663 | survives |
| grad_linf | 120 | -0.568 | -0.572 | survives |
| grad_mean_abs | 120 | -0.702 | -0.663 | survives |
| grad_noise_scale | 120 | +0.148 | -0.067 | weak-or-mixed |
| grad_norm | 120 | -0.703 | -0.651 | survives |
| hessian_top_eig_power | 40 | -0.770 | -0.667 | survives |
| hessian_trace_hutchinson | 40 | -0.598 | -0.463 | survives |
| logit_norm_mean | 120 | +0.763 | +0.732 | survives |
| margin_mean | 120 | +0.487 | +0.614 | survives |
| metric_batch_acc | 120 | +0.490 | +0.476 | survives |
| metric_batch_loss | 120 | -0.510 | -0.639 | survives |
| per_sample_grad_norm_mean | 120 | -0.714 | -0.709 | survives |
| per_sample_grad_norm_std | 120 | -0.672 | -0.664 | survives |
| random_metric | 120 | -0.136 | -0.088 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.719 | +0.231 | survives |
| sam_sharpness | 120 | -0.773 | -0.491 | survives |
| train_acc | 120 | +0.352 | +0.540 | survives |
| train_loss | 120 | -0.451 | -0.634 | survives |
| update_to_weight_ratio | 120 | +0.665 | -0.010 | washout |
| weight_l1 | 120 | +0.737 | +0.701 | survives |
| weight_l2 | 120 | +0.660 | +0.669 | survives |
| weight_linf | 120 | +0.649 | +0.534 | survives |
| weight_rms | 120 | +0.660 | +0.669 | survives |
