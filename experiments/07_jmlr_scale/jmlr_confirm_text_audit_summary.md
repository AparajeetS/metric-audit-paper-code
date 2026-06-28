# JMLR-Scale Metric Audit

- summary csv: `experiments\07_jmlr_scale\jmlr_confirm_text_audit_summary.csv`
- MBE covariates: `lr, wd, dropout, optimizer, arch, task, seed`

## pooled

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 120 | -0.804 | -0.382 | survives |
| brier | 120 | -0.214 | -0.007 | washout |
| confidence_mean | 120 | +0.294 | +0.106 | weak-or-mixed |
| distance_from_init_l2 | 120 | +0.741 | +0.187 | weak-or-mixed |
| ece | 120 | -0.258 | -0.012 | washout |
| entropy_mean | 120 | -0.342 | -0.141 | weak-or-mixed |
| feature_cosine_mean | 120 | +0.720 | +0.361 | survives |
| feature_erank | 120 | -0.729 | -0.448 | survives |
| feature_erank_norm | 120 | -0.729 | -0.448 | survives |
| feature_norm_mean | 120 | +0.316 | -0.231 | reverse-inversion |
| fim_erank | 120 | -0.270 | -0.015 | washout |
| fim_norm | 120 | -0.270 | -0.015 | washout |
| fisher_condition | 120 | +0.628 | +0.293 | survives |
| fisher_entropy | 120 | -0.270 | -0.015 | washout |
| fisher_spectral | 120 | -0.795 | -0.353 | survives |
| fisher_stable_rank | 120 | -0.063 | +0.115 | weak-or-mixed |
| fisher_trace | 120 | -0.812 | -0.410 | survives |
| grad_l1 | 120 | -0.816 | -0.423 | survives |
| grad_linf | 120 | -0.146 | +0.222 | hidden-after-control |
| grad_mean_abs | 120 | -0.816 | -0.423 | survives |
| grad_noise_scale | 120 | -0.145 | -0.073 | weak-or-mixed |
| grad_norm | 120 | -0.813 | -0.418 | survives |
| logit_norm_mean | 120 | +0.745 | -0.029 | washout |
| margin_mean | 120 | +0.305 | +0.083 | washout |
| metric_batch_acc | 120 | +0.196 | -0.031 | weak-or-mixed |
| metric_batch_loss | 120 | -0.231 | -0.092 | washout |
| per_sample_grad_norm_mean | 120 | -0.794 | -0.376 | survives |
| per_sample_grad_norm_std | 120 | -0.727 | -0.242 | survives |
| random_metric | 120 | +0.055 | +0.033 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.743 | +0.192 | weak-or-mixed |
| sam_sharpness | 120 | -0.811 | -0.400 | survives |
| train_acc | 120 | +0.212 | +0.112 | weak-or-mixed |
| train_loss | 120 | -0.267 | -0.132 | weak-or-mixed |
| update_to_weight_ratio | 120 | +0.741 | +0.149 | weak-or-mixed |
| val_loss | 120 | -0.925 | -0.852 | survives |
| weight_l1 | 120 | +0.707 | +0.172 | weak-or-mixed |
| weight_l2 | 120 | +0.710 | +0.064 | washout |
| weight_linf | 120 | +0.210 | -0.128 | weak-or-mixed |
| weight_rms | 120 | +0.710 | +0.062 | washout |

