# JMLR-Scale Metric Audit

- summary csv: `jmlr_scale_v2_audit_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed`

## pooled

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 240 | -0.739 | -0.164 | weak-or-mixed |
| brier | 240 | -0.771 | -0.313 | survives |
| confidence_mean | 240 | +0.833 | +0.317 | survives |
| distance_from_init_l2 | 240 | +0.685 | -0.065 | washout |
| ece | 240 | -0.847 | -0.353 | survives |
| entropy_mean | 240 | -0.855 | -0.356 | survives |
| feature_cosine_mean | 240 | +0.816 | +0.268 | survives |
| feature_erank | 240 | -0.548 | +0.024 | washout |
| feature_erank_norm | 240 | -0.166 | +0.064 | weak-or-mixed |
| feature_norm_mean | 240 | -0.486 | +0.136 | weak-or-mixed |
| fim_erank | 240 | +0.014 | -0.203 | hidden-after-control |
| fim_norm | 240 | +0.309 | -0.200 | weak-or-mixed |
| fisher_condition | 240 | +0.189 | +0.228 | hidden-after-control |
| fisher_entropy | 240 | +0.014 | -0.203 | hidden-after-control |
| fisher_spectral | 240 | -0.792 | -0.116 | weak-or-mixed |
| fisher_stable_rank | 240 | +0.284 | -0.119 | weak-or-mixed |
| fisher_trace | 240 | -0.822 | -0.167 | weak-or-mixed |
| grad_l1 | 240 | -0.775 | -0.153 | weak-or-mixed |
| grad_linf | 240 | -0.756 | -0.208 | survives |
| grad_mean_abs | 240 | -0.818 | -0.192 | weak-or-mixed |
| grad_noise_scale | 240 | -0.477 | +0.078 | washout |
| grad_norm | 240 | -0.819 | -0.176 | weak-or-mixed |
| hessian_top_eig_power | 120 | -0.501 | -0.240 | survives |
| hessian_trace_hutchinson | 120 | -0.588 | -0.093 | washout |
| logit_norm_mean | 240 | +0.907 | +0.322 | survives |
| margin_mean | 240 | +0.844 | +0.306 | survives |
| metric_batch_acc | 240 | +0.619 | +0.296 | survives |
| metric_batch_loss | 240 | -0.802 | -0.353 | survives |
| per_sample_grad_norm_mean | 240 | -0.854 | -0.250 | survives |
| per_sample_grad_norm_std | 240 | -0.781 | -0.064 | washout |
| random_metric | 240 | -0.047 | -0.083 | weak-or-mixed |
| relative_distance_from_init | 240 | +0.229 | +0.165 | weak-or-mixed |
| sam_sharpness | 240 | -0.725 | -0.069 | washout |
| train_acc | 240 | +0.827 | +0.397 | survives |
| train_loss | 240 | -0.851 | -0.467 | survives |
| update_to_weight_ratio | 240 | +0.211 | +0.072 | washout |
| val_loss | 240 | -0.946 | -0.700 | survives |
| weight_l1 | 240 | +0.650 | -0.065 | washout |
| weight_l2 | 240 | +0.738 | +0.118 | weak-or-mixed |
| weight_linf | 240 | +0.826 | +0.141 | weak-or-mixed |
| weight_rms | 240 | +0.659 | +0.082 | washout |

