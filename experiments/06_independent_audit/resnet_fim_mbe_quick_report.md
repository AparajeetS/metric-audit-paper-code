# ResNet FIM_norm MBE Smoke Test

- csv: `C:\Research\cei\metric-audit-paper-code\experiments\06_independent_audit\resnet_fim_mbe_quick.csv`
- rows: `8`
- model: compact CIFAR ResNet with BatchNorm, trained on CPU
- MBE control covariates: rank(`lr`), rank(`wd`)

| metric | raw Spearman vs final_acc | partial rank vs final_acc |
|---|---:|---:|
| fim_norm | -0.703 | -0.858 |
| val_loss | -0.788 | -0.880 |
| train_acc | +0.795 | +0.889 |
| train_loss | -0.594 | -0.994 |

Interpretation guardrail: this is a CPU smoke test for direction and plumbing, not a publishable-scale ResNet result.
