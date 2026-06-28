# JMLR-Scale Metric Audit

- summary csv: `experiments\07_jmlr_scale\jmlr_current_plus_confirm_text_strict_loss_mbe_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed, val_loss`

## pooled

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 360 | -0.892 | -0.169 | weak-or-mixed |
| brier | 360 | -0.684 | -0.180 | weak-or-mixed |
| confidence_mean | 360 | +0.778 | +0.222 | survives |
| distance_from_init_l2 | 360 | +0.757 | +0.118 | weak-or-mixed |
| ece | 360 | -0.795 | -0.141 | weak-or-mixed |
| entropy_mean | 360 | -0.813 | -0.236 | survives |
| feature_cosine_mean | 360 | +0.900 | +0.187 | weak-or-mixed |
| feature_erank | 360 | -0.627 | -0.196 | weak-or-mixed |
| feature_erank_norm | 360 | -0.210 | -0.139 | weak-or-mixed |
| feature_norm_mean | 360 | -0.635 | -0.084 | washout |
| fim_erank | 360 | +0.151 | -0.079 | weak-or-mixed |
| fim_norm | 360 | +0.463 | -0.040 | washout |
| fisher_condition | 360 | +0.140 | +0.225 | hidden-after-control |
| fisher_entropy | 360 | +0.151 | -0.079 | weak-or-mixed |
| fisher_spectral | 360 | -0.907 | -0.348 | survives |
| fisher_stable_rank | 360 | +0.449 | +0.001 | washout |
| fisher_trace | 360 | -0.916 | -0.359 | survives |
| grad_l1 | 360 | -0.901 | -0.368 | survives |
| grad_linf | 360 | -0.759 | -0.138 | weak-or-mixed |
| grad_mean_abs | 360 | -0.912 | -0.368 | survives |
| grad_noise_scale | 360 | -0.551 | -0.015 | washout |
| grad_norm | 360 | -0.914 | -0.355 | survives |
| hessian_top_eig_power | 120 | -0.501 | -0.525 | survives |
| hessian_trace_hutchinson | 120 | -0.588 | -0.434 | survives |
| logit_norm_mean | 360 | +0.921 | +0.295 | survives |
| margin_mean | 360 | +0.794 | +0.194 | weak-or-mixed |
| metric_batch_acc | 360 | +0.496 | +0.138 | weak-or-mixed |
| metric_batch_loss | 360 | -0.727 | -0.209 | survives |
| per_sample_grad_norm_mean | 360 | -0.917 | -0.385 | survives |
| per_sample_grad_norm_std | 360 | -0.890 | -0.361 | survives |
| random_metric | 360 | -0.022 | -0.051 | weak-or-mixed |
| relative_distance_from_init | 360 | +0.276 | +0.314 | survives |
| sam_sharpness | 360 | -0.889 | -0.242 | survives |
| train_acc | 360 | +0.741 | +0.200 | survives |
| train_loss | 360 | -0.779 | -0.210 | survives |
| update_to_weight_ratio | 360 | +0.260 | +0.245 | survives |
| weight_l1 | 360 | +0.775 | +0.014 | washout |
| weight_l2 | 360 | +0.873 | +0.106 | weak-or-mixed |
| weight_linf | 360 | +0.818 | +0.024 | washout |
| weight_rms | 360 | +0.852 | +0.104 | weak-or-mixed |