## suite=image

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 160 | -0.140 | -0.165 | weak-or-mixed |
| brier | 160 | -0.723 | -0.423 | survives |
| confidence_mean | 160 | +0.708 | +0.305 | survives |
| distance_from_init_l2 | 160 | +0.433 | +0.126 | weak-or-mixed |
| ece | 160 | -0.700 | -0.382 | survives |
| entropy_mean | 160 | -0.713 | -0.327 | survives |
| feature_cosine_mean | 160 | +0.417 | +0.266 | survives |
| feature_erank | 160 | -0.409 | +0.241 | sign-inversion |
| feature_erank_norm | 160 | -0.409 | +0.241 | sign-inversion |
| feature_norm_mean | 160 | +0.567 | +0.322 | survives |
| fim_erank | 160 | -0.672 | -0.213 | survives |
| fim_norm | 160 | -0.672 | -0.213 | survives |
| fisher_condition | 160 | +0.680 | +0.134 | weak-or-mixed |
| fisher_entropy | 160 | -0.672 | -0.213 | survives |
| fisher_spectral | 160 | -0.324 | -0.060 | washout |
| fisher_stable_rank | 160 | -0.607 | -0.187 | weak-or-mixed |
| fisher_trace | 160 | -0.430 | -0.116 | weak-or-mixed |
| grad_l1 | 160 | -0.275 | -0.119 | weak-or-mixed |
| grad_linf | 160 | -0.371 | -0.251 | survives |
| grad_mean_abs | 160 | -0.423 | -0.158 | weak-or-mixed |
| grad_noise_scale | 160 | -0.013 | +0.089 | weak-or-mixed |
| grad_norm | 160 | -0.423 | -0.127 | weak-or-mixed |
| hessian_top_eig_power | 120 | -0.501 | -0.240 | survives |
| hessian_trace_hutchinson | 120 | -0.588 | -0.093 | washout |
| logit_norm_mean | 160 | +0.761 | +0.367 | survives |
| margin_mean | 160 | +0.713 | +0.297 | survives |
| metric_batch_acc | 160 | +0.707 | +0.378 | survives |
| metric_batch_loss | 160 | -0.724 | -0.417 | survives |
| per_sample_grad_norm_mean | 160 | -0.551 | -0.199 | weak-or-mixed |
| per_sample_grad_norm_std | 160 | -0.297 | -0.023 | washout |
| random_metric | 160 | -0.048 | -0.091 | weak-or-mixed |
| relative_distance_from_init | 160 | +0.413 | +0.094 | washout |
| sam_sharpness | 160 | -0.093 | -0.073 | weak-or-mixed |
| train_acc | 160 | +0.793 | +0.558 | survives |
| train_loss | 160 | -0.792 | -0.595 | survives |
| update_to_weight_ratio | 160 | +0.399 | -0.010 | washout |
| val_loss | 160 | -0.825 | -0.723 | survives |
| weight_l1 | 160 | +0.156 | +0.105 | weak-or-mixed |
| weight_l2 | 160 | +0.159 | +0.163 | weak-or-mixed |
| weight_linf | 160 | +0.521 | +0.232 | survives |
| weight_rms | 160 | -0.115 | +0.105 | weak-or-mixed |

## suite=text

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 80 | -0.828 | -0.422 | survives |
| brier | 80 | -0.280 | +0.048 | washout |
| confidence_mean | 80 | +0.325 | +0.026 | washout |
| distance_from_init_l2 | 80 | +0.768 | +0.244 | survives |
| ece | 80 | -0.279 | -0.016 | washout |
| entropy_mean | 80 | -0.409 | -0.158 | weak-or-mixed |
| feature_cosine_mean | 80 | +0.711 | +0.350 | survives |
| feature_erank | 80 | -0.746 | -0.509 | survives |
| feature_erank_norm | 80 | -0.746 | -0.509 | survives |
| feature_norm_mean | 80 | +0.338 | -0.267 | reverse-inversion |
| fim_erank | 80 | -0.319 | +0.059 | washout |
| fim_norm | 80 | -0.319 | +0.059 | washout |
| fisher_condition | 80 | +0.648 | +0.321 | survives |
| fisher_entropy | 80 | -0.319 | +0.059 | washout |
| fisher_spectral | 80 | -0.829 | -0.432 | survives |
| fisher_stable_rank | 80 | -0.098 | +0.181 | weak-or-mixed |
| fisher_trace | 80 | -0.825 | -0.424 | survives |
| grad_l1 | 80 | -0.830 | -0.437 | survives |
| grad_linf | 80 | -0.105 | +0.255 | hidden-after-control |
| grad_mean_abs | 80 | -0.830 | -0.437 | survives |
| grad_noise_scale | 80 | -0.109 | +0.007 | weak-or-mixed |
| grad_norm | 80 | -0.824 | -0.428 | survives |
| logit_norm_mean | 80 | +0.763 | +0.011 | washout |
| margin_mean | 80 | +0.312 | -0.027 | washout |
| metric_batch_acc | 80 | +0.222 | -0.068 | washout |
| metric_batch_loss | 80 | -0.320 | -0.104 | weak-or-mixed |
| per_sample_grad_norm_mean | 80 | -0.799 | -0.369 | survives |
| per_sample_grad_norm_std | 80 | -0.721 | -0.257 | survives |
| random_metric | 80 | +0.088 | -0.006 | weak-or-mixed |
| relative_distance_from_init | 80 | +0.770 | +0.263 | survives |
| sam_sharpness | 80 | -0.823 | -0.411 | survives |
| train_acc | 80 | +0.320 | +0.120 | weak-or-mixed |
| train_loss | 80 | -0.363 | -0.160 | weak-or-mixed |
| update_to_weight_ratio | 80 | +0.769 | +0.244 | survives |
| val_loss | 80 | -0.937 | -0.872 | survives |
| weight_l1 | 80 | +0.721 | +0.121 | weak-or-mixed |
| weight_l2 | 80 | +0.704 | -0.048 | washout |
| weight_linf | 80 | +0.130 | -0.096 | weak-or-mixed |
| weight_rms | 80 | +0.704 | -0.052 | washout |

