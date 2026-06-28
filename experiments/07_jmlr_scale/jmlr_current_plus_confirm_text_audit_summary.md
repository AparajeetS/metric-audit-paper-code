# JMLR-Scale Metric Audit

- summary csv: `experiments\07_jmlr_scale\jmlr_current_plus_confirm_text_audit_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed`

## pooled

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 360 | -0.892 | -0.400 | survives |
| brier | 360 | -0.684 | -0.126 | weak-or-mixed |
| confidence_mean | 360 | +0.778 | +0.181 | weak-or-mixed |
| distance_from_init_l2 | 360 | +0.757 | -0.131 | weak-or-mixed |
| ece | 360 | -0.795 | -0.164 | weak-or-mixed |
| entropy_mean | 360 | -0.813 | -0.235 | survives |
| feature_cosine_mean | 360 | +0.900 | +0.417 | survives |
| feature_erank | 360 | -0.627 | -0.414 | survives |
| feature_erank_norm | 360 | -0.210 | -0.346 | survives |
| feature_norm_mean | 360 | -0.635 | +0.038 | washout |
| fim_erank | 360 | +0.151 | -0.107 | weak-or-mixed |
| fim_norm | 360 | +0.463 | -0.107 | weak-or-mixed |
| fisher_condition | 360 | +0.140 | +0.324 | hidden-after-control |
| fisher_entropy | 360 | +0.151 | -0.107 | weak-or-mixed |
| fisher_spectral | 360 | -0.907 | -0.340 | survives |
| fisher_stable_rank | 360 | +0.449 | +0.037 | washout |
| fisher_trace | 360 | -0.916 | -0.364 | survives |
| grad_l1 | 360 | -0.901 | -0.334 | survives |
| grad_linf | 360 | -0.759 | +0.082 | washout |
| grad_mean_abs | 360 | -0.912 | -0.368 | survives |
| grad_noise_scale | 360 | -0.551 | -0.022 | washout |
| grad_norm | 360 | -0.914 | -0.367 | survives |
| hessian_top_eig_power | 120 | -0.501 | -0.240 | survives |
| hessian_trace_hutchinson | 120 | -0.588 | -0.093 | washout |
| logit_norm_mean | 360 | +0.921 | +0.290 | survives |
| margin_mean | 360 | +0.794 | +0.171 | weak-or-mixed |
| metric_batch_acc | 360 | +0.496 | +0.090 | washout |
| metric_batch_loss | 360 | -0.727 | -0.189 | weak-or-mixed |
| per_sample_grad_norm_mean | 360 | -0.917 | -0.369 | survives |
| per_sample_grad_norm_std | 360 | -0.890 | -0.235 | survives |
| random_metric | 360 | -0.022 | -0.017 | weak-or-mixed |
| relative_distance_from_init | 360 | +0.276 | +0.133 | weak-or-mixed |
| sam_sharpness | 360 | -0.889 | -0.310 | survives |
| train_acc | 360 | +0.741 | +0.218 | survives |
| train_loss | 360 | -0.779 | -0.267 | survives |
| update_to_weight_ratio | 360 | +0.260 | +0.071 | washout |
| val_loss | 360 | -0.973 | -0.837 | survives |
| weight_l1 | 360 | +0.775 | -0.029 | washout |
| weight_l2 | 360 | +0.873 | +0.207 | survives |
| weight_linf | 360 | +0.818 | -0.105 | weak-or-mixed |
| weight_rms | 360 | +0.852 | +0.231 | survives |

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
| asam_sharpness | 200 | -0.813 | -0.400 | survives |
| brier | 200 | -0.240 | +0.014 | washout |
| confidence_mean | 200 | +0.308 | +0.076 | washout |
| distance_from_init_l2 | 200 | +0.752 | +0.198 | weak-or-mixed |
| ece | 200 | -0.268 | -0.015 | washout |
| entropy_mean | 200 | -0.369 | -0.144 | weak-or-mixed |
| feature_cosine_mean | 200 | +0.715 | +0.360 | survives |
| feature_erank | 200 | -0.734 | -0.471 | survives |
| feature_erank_norm | 200 | -0.734 | -0.471 | survives |
| feature_norm_mean | 200 | +0.325 | -0.240 | reverse-inversion |
| fim_erank | 200 | -0.291 | +0.014 | washout |
| fim_norm | 200 | -0.291 | +0.014 | washout |
| fisher_condition | 200 | +0.637 | +0.304 | survives |
| fisher_entropy | 200 | -0.291 | +0.014 | washout |
| fisher_spectral | 200 | -0.809 | -0.388 | survives |
| fisher_stable_rank | 200 | -0.078 | +0.144 | weak-or-mixed |
| fisher_trace | 200 | -0.818 | -0.424 | survives |
| grad_l1 | 200 | -0.822 | -0.435 | survives |
| grad_linf | 200 | -0.131 | +0.231 | hidden-after-control |
| grad_mean_abs | 200 | -0.822 | -0.435 | survives |
| grad_noise_scale | 200 | -0.129 | -0.042 | weak-or-mixed |
| grad_norm | 200 | -0.818 | -0.430 | survives |
| logit_norm_mean | 200 | +0.752 | -0.016 | washout |
| margin_mean | 200 | +0.308 | +0.041 | washout |
| metric_batch_acc | 200 | +0.207 | -0.043 | washout |
| metric_batch_loss | 200 | -0.267 | -0.095 | washout |
| per_sample_grad_norm_mean | 200 | -0.797 | -0.382 | survives |
| per_sample_grad_norm_std | 200 | -0.724 | -0.249 | survives |
| random_metric | 200 | +0.068 | +0.009 | weak-or-mixed |
| relative_distance_from_init | 200 | +0.753 | +0.210 | survives |
| sam_sharpness | 200 | -0.817 | -0.411 | survives |
| train_acc | 200 | +0.257 | +0.113 | weak-or-mixed |
| train_loss | 200 | -0.308 | -0.140 | weak-or-mixed |
| update_to_weight_ratio | 200 | +0.752 | +0.176 | weak-or-mixed |
| val_loss | 200 | -0.930 | -0.861 | survives |
| weight_l1 | 200 | +0.713 | +0.140 | weak-or-mixed |
| weight_l2 | 200 | +0.708 | +0.023 | washout |
| weight_linf | 200 | +0.181 | -0.113 | weak-or-mixed |
| weight_rms | 200 | +0.708 | +0.020 | washout |