## suite=image

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 160 | -0.140 | -0.096 | weak-or-mixed |
| brier | 160 | -0.723 | -0.489 | survives |
| confidence_mean | 160 | +0.708 | +0.518 | survives |
| distance_from_init_l2 | 160 | +0.433 | +0.296 | survives |
| ece | 160 | -0.700 | -0.500 | survives |
| entropy_mean | 160 | -0.713 | -0.544 | survives |
| feature_cosine_mean | 160 | +0.417 | -0.034 | washout |
| feature_erank | 160 | -0.409 | +0.254 | sign-inversion |
| feature_erank_norm | 160 | -0.409 | +0.254 | sign-inversion |
| feature_norm_mean | 160 | +0.567 | +0.355 | survives |
| fim_erank | 160 | -0.672 | -0.437 | survives |
| fim_norm | 160 | -0.672 | -0.437 | survives |
| fisher_condition | 160 | +0.680 | +0.314 | survives |
| fisher_entropy | 160 | -0.672 | -0.437 | survives |
| fisher_spectral | 160 | -0.324 | -0.231 | survives |
| fisher_stable_rank | 160 | -0.607 | -0.396 | survives |
| fisher_trace | 160 | -0.430 | -0.321 | survives |
| grad_l1 | 160 | -0.275 | -0.342 | survives |
| grad_linf | 160 | -0.371 | -0.352 | survives |
| grad_mean_abs | 160 | -0.423 | -0.345 | survives |
| grad_noise_scale | 160 | -0.013 | +0.038 | weak-or-mixed |
| grad_norm | 160 | -0.423 | -0.307 | survives |
| hessian_top_eig_power | 120 | -0.501 | -0.525 | survives |
| hessian_trace_hutchinson | 120 | -0.588 | -0.434 | survives |
| logit_norm_mean | 160 | +0.761 | +0.397 | survives |
| margin_mean | 160 | +0.713 | +0.505 | survives |
| metric_batch_acc | 160 | +0.707 | +0.403 | survives |
| metric_batch_loss | 160 | -0.724 | -0.502 | survives |
| per_sample_grad_norm_mean | 160 | -0.551 | -0.430 | survives |
| per_sample_grad_norm_std | 160 | -0.297 | -0.251 | survives |
| random_metric | 160 | -0.048 | -0.043 | weak-or-mixed |
| relative_distance_from_init | 160 | +0.413 | +0.283 | survives |
| sam_sharpness | 160 | -0.093 | -0.224 | hidden-after-control |
| train_acc | 160 | +0.793 | +0.556 | survives |
| train_loss | 160 | -0.792 | -0.603 | survives |
| update_to_weight_ratio | 160 | +0.399 | +0.157 | weak-or-mixed |
| weight_l1 | 160 | +0.156 | +0.242 | hidden-after-control |
| weight_l2 | 160 | +0.159 | +0.237 | hidden-after-control |
| weight_linf | 160 | +0.521 | +0.170 | weak-or-mixed |
| weight_rms | 160 | -0.115 | +0.206 | hidden-after-control |

## suite=text

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 200 | -0.813 | -0.265 | survives |
| brier | 200 | -0.240 | +0.196 | weak-or-mixed |
| confidence_mean | 200 | +0.308 | -0.049 | washout |
| distance_from_init_l2 | 200 | +0.752 | +0.254 | survives |
| ece | 200 | -0.268 | +0.150 | weak-or-mixed |
| entropy_mean | 200 | -0.369 | +0.005 | washout |
| feature_cosine_mean | 200 | +0.715 | +0.231 | survives |
| feature_erank | 200 | -0.734 | -0.312 | survives |
| feature_erank_norm | 200 | -0.734 | -0.312 | survives |
| feature_norm_mean | 200 | +0.325 | -0.152 | weak-or-mixed |
| fim_erank | 200 | -0.291 | +0.188 | weak-or-mixed |
| fim_norm | 200 | -0.291 | +0.188 | weak-or-mixed |
| fisher_condition | 200 | +0.637 | +0.030 | washout |
| fisher_entropy | 200 | -0.291 | +0.188 | weak-or-mixed |
| fisher_spectral | 200 | -0.809 | -0.327 | survives |
| fisher_stable_rank | 200 | -0.078 | +0.175 | weak-or-mixed |
| fisher_trace | 200 | -0.818 | -0.295 | survives |
| grad_l1 | 200 | -0.822 | -0.327 | survives |
| grad_linf | 200 | -0.131 | -0.034 | weak-or-mixed |
| grad_mean_abs | 200 | -0.822 | -0.327 | survives |
| grad_noise_scale | 200 | -0.129 | +0.127 | weak-or-mixed |
| grad_norm | 200 | -0.818 | -0.325 | survives |
| logit_norm_mean | 200 | +0.752 | +0.054 | washout |
| margin_mean | 200 | +0.308 | -0.081 | washout |
| metric_batch_acc | 200 | +0.207 | -0.265 | reverse-inversion |
| metric_batch_loss | 200 | -0.267 | +0.100 | weak-or-mixed |
| per_sample_grad_norm_mean | 200 | -0.797 | -0.219 | survives |
| per_sample_grad_norm_std | 200 | -0.724 | -0.336 | survives |
| random_metric | 200 | +0.068 | -0.042 | weak-or-mixed |
| relative_distance_from_init | 200 | +0.753 | +0.261 | survives |
| sam_sharpness | 200 | -0.817 | -0.327 | survives |
| train_acc | 200 | +0.257 | -0.006 | washout |
| train_loss | 200 | -0.308 | -0.034 | washout |
| update_to_weight_ratio | 200 | +0.752 | +0.235 | survives |
| weight_l1 | 200 | +0.713 | +0.113 | weak-or-mixed |
| weight_l2 | 200 | +0.708 | +0.131 | weak-or-mixed |
| weight_linf | 200 | +0.181 | +0.038 | weak-or-mixed |
| weight_rms | 200 | +0.708 | +0.128 | weak-or-mixed |

