# JMLR-Scale Artifacts

This folder contains scripts, summary reports, and compact CSV outputs for the current MBE audit.

Large downloaded datasets and runtime logs are intentionally ignored by git:

- CIFAR-10 archives and extracted batches
- Tiny Shakespeare text copies
- Kaggle log files
- local smoke-run byproducts
- Python caches

## Raw Result CSVs

The four raw result CSVs used for the 680-model confirmed audit are:

| File | Models | SHA256 |
|---|---:|---|
| `kaggle_downloads/image_v2/jmlr_scale_image_results.csv` | 160 | `9ca5f7a23d48461081aeed08da7a62a94485a5dd22edd3dcb0fefaa960c116c6` |
| `kaggle_downloads/confirm_image/jmlr_confirm_image_results.csv` | 320 | `73ee9395e66579018c21c373f207a80f62569cd0141373474c79896cde19b6a2` |
| `kaggle_downloads/text_v2/jmlr_scale_text_results.csv` | 80 | `0820b16ba089316db5dd5becd73ade18e95946b3e6b9d733fe94db876217f919` |
| `kaggle_downloads/confirm_text/jmlr_confirm_text_results.csv` | 120 | `e4d126aa3edb7bdfcbab60778628b3a6263ea42c9ed5e4c9851a128a0a13c837` |

## Main Summaries

- `jmlr_full_confirmed_680_audit_summary.md`
- `jmlr_full_confirmed_680_strict_loss_mbe_summary.md`
- `jmlr_image_combined_480_audit_summary.md`
- `jmlr_image_combined_480_strict_loss_mbe_summary.md`
- `jmlr_text_combined_200_audit_summary.md`
- `jmlr_text_combined_200_strict_loss_mbe_summary.md`

## Regeneration Commands

Default 680-model audit:

```powershell
python experiments\07_jmlr_scale\analyze_jmlr_scale.py `
  experiments\07_jmlr_scale\kaggle_downloads\image_v2\jmlr_scale_image_results.csv `
  experiments\07_jmlr_scale\kaggle_downloads\confirm_image\jmlr_confirm_image_results.csv `
  experiments\07_jmlr_scale\kaggle_downloads\text_v2\jmlr_scale_text_results.csv `
  experiments\07_jmlr_scale\kaggle_downloads\confirm_text\jmlr_confirm_text_results.csv `
  --out-prefix experiments\07_jmlr_scale\jmlr_full_confirmed_680_audit
```

Strict validation-loss control audit:

```powershell
python experiments\07_jmlr_scale\analyze_jmlr_scale.py `
  experiments\07_jmlr_scale\kaggle_downloads\image_v2\jmlr_scale_image_results.csv `
  experiments\07_jmlr_scale\kaggle_downloads\confirm_image\jmlr_confirm_image_results.csv `
  experiments\07_jmlr_scale\kaggle_downloads\text_v2\jmlr_scale_text_results.csv `
  experiments\07_jmlr_scale\kaggle_downloads\confirm_text\jmlr_confirm_text_results.csv `
  --covars lr,wd,dropout,optimizer,arch,task,seed,val_loss `
  --out-prefix experiments\07_jmlr_scale\jmlr_full_confirmed_680_strict_loss_mbe
```
