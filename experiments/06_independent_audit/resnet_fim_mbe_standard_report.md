# ResNet FIM_norm MBE Smoke Test

- csv: `C:\Research\cei\metric-audit-paper-code\experiments\06_independent_audit\resnet_fim_mbe_standard.csv`
- rows: `18`
- model: compact CIFAR ResNet with BatchNorm, trained on CPU
- MBE control covariates: rank(`lr`), rank(`wd`)

| metric | raw Spearman vs final_acc | partial rank, lr+wd | partial rank, lr+wd+seed |
|---|---:|---:|---:|
| fim_norm | -0.146 | +0.418 | +0.368 |
| val_loss | -0.850 | -0.797 | -0.654 |
| train_acc | +0.768 | +0.683 | +0.693 |
| train_loss | -0.804 | -0.742 | -0.662 |

Interpretation guardrail: this is a CPU smoke test for direction and plumbing, not a publishable-scale ResNet result.