## arch=char_transformer

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 200 | -0.813 | -0.265 | survives |
| brier | 200 | -0.240 | +0.196 | weak-or-mixed |
| confidence_mean | 200 | +0.308 | -0.049 | washout |
| distance_from_init_l2 | 200 | +0.752 | +0.254 | survives |
| ece | 200 | -0.268 | +0.150 | weak-or-mixed |
| entropy_mean | 200 | -0.369 | +0.005 | washout |
| feature_cosine_mean | 200 | +0.715 | +0.231 | survives |
| feature_erank | 200 | -0.734 | -0.312 | survives |
| feature_erank_norm | 200 | -0.734 | -0.312 | survives |
| feature_norm_mean | 200 | +0.325 | -0.152 | weak-or-mixed |
| fim_erank | 200 | -0.291 | +0.188 | weak-or-mixed |
| fim_norm | 200 | -0.291 | +0.188 | weak-or-mixed |
| fisher_condition | 200 | +0.637 | +0.030 | washout |
| fisher_entropy | 200 | -0.291 | +0.188 | weak-or-mixed |
| fisher_spectral | 200 | -0.809 | -0.327 | survives |
| fisher_stable_rank | 200 | -0.078 | +0.175 | weak-or-mixed |
| fisher_trace | 200 | -0.818 | -0.295 | survives |
| grad_l1 | 200 | -0.822 | -0.327 | survives |
| grad_linf | 200 | -0.131 | -0.034 | weak-or-mixed |
| grad_mean_abs | 200 | -0.822 | -0.327 | survives |
| grad_noise_scale | 200 | -0.129 | +0.127 | weak-or-mixed |
| grad_norm | 200 | -0.818 | -0.325 | survives |
| logit_norm_mean | 200 | +0.752 | +0.054 | washout |
| margin_mean | 200 | +0.308 | -0.081 | washout |
| metric_batch_acc | 200 | +0.207 | -0.265 | reverse-inversion |
| metric_batch_loss | 200 | -0.267 | +0.100 | weak-or-mixed |
| per_sample_grad_norm_mean | 200 | -0.797 | -0.219 | survives |
| per_sample_grad_norm_std | 200 | -0.724 | -0.336 | survives |
| random_metric | 200 | +0.068 | -0.042 | weak-or-mixed |
| relative_distance_from_init | 200 | +0.753 | +0.261 | survives |
| sam_sharpness | 200 | -0.817 | -0.327 | survives |
| train_acc | 200 | +0.257 | -0.006 | washout |
| train_loss | 200 | -0.308 | -0.034 | washout |
| update_to_weight_ratio | 200 | +0.752 | +0.235 | survives |
| weight_l1 | 200 | +0.713 | +0.113 | weak-or-mixed |
| weight_l2 | 200 | +0.708 | +0.131 | weak-or-mixed |
| weight_linf | 200 | +0.181 | +0.038 | weak-or-mixed |
| weight_rms | 200 | +0.708 | +0.128 | weak-or-mixed |

