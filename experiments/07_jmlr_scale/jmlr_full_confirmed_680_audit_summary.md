# JMLR-Scale Metric Audit

- summary csv: `experiments\07_jmlr_scale\jmlr_full_confirmed_680_audit_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed`

## pooled

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 680 | -0.700 | -0.218 | survives |
| brier | 680 | -0.755 | -0.349 | survives |
| confidence_mean | 680 | +0.833 | +0.339 | survives |
| distance_from_init_l2 | 680 | +0.672 | +0.014 | washout |
| ece | 680 | -0.845 | -0.366 | survives |
| entropy_mean | 680 | -0.856 | -0.370 | survives |
| feature_cosine_mean | 680 | +0.786 | +0.164 | weak-or-mixed |
| feature_erank | 680 | -0.538 | +0.097 | washout |
| feature_erank_norm | 680 | -0.179 | +0.139 | weak-or-mixed |
| feature_norm_mean | 680 | -0.425 | +0.071 | washout |
| fim_erank | 680 | -0.068 | -0.206 | hidden-after-control |
| fim_norm | 680 | +0.225 | -0.203 | reverse-inversion |
| fisher_condition | 680 | +0.229 | +0.190 | weak-or-mixed |
| fisher_entropy | 680 | -0.068 | -0.206 | hidden-after-control |
| fisher_spectral | 680 | -0.776 | -0.165 | weak-or-mixed |
| fisher_stable_rank | 680 | +0.199 | -0.126 | weak-or-mixed |
| fisher_trace | 680 | -0.809 | -0.211 | survives |
| grad_l1 | 680 | -0.760 | -0.220 | survives |
| grad_linf | 680 | -0.757 | -0.260 | survives |
| grad_mean_abs | 680 | -0.800 | -0.233 | survives |
| grad_noise_scale | 680 | -0.424 | +0.114 | weak-or-mixed |
| grad_norm | 680 | -0.809 | -0.227 | survives |
| hessian_top_eig_power | 120 | -0.501 | -0.240 | survives |
| hessian_trace_hutchinson | 120 | -0.588 | -0.093 | washout |
| logit_norm_mean | 680 | +0.890 | +0.332 | survives |
| margin_mean | 680 | +0.847 | +0.345 | survives |
| metric_batch_acc | 680 | +0.621 | +0.305 | survives |
| metric_batch_loss | 680 | -0.811 | -0.381 | survives |
| per_sample_grad_norm_mean | 680 | -0.840 | -0.270 | survives |
| per_sample_grad_norm_std | 680 | -0.764 | -0.129 | weak-or-mixed |
| random_metric | 680 | -0.035 | -0.062 | weak-or-mixed |
| relative_distance_from_init | 680 | +0.257 | +0.129 | weak-or-mixed |
| sam_sharpness | 680 | -0.684 | -0.141 | weak-or-mixed |
| train_acc | 680 | +0.814 | +0.378 | survives |
| train_loss | 680 | -0.850 | -0.444 | survives |
| update_to_weight_ratio | 680 | +0.241 | +0.066 | washout |
| val_loss | 680 | -0.935 | -0.698 | survives |
| weight_l1 | 680 | +0.614 | -0.027 | washout |
| weight_l2 | 680 | +0.685 | +0.093 | washout |
| weight_linf | 680 | +0.807 | +0.143 | weak-or-mixed |
| weight_rms | 680 | +0.595 | +0.106 | weak-or-mixed |

