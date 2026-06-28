# JMLR-Scale Metric Audit

- summary csv: `experiments\07_jmlr_scale\jmlr_text_combined_200_audit_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed`

## pooled

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