## arch=cnn

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 40 | +0.036 | -0.040 | weak-or-mixed |
| brier | 40 | -0.829 | +0.016 | washout |
| confidence_mean | 40 | +0.694 | +0.155 | weak-or-mixed |
| distance_from_init_l2 | 40 | +0.850 | +0.550 | survives |
| ece | 40 | -0.617 | -0.250 | survives |
| entropy_mean | 40 | -0.701 | -0.176 | weak-or-mixed |
| feature_cosine_mean | 40 | +0.392 | +0.313 | survives |
| feature_erank | 40 | +0.543 | +0.348 | survives |
| feature_erank_norm | 40 | +0.543 | +0.348 | survives |
| feature_norm_mean | 40 | +0.581 | +0.063 | washout |
| fim_erank | 40 | -0.497 | -0.104 | weak-or-mixed |
| fim_norm | 40 | -0.497 | -0.104 | weak-or-mixed |
| fisher_condition | 40 | +0.579 | +0.324 | survives |
| fisher_entropy | 40 | -0.497 | -0.104 | weak-or-mixed |
| fisher_spectral | 40 | -0.393 | -0.382 | survives |
| fisher_stable_rank | 40 | -0.247 | +0.125 | weak-or-mixed |
| fisher_trace | 40 | -0.373 | -0.367 | survives |
| grad_l1 | 40 | -0.432 | -0.267 | survives |
| grad_linf | 40 | -0.144 | +0.208 | hidden-after-control |
| grad_mean_abs | 40 | -0.432 | -0.267 | survives |
| grad_noise_scale | 40 | +0.134 | -0.113 | weak-or-mixed |
| grad_norm | 40 | -0.384 | -0.213 | survives |
| hessian_top_eig_power | 40 | -0.216 | -0.144 | weak-or-mixed |
| hessian_trace_hutchinson | 40 | -0.315 | -0.438 | survives |
| logit_norm_mean | 40 | +0.843 | +0.282 | survives |
| margin_mean | 40 | +0.690 | +0.119 | weak-or-mixed |
| metric_batch_acc | 40 | +0.755 | -0.248 | reverse-inversion |
| metric_batch_loss | 40 | -0.822 | -0.000 | washout |
| per_sample_grad_norm_mean | 40 | -0.484 | -0.424 | survives |
| per_sample_grad_norm_std | 40 | -0.218 | -0.236 | survives |
| random_metric | 40 | -0.102 | +0.001 | weak-or-mixed |
| relative_distance_from_init | 40 | +0.850 | +0.550 | survives |
| sam_sharpness | 40 | -0.303 | -0.302 | survives |
| train_acc | 40 | +0.977 | +0.820 | survives |
| train_loss | 40 | -0.973 | -0.575 | survives |
| update_to_weight_ratio | 40 | +0.829 | +0.534 | survives |
| weight_l1 | 40 | +0.772 | +0.394 | survives |
| weight_l2 | 40 | +0.798 | +0.430 | survives |
| weight_linf | 40 | +0.804 | +0.441 | survives |
| weight_rms | 40 | +0.798 | +0.430 | survives |