## arch=char_transformer

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 80 | -0.828 | -0.422 | survives |
| brier | 80 | -0.280 | +0.048 | washout |
| confidence_mean | 80 | +0.325 | +0.026 | washout |
| distance_from_init_l2 | 80 | +0.768 | +0.244 | survives |
| ece | 80 | -0.279 | -0.016 | washout |
| entropy_mean | 80 | -0.409 | -0.158 | weak-or-mixed |
| feature_cosine_mean | 80 | +0.711 | +0.350 | survives |
| feature_erank | 80 | -0.746 | -0.509 | survives |
| feature_erank_norm | 80 | -0.746 | -0.509 | survives |
| feature_norm_mean | 80 | +0.338 | -0.267 | reverse-inversion |
| fim_erank | 80 | -0.319 | +0.059 | washout |
| fim_norm | 80 | -0.319 | +0.059 | washout |
| fisher_condition | 80 | +0.648 | +0.321 | survives |
| fisher_entropy | 80 | -0.319 | +0.059 | washout |
| fisher_spectral | 80 | -0.829 | -0.432 | survives |
| fisher_stable_rank | 80 | -0.098 | +0.181 | weak-or-mixed |
| fisher_trace | 80 | -0.825 | -0.424 | survives |
| grad_l1 | 80 | -0.830 | -0.437 | survives |
| grad_linf | 80 | -0.105 | +0.255 | hidden-after-control |
| grad_mean_abs | 80 | -0.830 | -0.437 | survives |
| grad_noise_scale | 80 | -0.109 | +0.007 | weak-or-mixed |
| grad_norm | 80 | -0.824 | -0.428 | survives |
| logit_norm_mean | 80 | +0.763 | +0.011 | washout |
| margin_mean | 80 | +0.312 | -0.027 | washout |
| metric_batch_acc | 80 | +0.222 | -0.068 | washout |
| metric_batch_loss | 80 | -0.320 | -0.104 | weak-or-mixed |
| per_sample_grad_norm_mean | 80 | -0.799 | -0.369 | survives |
| per_sample_grad_norm_std | 80 | -0.721 | -0.257 | survives |
| random_metric | 80 | +0.088 | -0.006 | weak-or-mixed |
| relative_distance_from_init | 80 | +0.770 | +0.263 | survives |
| sam_sharpness | 80 | -0.823 | -0.411 | survives |
| train_acc | 80 | +0.320 | +0.120 | weak-or-mixed |
| train_loss | 80 | -0.363 | -0.160 | weak-or-mixed |
| update_to_weight_ratio | 80 | +0.769 | +0.244 | survives |
| val_loss | 80 | -0.937 | -0.872 | survives |
| weight_l1 | 80 | +0.721 | +0.121 | weak-or-mixed |
| weight_l2 | 80 | +0.704 | -0.048 | washout |
| weight_linf | 80 | +0.130 | -0.096 | weak-or-mixed |
| weight_rms | 80 | +0.704 | -0.052 | washout |

