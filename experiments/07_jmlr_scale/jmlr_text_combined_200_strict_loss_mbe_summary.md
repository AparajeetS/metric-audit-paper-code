# JMLR-Scale Metric Audit

- summary csv: `experiments\07_jmlr_scale\jmlr_text_combined_200_strict_loss_mbe_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed, val_loss`

## pooled

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