## suite=image

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 480 | -0.161 | -0.231 | hidden-after-control |
| brier | 480 | -0.731 | -0.431 | survives |
| confidence_mean | 480 | +0.720 | +0.315 | survives |
| distance_from_init_l2 | 480 | +0.438 | +0.148 | weak-or-mixed |
| ece | 480 | -0.693 | -0.364 | survives |
| entropy_mean | 480 | -0.720 | -0.318 | survives |
| feature_cosine_mean | 480 | +0.412 | +0.164 | weak-or-mixed |
| feature_erank | 480 | -0.424 | +0.199 | weak-or-mixed |
| feature_erank_norm | 480 | -0.424 | +0.199 | weak-or-mixed |
| feature_norm_mean | 480 | +0.539 | +0.254 | survives |
| fim_erank | 480 | -0.662 | -0.218 | survives |
| fim_norm | 480 | -0.662 | -0.218 | survives |
| fisher_condition | 480 | +0.658 | +0.137 | weak-or-mixed |
| fisher_entropy | 480 | -0.662 | -0.218 | survives |
| fisher_spectral | 480 | -0.379 | -0.135 | weak-or-mixed |
| fisher_stable_rank | 480 | -0.588 | -0.186 | weak-or-mixed |
| fisher_trace | 480 | -0.475 | -0.180 | weak-or-mixed |
| grad_l1 | 480 | -0.336 | -0.210 | survives |
| grad_linf | 480 | -0.422 | -0.268 | survives |
| grad_mean_abs | 480 | -0.454 | -0.213 | survives |
| grad_noise_scale | 480 | +0.047 | +0.133 | weak-or-mixed |
| grad_norm | 480 | -0.476 | -0.200 | survives |
| hessian_top_eig_power | 120 | -0.501 | -0.240 | survives |
| hessian_trace_hutchinson | 120 | -0.588 | -0.093 | washout |
| logit_norm_mean | 480 | +0.733 | +0.379 | survives |
| margin_mean | 480 | +0.724 | +0.314 | survives |
| metric_batch_acc | 480 | +0.701 | +0.361 | survives |
| metric_batch_loss | 480 | -0.733 | -0.423 | survives |
| per_sample_grad_norm_mean | 480 | -0.570 | -0.238 | survives |
| per_sample_grad_norm_std | 480 | -0.351 | -0.109 | weak-or-mixed |
| random_metric | 480 | -0.013 | -0.070 | weak-or-mixed |
| relative_distance_from_init | 480 | +0.416 | +0.099 | washout |
| sam_sharpness | 480 | -0.115 | -0.133 | weak-or-mixed |
| train_acc | 480 | +0.783 | +0.496 | survives |
| train_loss | 480 | -0.785 | -0.530 | survives |
| update_to_weight_ratio | 480 | +0.404 | +0.020 | washout |
| val_loss | 480 | -0.822 | -0.730 | survives |
| weight_l1 | 480 | +0.131 | +0.119 | weak-or-mixed |
| weight_l2 | 480 | +0.128 | +0.122 | weak-or-mixed |
| weight_linf | 480 | +0.509 | +0.165 | weak-or-mixed |
| weight_rms | 480 | -0.129 | +0.124 | weak-or-mixed |

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
| asam_sharpness | 120 | +0.042 | -0.382 | hidden-after-control |
| brier | 120 | -0.838 | -0.667 | survives |
| confidence_mean | 120 | +0.672 | +0.110 | weak-or-mixed |
| distance_from_init_l2 | 120 | +0.803 | +0.233 | survives |
| ece | 120 | -0.606 | -0.441 | survives |
| entropy_mean | 120 | -0.665 | -0.092 | washout |
| feature_cosine_mean | 120 | +0.351 | -0.050 | washout |
| feature_erank | 120 | +0.605 | +0.163 | weak-or-mixed |
| feature_erank_norm | 120 | +0.605 | +0.163 | weak-or-mixed |
| feature_norm_mean | 120 | +0.551 | +0.031 | washout |
| fim_erank | 120 | -0.478 | +0.038 | washout |
| fim_norm | 120 | -0.478 | +0.038 | washout |
| fisher_condition | 120 | +0.523 | -0.104 | weak-or-mixed |
| fisher_entropy | 120 | -0.478 | +0.038 | washout |
| fisher_spectral | 120 | -0.391 | -0.268 | survives |
| fisher_stable_rank | 120 | -0.264 | +0.133 | weak-or-mixed |
| fisher_trace | 120 | -0.415 | -0.252 | survives |
| grad_l1 | 120 | -0.474 | -0.280 | survives |
| grad_linf | 120 | -0.210 | -0.328 | survives |
| grad_mean_abs | 120 | -0.474 | -0.280 | survives |
| grad_noise_scale | 120 | +0.141 | +0.286 | hidden-after-control |
| grad_norm | 120 | -0.414 | -0.322 | survives |
| hessian_top_eig_power | 40 | -0.216 | +0.149 | weak-or-mixed |
| hessian_trace_hutchinson | 40 | -0.315 | +0.125 | weak-or-mixed |
| logit_norm_mean | 120 | +0.774 | +0.141 | weak-or-mixed |
| margin_mean | 120 | +0.676 | +0.125 | weak-or-mixed |
| metric_batch_acc | 120 | +0.758 | +0.533 | survives |
| metric_batch_loss | 120 | -0.833 | -0.648 | survives |
| per_sample_grad_norm_mean | 120 | -0.512 | -0.272 | survives |
| per_sample_grad_norm_std | 120 | -0.238 | -0.207 | survives |
| random_metric | 120 | -0.066 | +0.038 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.803 | +0.233 | survives |
| sam_sharpness | 120 | -0.357 | -0.187 | weak-or-mixed |
| train_acc | 120 | +0.970 | +0.936 | survives |
| train_loss | 120 | -0.974 | -0.920 | survives |
| update_to_weight_ratio | 120 | +0.785 | +0.191 | weak-or-mixed |
| val_loss | 120 | -0.899 | -0.889 | survives |
| weight_l1 | 120 | +0.765 | +0.212 | survives |
| weight_l2 | 120 | +0.772 | +0.101 | weak-or-mixed |
| weight_linf | 120 | +0.780 | +0.180 | weak-or-mixed |
| weight_rms | 120 | +0.772 | +0.101 | weak-or-mixed |