## arch=cnn

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 40 | +0.036 | -0.266 | hidden-after-control |
| brier | 40 | -0.829 | -0.599 | survives |
| confidence_mean | 40 | +0.694 | +0.175 | weak-or-mixed |
| distance_from_init_l2 | 40 | +0.850 | +0.450 | survives |
| ece | 40 | -0.617 | -0.412 | survives |
| entropy_mean | 40 | -0.701 | -0.196 | weak-or-mixed |
| feature_cosine_mean | 40 | +0.392 | +0.063 | washout |
| feature_erank | 40 | +0.543 | +0.126 | weak-or-mixed |
| feature_erank_norm | 40 | +0.543 | +0.126 | weak-or-mixed |
| feature_norm_mean | 40 | +0.581 | +0.080 | washout |
| fim_erank | 40 | -0.497 | +0.092 | washout |
| fim_norm | 40 | -0.497 | +0.092 | washout |
| fisher_condition | 40 | +0.579 | -0.002 | washout |
| fisher_entropy | 40 | -0.497 | +0.092 | washout |
| fisher_spectral | 40 | -0.393 | -0.327 | survives |
| fisher_stable_rank | 40 | -0.247 | +0.320 | sign-inversion |
| fisher_trace | 40 | -0.373 | -0.212 | survives |
| grad_l1 | 40 | -0.432 | -0.166 | weak-or-mixed |
| grad_linf | 40 | -0.144 | -0.115 | weak-or-mixed |
| grad_mean_abs | 40 | -0.432 | -0.166 | weak-or-mixed |
| grad_noise_scale | 40 | +0.134 | +0.165 | weak-or-mixed |
| grad_norm | 40 | -0.384 | -0.247 | survives |
| hessian_top_eig_power | 40 | -0.216 | +0.149 | weak-or-mixed |
| hessian_trace_hutchinson | 40 | -0.315 | +0.125 | weak-or-mixed |
| logit_norm_mean | 40 | +0.843 | +0.358 | survives |
| margin_mean | 40 | +0.690 | +0.166 | weak-or-mixed |
| metric_batch_acc | 40 | +0.755 | +0.413 | survives |
| metric_batch_loss | 40 | -0.822 | -0.607 | survives |
| per_sample_grad_norm_mean | 40 | -0.484 | -0.264 | survives |
| per_sample_grad_norm_std | 40 | -0.218 | -0.245 | survives |
| random_metric | 40 | -0.102 | +0.227 | hidden-after-control |
| relative_distance_from_init | 40 | +0.850 | +0.450 | survives |
| sam_sharpness | 40 | -0.303 | -0.039 | washout |
| train_acc | 40 | +0.977 | +0.938 | survives |
| train_loss | 40 | -0.973 | -0.901 | survives |
| update_to_weight_ratio | 40 | +0.829 | +0.414 | survives |
| val_loss | 40 | -0.940 | -0.925 | survives |
| weight_l1 | 40 | +0.772 | +0.280 | survives |
| weight_l2 | 40 | +0.798 | +0.172 | weak-or-mixed |
| weight_linf | 40 | +0.804 | +0.228 | survives |
| weight_rms | 40 | +0.798 | +0.172 | weak-or-mixed |