## arch=resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 40 | -0.205 | -0.209 | survives |
| brier | 40 | -0.533 | -0.166 | weak-or-mixed |
| confidence_mean | 40 | +0.585 | +0.292 | survives |
| distance_from_init_l2 | 40 | +0.832 | +0.639 | survives |
| ece | 40 | -0.585 | -0.235 | survives |
| entropy_mean | 40 | -0.616 | -0.345 | survives |
| feature_cosine_mean | 40 | +0.247 | +0.108 | weak-or-mixed |
| feature_erank | 40 | +0.488 | +0.166 | weak-or-mixed |
| feature_erank_norm | 40 | +0.488 | +0.166 | weak-or-mixed |
| feature_norm_mean | 40 | -0.061 | +0.009 | weak-or-mixed |
| fim_erank | 40 | -0.593 | -0.105 | weak-or-mixed |
| fim_norm | 40 | -0.593 | -0.105 | weak-or-mixed |
| fisher_condition | 40 | +0.684 | +0.255 | survives |
| fisher_entropy | 40 | -0.593 | -0.105 | weak-or-mixed |
| fisher_spectral | 40 | -0.487 | -0.197 | weak-or-mixed |
| fisher_stable_rank | 40 | -0.555 | -0.095 | washout |
| fisher_trace | 40 | -0.585 | -0.255 | survives |
| grad_l1 | 40 | -0.582 | -0.285 | survives |
| grad_linf | 40 | -0.429 | -0.018 | washout |
| grad_mean_abs | 40 | -0.582 | -0.285 | survives |
| grad_noise_scale | 40 | -0.165 | -0.201 | hidden-after-control |
| grad_norm | 40 | -0.556 | -0.232 | survives |
| hessian_top_eig_power | 40 | -0.625 | -0.412 | survives |
| hessian_trace_hutchinson | 40 | -0.643 | -0.350 | survives |
| logit_norm_mean | 40 | +0.755 | +0.457 | survives |
| margin_mean | 40 | +0.581 | +0.286 | survives |
| metric_batch_acc | 40 | +0.441 | -0.044 | washout |
| metric_batch_loss | 40 | -0.552 | -0.194 | weak-or-mixed |
| per_sample_grad_norm_mean | 40 | -0.693 | -0.367 | survives |
| per_sample_grad_norm_std | 40 | -0.449 | -0.265 | survives |
| random_metric | 40 | -0.179 | -0.122 | weak-or-mixed |
| relative_distance_from_init | 40 | +0.832 | +0.639 | survives |
| sam_sharpness | 40 | -0.589 | -0.468 | survives |
| train_acc | 40 | +0.557 | +0.066 | washout |
| train_loss | 40 | -0.603 | -0.188 | weak-or-mixed |
| update_to_weight_ratio | 40 | +0.821 | +0.506 | survives |
| weight_l1 | 40 | +0.829 | +0.506 | survives |
| weight_l2 | 40 | +0.700 | +0.213 | survives |
| weight_linf | 40 | +0.682 | +0.203 | survives |
| weight_rms | 40 | +0.700 | +0.213 | survives |

## arch=vit

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 40 | -0.121 | -0.028 | weak-or-mixed |
| brier | 40 | -0.503 | -0.605 | survives |
| confidence_mean | 40 | +0.645 | +0.773 | survives |
| distance_from_init_l2 | 40 | +0.571 | +0.520 | survives |
| ece | 40 | -0.366 | -0.460 | survives |
| entropy_mean | 40 | -0.606 | -0.758 | survives |
| feature_cosine_mean | 40 | -0.214 | -0.647 | survives |
| feature_erank | 40 | -0.065 | +0.505 | hidden-after-control |
| feature_erank_norm | 40 | -0.065 | +0.505 | hidden-after-control |
| feature_norm_mean | 40 | +0.288 | +0.623 | survives |
| fim_erank | 40 | -0.514 | -0.542 | survives |
| fim_norm | 40 | -0.514 | -0.542 | survives |
| fisher_condition | 40 | +0.512 | +0.523 | survives |
| fisher_entropy | 40 | -0.514 | -0.542 | survives |
| fisher_spectral | 40 | -0.080 | +0.220 | hidden-after-control |
| fisher_stable_rank | 40 | -0.533 | -0.595 | survives |
| fisher_trace | 40 | -0.331 | -0.161 | weak-or-mixed |
| grad_l1 | 40 | -0.363 | +0.008 | washout |
| grad_linf | 40 | -0.173 | -0.363 | hidden-after-control |
| grad_mean_abs | 40 | -0.363 | +0.008 | washout |
| grad_noise_scale | 40 | +0.013 | -0.070 | weak-or-mixed |
| grad_norm | 40 | -0.336 | -0.157 | weak-or-mixed |
| logit_norm_mean | 40 | +0.392 | +0.588 | survives |
| margin_mean | 40 | +0.630 | +0.757 | survives |
| metric_batch_acc | 40 | +0.498 | +0.613 | survives |
| metric_batch_loss | 40 | -0.525 | -0.643 | survives |
| per_sample_grad_norm_mean | 40 | -0.457 | -0.358 | survives |
| per_sample_grad_norm_std | 40 | -0.084 | +0.204 | hidden-after-control |
| random_metric | 40 | -0.335 | -0.075 | washout |
| relative_distance_from_init | 40 | +0.571 | +0.520 | survives |
| sam_sharpness | 40 | -0.163 | +0.114 | weak-or-mixed |
| train_acc | 40 | +0.632 | +0.837 | survives |
| train_loss | 40 | -0.642 | -0.836 | survives |
| update_to_weight_ratio | 40 | +0.544 | +0.402 | survives |
| weight_l1 | 40 | +0.452 | +0.101 | weak-or-mixed |
| weight_l2 | 40 | +0.447 | +0.077 | washout |
| weight_linf | 40 | +0.467 | +0.205 | survives |
| weight_rms | 40 | +0.447 | +0.077 | washout |