## arch=resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 120 | -0.411 | -0.349 | survives |
| brier | 120 | -0.454 | -0.341 | survives |
| confidence_mean | 120 | +0.485 | +0.317 | survives |
| distance_from_init_l2 | 120 | +0.796 | +0.419 | survives |
| ece | 120 | -0.463 | -0.319 | survives |
| entropy_mean | 120 | -0.513 | -0.331 | survives |
| feature_cosine_mean | 120 | +0.171 | +0.283 | hidden-after-control |
| feature_erank | 120 | +0.382 | +0.158 | weak-or-mixed |
| feature_erank_norm | 120 | +0.382 | +0.158 | weak-or-mixed |
| feature_norm_mean | 120 | -0.038 | +0.096 | weak-or-mixed |
| fim_erank | 120 | -0.512 | -0.179 | weak-or-mixed |
| fim_norm | 120 | -0.512 | -0.179 | weak-or-mixed |
| fisher_condition | 120 | +0.529 | +0.084 | washout |
| fisher_entropy | 120 | -0.512 | -0.179 | weak-or-mixed |
| fisher_spectral | 120 | -0.552 | -0.173 | weak-or-mixed |
| fisher_stable_rank | 120 | -0.447 | -0.146 | weak-or-mixed |
| fisher_trace | 120 | -0.619 | -0.247 | survives |
| grad_l1 | 120 | -0.618 | -0.269 | survives |
| grad_linf | 120 | -0.507 | -0.189 | weak-or-mixed |
| grad_mean_abs | 120 | -0.618 | -0.269 | survives |
| grad_noise_scale | 120 | +0.115 | +0.122 | weak-or-mixed |
| grad_norm | 120 | -0.610 | -0.261 | survives |
| hessian_top_eig_power | 40 | -0.625 | -0.253 | survives |
| hessian_trace_hutchinson | 40 | -0.643 | -0.155 | weak-or-mixed |
| logit_norm_mean | 120 | +0.696 | +0.367 | survives |
| margin_mean | 120 | +0.481 | +0.323 | survives |
| metric_batch_acc | 120 | +0.428 | +0.274 | survives |
| metric_batch_loss | 120 | -0.467 | -0.345 | survives |
| per_sample_grad_norm_mean | 120 | -0.669 | -0.314 | survives |
| per_sample_grad_norm_std | 120 | -0.549 | -0.178 | weak-or-mixed |
| random_metric | 120 | -0.086 | +0.075 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.796 | +0.419 | survives |
| sam_sharpness | 120 | -0.684 | -0.226 | survives |
| train_acc | 120 | +0.500 | +0.437 | survives |
| train_loss | 120 | -0.519 | -0.458 | survives |
| update_to_weight_ratio | 120 | +0.777 | +0.280 | survives |
| val_loss | 120 | -0.334 | -0.646 | survives |
| weight_l1 | 120 | +0.741 | +0.452 | survives |
| weight_l2 | 120 | +0.656 | +0.322 | survives |
| weight_linf | 120 | +0.627 | +0.262 | survives |
| weight_rms | 120 | +0.656 | +0.322 | survives |