## arch=resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 40 | -0.205 | -0.261 | survives |
| brier | 40 | -0.533 | -0.287 | survives |
| confidence_mean | 40 | +0.585 | +0.266 | survives |
| distance_from_init_l2 | 40 | +0.832 | +0.498 | survives |
| ece | 40 | -0.585 | -0.241 | survives |
| entropy_mean | 40 | -0.616 | -0.271 | survives |
| feature_cosine_mean | 40 | +0.247 | +0.264 | survives |
| feature_erank | 40 | +0.488 | +0.171 | weak-or-mixed |
| feature_erank_norm | 40 | +0.488 | +0.171 | weak-or-mixed |
| feature_norm_mean | 40 | -0.061 | +0.029 | weak-or-mixed |
| fim_erank | 40 | -0.593 | +0.078 | washout |
| fim_norm | 40 | -0.593 | +0.078 | washout |
| fisher_condition | 40 | +0.684 | +0.158 | weak-or-mixed |
| fisher_entropy | 40 | -0.593 | +0.078 | washout |
| fisher_spectral | 40 | -0.487 | -0.086 | washout |
| fisher_stable_rank | 40 | -0.555 | +0.050 | washout |
| fisher_trace | 40 | -0.585 | -0.125 | weak-or-mixed |
| grad_l1 | 40 | -0.582 | -0.100 | washout |
| grad_linf | 40 | -0.429 | -0.051 | washout |
| grad_mean_abs | 40 | -0.582 | -0.100 | washout |
| grad_noise_scale | 40 | -0.165 | -0.190 | weak-or-mixed |
| grad_norm | 40 | -0.556 | -0.105 | weak-or-mixed |
| hessian_top_eig_power | 40 | -0.625 | -0.253 | survives |
| hessian_trace_hutchinson | 40 | -0.643 | -0.155 | weak-or-mixed |
| logit_norm_mean | 40 | +0.755 | +0.188 | weak-or-mixed |
| margin_mean | 40 | +0.581 | +0.265 | survives |
| metric_batch_acc | 40 | +0.441 | +0.092 | washout |
| metric_batch_loss | 40 | -0.552 | -0.265 | survives |
| per_sample_grad_norm_mean | 40 | -0.693 | -0.262 | survives |
| per_sample_grad_norm_std | 40 | -0.449 | -0.050 | washout |
| random_metric | 40 | -0.179 | -0.213 | hidden-after-control |
| relative_distance_from_init | 40 | +0.832 | +0.498 | survives |
| sam_sharpness | 40 | -0.589 | -0.131 | weak-or-mixed |
| train_acc | 40 | +0.557 | +0.137 | weak-or-mixed |
| train_loss | 40 | -0.603 | -0.236 | survives |
| update_to_weight_ratio | 40 | +0.821 | +0.388 | survives |
| val_loss | 40 | -0.263 | -0.604 | survives |
| weight_l1 | 40 | +0.829 | +0.458 | survives |
| weight_l2 | 40 | +0.700 | +0.097 | washout |
| weight_linf | 40 | +0.682 | +0.196 | weak-or-mixed |
| weight_rms | 40 | +0.700 | +0.097 | washout |

## arch=vit

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 40 | -0.121 | +0.022 | weak-or-mixed |
| brier | 40 | -0.503 | -0.440 | survives |
| confidence_mean | 40 | +0.645 | +0.624 | survives |
| distance_from_init_l2 | 40 | +0.571 | +0.330 | survives |
| ece | 40 | -0.366 | -0.227 | survives |
| entropy_mean | 40 | -0.606 | -0.582 | survives |
| feature_cosine_mean | 40 | -0.214 | -0.592 | survives |
| feature_erank | 40 | -0.065 | +0.545 | hidden-after-control |
| feature_erank_norm | 40 | -0.065 | +0.545 | hidden-after-control |
| feature_norm_mean | 40 | +0.288 | +0.394 | survives |
| fim_erank | 40 | -0.514 | -0.340 | survives |
| fim_norm | 40 | -0.514 | -0.340 | survives |
| fisher_condition | 40 | +0.512 | +0.409 | survives |
| fisher_entropy | 40 | -0.514 | -0.340 | survives |
| fisher_spectral | 40 | -0.080 | +0.272 | hidden-after-control |
| fisher_stable_rank | 40 | -0.533 | -0.436 | survives |
| fisher_trace | 40 | -0.331 | -0.015 | washout |
| grad_l1 | 40 | -0.363 | +0.132 | weak-or-mixed |
| grad_linf | 40 | -0.173 | -0.234 | hidden-after-control |
| grad_mean_abs | 40 | -0.363 | +0.132 | weak-or-mixed |
| grad_noise_scale | 40 | +0.013 | -0.026 | weak-or-mixed |
| grad_norm | 40 | -0.336 | -0.021 | washout |
| logit_norm_mean | 40 | +0.392 | +0.343 | survives |
| margin_mean | 40 | +0.630 | +0.624 | survives |
| metric_batch_acc | 40 | +0.498 | +0.475 | survives |
| metric_batch_loss | 40 | -0.525 | -0.454 | survives |
| per_sample_grad_norm_mean | 40 | -0.457 | -0.119 | weak-or-mixed |
| per_sample_grad_norm_std | 40 | -0.084 | +0.269 | hidden-after-control |
| random_metric | 40 | -0.335 | -0.177 | weak-or-mixed |
| relative_distance_from_init | 40 | +0.571 | +0.330 | survives |
| sam_sharpness | 40 | -0.163 | +0.193 | weak-or-mixed |
| train_acc | 40 | +0.632 | +0.720 | survives |
| train_loss | 40 | -0.642 | -0.714 | survives |
| update_to_weight_ratio | 40 | +0.544 | +0.265 | survives |
| val_loss | 40 | -0.294 | -0.352 | survives |
| weight_l1 | 40 | +0.452 | -0.062 | washout |
| weight_l2 | 40 | +0.447 | -0.087 | washout |
| weight_linf | 40 | +0.467 | +0.025 | washout |
| weight_rms | 40 | +0.447 | -0.087 | washout |