## arch=char_transformer

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 200 | -0.813 | -0.400 | survives |
| brier | 200 | -0.240 | +0.014 | washout |
| confidence_mean | 200 | +0.308 | +0.076 | washout |
| distance_from_init_l2 | 200 | +0.752 | +0.198 | weak-or-mixed |
| ece | 200 | -0.268 | -0.015 | washout |
| entropy_mean | 200 | -0.369 | -0.144 | weak-or-mixed |
| feature_cosine_mean | 200 | +0.715 | +0.360 | survives |
| feature_erank | 200 | -0.734 | -0.471 | survives |
| feature_erank_norm | 200 | -0.734 | -0.471 | survives |
| feature_norm_mean | 200 | +0.325 | -0.240 | reverse-inversion |
| fim_erank | 200 | -0.291 | +0.014 | washout |
| fim_norm | 200 | -0.291 | +0.014 | washout |
| fisher_condition | 200 | +0.637 | +0.304 | survives |
| fisher_entropy | 200 | -0.291 | +0.014 | washout |
| fisher_spectral | 200 | -0.809 | -0.388 | survives |
| fisher_stable_rank | 200 | -0.078 | +0.144 | weak-or-mixed |
| fisher_trace | 200 | -0.818 | -0.424 | survives |
| grad_l1 | 200 | -0.822 | -0.435 | survives |
| grad_linf | 200 | -0.131 | +0.231 | hidden-after-control |
| grad_mean_abs | 200 | -0.822 | -0.435 | survives |
| grad_noise_scale | 200 | -0.129 | -0.042 | weak-or-mixed |
| grad_norm | 200 | -0.818 | -0.430 | survives |
| logit_norm_mean | 200 | +0.752 | -0.016 | washout |
| margin_mean | 200 | +0.308 | +0.041 | washout |
| metric_batch_acc | 200 | +0.207 | -0.043 | washout |
| metric_batch_loss | 200 | -0.267 | -0.095 | washout |
| per_sample_grad_norm_mean | 200 | -0.797 | -0.382 | survives |
| per_sample_grad_norm_std | 200 | -0.724 | -0.249 | survives |
| random_metric | 200 | +0.068 | +0.009 | weak-or-mixed |
| relative_distance_from_init | 200 | +0.753 | +0.210 | survives |
| sam_sharpness | 200 | -0.817 | -0.411 | survives |
| train_acc | 200 | +0.257 | +0.113 | weak-or-mixed |
| train_loss | 200 | -0.308 | -0.140 | weak-or-mixed |
| update_to_weight_ratio | 200 | +0.752 | +0.176 | weak-or-mixed |
| val_loss | 200 | -0.930 | -0.861 | survives |
| weight_l1 | 200 | +0.713 | +0.140 | weak-or-mixed |
| weight_l2 | 200 | +0.708 | +0.023 | washout |
| weight_linf | 200 | +0.181 | -0.113 | weak-or-mixed |
| weight_rms | 200 | +0.708 | +0.020 | washout |

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