## arch=wide_resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 40 | -0.672 | -0.469 | survives |
| brier | 40 | -0.393 | -0.653 | survives |
| confidence_mean | 40 | +0.335 | +0.621 | survives |
| distance_from_init_l2 | 40 | +0.593 | -0.036 | washout |
| ece | 40 | -0.337 | -0.680 | survives |
| entropy_mean | 40 | -0.353 | -0.690 | survives |
| feature_cosine_mean | 40 | +0.266 | +0.164 | weak-or-mixed |
| feature_erank | 40 | +0.196 | +0.102 | weak-or-mixed |
| feature_erank_norm | 40 | +0.196 | +0.102 | weak-or-mixed |
| feature_norm_mean | 40 | +0.052 | +0.392 | hidden-after-control |
| fim_erank | 40 | -0.316 | -0.289 | survives |
| fim_norm | 40 | -0.316 | -0.289 | survives |
| fisher_condition | 40 | +0.068 | +0.037 | weak-or-mixed |
| fisher_entropy | 40 | -0.316 | -0.289 | survives |
| fisher_spectral | 40 | -0.577 | -0.708 | survives |
| fisher_stable_rank | 40 | -0.157 | -0.165 | weak-or-mixed |
| fisher_trace | 40 | -0.581 | -0.735 | survives |
| grad_l1 | 40 | -0.588 | -0.754 | survives |
| grad_linf | 40 | -0.454 | -0.669 | survives |
| grad_mean_abs | 40 | -0.588 | -0.754 | survives |
| grad_noise_scale | 40 | +0.386 | +0.304 | survives |
| grad_norm | 40 | -0.599 | -0.738 | survives |
| hessian_top_eig_power | 40 | -0.770 | -0.667 | survives |
| hessian_trace_hutchinson | 40 | -0.598 | -0.463 | survives |
| logit_norm_mean | 40 | +0.622 | +0.753 | survives |
| margin_mean | 40 | +0.336 | +0.591 | survives |
| metric_batch_acc | 40 | +0.470 | +0.522 | survives |
| metric_batch_loss | 40 | -0.397 | -0.697 | survives |
| per_sample_grad_norm_mean | 40 | -0.591 | -0.767 | survives |
| per_sample_grad_norm_std | 40 | -0.568 | -0.726 | survives |
| random_metric | 40 | -0.052 | -0.065 | weak-or-mixed |
| relative_distance_from_init | 40 | +0.593 | -0.036 | washout |
| sam_sharpness | 40 | -0.808 | -0.549 | survives |
| train_acc | 40 | +0.278 | +0.599 | survives |
| train_loss | 40 | -0.302 | -0.677 | survives |
| update_to_weight_ratio | 40 | +0.519 | -0.223 | reverse-inversion |
| weight_l1 | 40 | +0.710 | +0.689 | survives |
| weight_l2 | 40 | +0.671 | +0.637 | survives |
| weight_linf | 40 | +0.655 | +0.472 | survives |
| weight_rms | 40 | +0.671 | +0.637 | survives |