## arch=wide_resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 40 | -0.672 | -0.419 | survives |
| brier | 40 | -0.393 | -0.432 | survives |
| confidence_mean | 40 | +0.335 | +0.390 | survives |
| distance_from_init_l2 | 40 | +0.593 | +0.039 | washout |
| ece | 40 | -0.337 | -0.403 | survives |
| entropy_mean | 40 | -0.353 | -0.444 | survives |
| feature_cosine_mean | 40 | +0.266 | +0.362 | survives |
| feature_erank | 40 | +0.196 | +0.162 | weak-or-mixed |
| feature_erank_norm | 40 | +0.196 | +0.162 | weak-or-mixed |
| feature_norm_mean | 40 | +0.052 | +0.277 | hidden-after-control |
| fim_erank | 40 | -0.316 | -0.071 | washout |
| fim_norm | 40 | -0.316 | -0.071 | washout |
| fisher_condition | 40 | +0.068 | -0.164 | weak-or-mixed |
| fisher_entropy | 40 | -0.316 | -0.071 | washout |
| fisher_spectral | 40 | -0.577 | -0.509 | survives |
| fisher_stable_rank | 40 | -0.157 | +0.119 | weak-or-mixed |
| fisher_trace | 40 | -0.581 | -0.501 | survives |
| grad_l1 | 40 | -0.588 | -0.512 | survives |
| grad_linf | 40 | -0.454 | -0.516 | survives |
| grad_mean_abs | 40 | -0.588 | -0.512 | survives |
| grad_noise_scale | 40 | +0.386 | +0.177 | weak-or-mixed |
| grad_norm | 40 | -0.599 | -0.511 | survives |
| hessian_top_eig_power | 40 | -0.770 | -0.568 | survives |
| hessian_trace_hutchinson | 40 | -0.598 | -0.370 | survives |
| logit_norm_mean | 40 | +0.622 | +0.591 | survives |
| margin_mean | 40 | +0.336 | +0.367 | survives |
| metric_batch_acc | 40 | +0.470 | +0.401 | survives |
| metric_batch_loss | 40 | -0.397 | -0.457 | survives |
| per_sample_grad_norm_mean | 40 | -0.591 | -0.538 | survives |
| per_sample_grad_norm_std | 40 | -0.568 | -0.502 | survives |
| random_metric | 40 | -0.052 | -0.083 | weak-or-mixed |
| relative_distance_from_init | 40 | +0.593 | +0.039 | washout |
| sam_sharpness | 40 | -0.808 | -0.470 | survives |
| train_acc | 40 | +0.278 | +0.463 | survives |
| train_loss | 40 | -0.302 | -0.510 | survives |
| update_to_weight_ratio | 40 | +0.519 | -0.171 | weak-or-mixed |
| val_loss | 40 | -0.482 | -0.796 | survives |
| weight_l1 | 40 | +0.710 | +0.603 | survives |
| weight_l2 | 40 | +0.671 | +0.588 | survives |
| weight_linf | 40 | +0.655 | +0.476 | survives |
| weight_rms | 40 | +0.671 | +0.588 | survives |