## suite=text

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 120 | -0.804 | -0.382 | survives |
| brier | 120 | -0.214 | -0.007 | washout |
| confidence_mean | 120 | +0.294 | +0.106 | weak-or-mixed |
| distance_from_init_l2 | 120 | +0.741 | +0.187 | weak-or-mixed |
| ece | 120 | -0.258 | -0.012 | washout |
| entropy_mean | 120 | -0.342 | -0.141 | weak-or-mixed |
| feature_cosine_mean | 120 | +0.720 | +0.361 | survives |
| feature_erank | 120 | -0.729 | -0.448 | survives |
| feature_erank_norm | 120 | -0.729 | -0.448 | survives |
| feature_norm_mean | 120 | +0.316 | -0.231 | reverse-inversion |
| fim_erank | 120 | -0.270 | -0.015 | washout |
| fim_norm | 120 | -0.270 | -0.015 | washout |
| fisher_condition | 120 | +0.628 | +0.293 | survives |
| fisher_entropy | 120 | -0.270 | -0.015 | washout |
| fisher_spectral | 120 | -0.795 | -0.353 | survives |
| fisher_stable_rank | 120 | -0.063 | +0.115 | weak-or-mixed |
| fisher_trace | 120 | -0.812 | -0.410 | survives |
| grad_l1 | 120 | -0.816 | -0.423 | survives |
| grad_linf | 120 | -0.146 | +0.222 | hidden-after-control |
| grad_mean_abs | 120 | -0.816 | -0.423 | survives |
| grad_noise_scale | 120 | -0.145 | -0.073 | weak-or-mixed |
| grad_norm | 120 | -0.813 | -0.418 | survives |
| logit_norm_mean | 120 | +0.745 | -0.029 | washout |
| margin_mean | 120 | +0.305 | +0.083 | washout |
| metric_batch_acc | 120 | +0.196 | -0.031 | weak-or-mixed |
| metric_batch_loss | 120 | -0.231 | -0.092 | washout |
| per_sample_grad_norm_mean | 120 | -0.794 | -0.376 | survives |
| per_sample_grad_norm_std | 120 | -0.727 | -0.242 | survives |
| random_metric | 120 | +0.055 | +0.033 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.743 | +0.192 | weak-or-mixed |
| sam_sharpness | 120 | -0.811 | -0.400 | survives |
| train_acc | 120 | +0.212 | +0.112 | weak-or-mixed |
| train_loss | 120 | -0.267 | -0.132 | weak-or-mixed |
| update_to_weight_ratio | 120 | +0.741 | +0.149 | weak-or-mixed |
| val_loss | 120 | -0.925 | -0.852 | survives |
| weight_l1 | 120 | +0.707 | +0.172 | weak-or-mixed |
| weight_l2 | 120 | +0.710 | +0.064 | washout |
| weight_linf | 120 | +0.210 | -0.128 | weak-or-mixed |
| weight_rms | 120 | +0.710 | +0.062 | washout |

## arch=char_transformer

| metric | n | raw rho | MBE partial rho | class |
|---|---:|---:|---:|---|
| asam_sharpness | 120 | -0.804 | -0.382 | survives |
| brier | 120 | -0.214 | -0.007 | washout |
| confidence_mean | 120 | +0.294 | +0.106 | weak-or-mixed |
| distance_from_init_l2 | 120 | +0.741 | +0.187 | weak-or-mixed |
| ece | 120 | -0.258 | -0.012 | washout |
| entropy_mean | 120 | -0.342 | -0.141 | weak-or-mixed |
| feature_cosine_mean | 120 | +0.720 | +0.361 | survives |
| feature_erank | 120 | -0.729 | -0.448 | survives |
| feature_erank_norm | 120 | -0.729 | -0.448 | survives |
| feature_norm_mean | 120 | +0.316 | -0.231 | reverse-inversion |
| fim_erank | 120 | -0.270 | -0.015 | washout |
| fim_norm | 120 | -0.270 | -0.015 | washout |
| fisher_condition | 120 | +0.628 | +0.293 | survives |
| fisher_entropy | 120 | -0.270 | -0.015 | washout |
| fisher_spectral | 120 | -0.795 | -0.353 | survives |
| fisher_stable_rank | 120 | -0.063 | +0.115 | weak-or-mixed |
| fisher_trace | 120 | -0.812 | -0.410 | survives |
| grad_l1 | 120 | -0.816 | -0.423 | survives |
| grad_linf | 120 | -0.146 | +0.222 | hidden-after-control |
| grad_mean_abs | 120 | -0.816 | -0.423 | survives |
| grad_noise_scale | 120 | -0.145 | -0.073 | weak-or-mixed |
| grad_norm | 120 | -0.813 | -0.418 | survives |
| logit_norm_mean | 120 | +0.745 | -0.029 | washout |
| margin_mean | 120 | +0.305 | +0.083 | washout |
| metric_batch_acc | 120 | +0.196 | -0.031 | weak-or-mixed |
| metric_batch_loss | 120 | -0.231 | -0.092 | washout |
| per_sample_grad_norm_mean | 120 | -0.794 | -0.376 | survives |
| per_sample_grad_norm_std | 120 | -0.727 | -0.242 | survives |
| random_metric | 120 | +0.055 | +0.033 | weak-or-mixed |
| relative_distance_from_init | 120 | +0.743 | +0.192 | weak-or-mixed |
| sam_sharpness | 120 | -0.811 | -0.400 | survives |
| train_acc | 120 | +0.212 | +0.112 | weak-or-mixed |
| train_loss | 120 | -0.267 | -0.132 | weak-or-mixed |
| update_to_weight_ratio | 120 | +0.741 | +0.149 | weak-or-mixed |
| val_loss | 120 | -0.925 | -0.852 | survives |
| weight_l1 | 120 | +0.707 | +0.172 | weak-or-mixed |
| weight_l2 | 120 | +0.710 | +0.064 | washout |
| weight_linf | 120 | +0.210 | -0.128 | weak-or-mixed |
| weight_rms | 120 | +0.710 | +0.062 | washout |