## arch=vit

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 120 | -0.168 | +0.044 | weak-or-mixed |
| brier | 120 | -0.452 | -0.388 | survives |
| confidence_mean | 120 | +0.527 | +0.490 | survives |
| distance_from_init_l2 | 120 | +0.505 | +0.220 | survives |
| ece | 120 | -0.199 | -0.118 | weak-or-mixed |
| entropy_mean | 120 | -0.513 | -0.483 | survives |
| feature_cosine_mean | 120 | -0.112 | -0.364 | hidden-after-control |
| feature_erank | 120 | -0.118 | +0.403 | hidden-after-control |
| feature_erank_norm | 120 | -0.118 | +0.403 | hidden-after-control |
| feature_norm_mean | 120 | +0.175 | +0.344 | hidden-after-control |
| fim_erank | 120 | -0.407 | -0.263 | survives |
| fim_norm | 120 | -0.407 | -0.263 | survives |
| fisher_condition | 120 | +0.438 | +0.313 | survives |
| fisher_entropy | 120 | -0.407 | -0.263 | survives |
| fisher_spectral | 120 | -0.091 | +0.218 | hidden-after-control |
| fisher_stable_rank | 120 | -0.337 | -0.190 | weak-or-mixed |
| fisher_trace | 120 | -0.261 | +0.064 | washout |
| grad_l1 | 120 | -0.283 | +0.156 | weak-or-mixed |
| grad_linf | 120 | -0.246 | -0.244 | survives |
| grad_mean_abs | 120 | -0.283 | +0.156 | weak-or-mixed |
| grad_noise_scale | 120 | +0.027 | -0.019 | weak-or-mixed |
| grad_norm | 120 | -0.257 | +0.064 | washout |
| logit_norm_mean | 120 | +0.351 | +0.364 | survives |
| margin_mean | 120 | +0.528 | +0.501 | survives |
| metric_batch_acc | 120 | +0.428 | +0.366 | survives |
| metric_batch_loss | 120 | -0.465 | -0.394 | survives |
| per_sample_grad_norm_mean | 120 | -0.379 | -0.087 | washout |
| per_sample_grad_norm_std | 120 | -0.048 | +0.285 | hidden-after-control |
| random_metric | 120 | +0.021 | +0.032 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.507 | +0.223 | survives |
| sam_sharpness | 120 | -0.241 | +0.132 | weak-or-mixed |
| train_acc | 120 | +0.549 | +0.610 | survives |
| train_loss | 120 | -0.544 | -0.599 | survives |
| update_to_weight_ratio | 120 | +0.483 | +0.149 | weak-or-mixed |
| val_loss | 120 | -0.397 | -0.405 | survives |
| weight_l1 | 120 | +0.385 | +0.002 | washout |
| weight_l2 | 120 | +0.379 | -0.016 | washout |
| weight_linf | 120 | +0.383 | +0.052 | washout |
| weight_rms | 120 | +0.379 | -0.016 | washout |

## arch=wide_resnet

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 120 | -0.682 | -0.499 | survives |
| brier | 120 | -0.490 | -0.542 | survives |
| confidence_mean | 120 | +0.488 | +0.523 | survives |
| distance_from_init_l2 | 120 | +0.719 | +0.096 | washout |
| ece | 120 | -0.491 | -0.535 | survives |
| entropy_mean | 120 | -0.507 | -0.541 | survives |
| feature_cosine_mean | 120 | +0.176 | +0.214 | hidden-after-control |
| feature_erank | 120 | +0.308 | +0.226 | survives |
| feature_erank_norm | 120 | +0.308 | +0.226 | survives |
| feature_norm_mean | 120 | +0.054 | +0.306 | hidden-after-control |
| fim_erank | 120 | -0.390 | -0.078 | washout |
| fim_norm | 120 | -0.390 | -0.078 | washout |
| fisher_condition | 120 | +0.387 | -0.015 | washout |
| fisher_entropy | 120 | -0.390 | -0.078 | washout |
| fisher_spectral | 120 | -0.673 | -0.533 | survives |
| fisher_stable_rank | 120 | -0.333 | -0.070 | washout |
| fisher_trace | 120 | -0.701 | -0.579 | survives |
| grad_l1 | 120 | -0.702 | -0.570 | survives |
| grad_linf | 120 | -0.568 | -0.535 | survives |
| grad_mean_abs | 120 | -0.702 | -0.570 | survives |
| grad_noise_scale | 120 | +0.148 | +0.103 | weak-or-mixed |
| grad_norm | 120 | -0.703 | -0.575 | survives |
| hessian_top_eig_power | 40 | -0.770 | -0.568 | survives |
| hessian_trace_hutchinson | 40 | -0.598 | -0.370 | survives |
| logit_norm_mean | 120 | +0.763 | +0.480 | survives |
| margin_mean | 120 | +0.487 | +0.518 | survives |
| metric_batch_acc | 120 | +0.490 | +0.377 | survives |
| metric_batch_loss | 120 | -0.510 | -0.558 | survives |
| per_sample_grad_norm_mean | 120 | -0.714 | -0.608 | survives |
| per_sample_grad_norm_std | 120 | -0.672 | -0.534 | survives |
| random_metric | 120 | -0.136 | -0.165 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.719 | +0.096 | washout |
| sam_sharpness | 120 | -0.773 | -0.423 | survives |
| train_acc | 120 | +0.352 | +0.513 | survives |
| train_loss | 120 | -0.451 | -0.578 | survives |
| update_to_weight_ratio | 120 | +0.665 | -0.067 | washout |
| val_loss | 120 | -0.461 | -0.685 | survives |
| weight_l1 | 120 | +0.737 | +0.450 | survives |
| weight_l2 | 120 | +0.660 | +0.360 | survives |
| weight_linf | 120 | +0.649 | +0.307 | survives |
| weight_rms | 120 | +0.660 | +0.360 | survives |
