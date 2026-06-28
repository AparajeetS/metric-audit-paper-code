import pandas as pd
import pingouin as pg

df = pd.read_csv('out/unified_grid.csv')

metrics = ['fim_norm','sam_sharpness','asam_sharpness','fisher_trace','grad_norm','weight_norm']

print("=== TABLE 1: MBE Partial Correlation (controlling for LR, WD) ===")
for m in metrics:
    mbe = pg.partial_corr(data=df, x=m, y='final_acc', covar=['lr', 'wd'], method='spearman')
    print(f"  {m:>16}: partial r = {mbe['r'].values[0]:+.3f} (p = {mbe['p_val'].values[0]:.2e})")

print()
print("=== ABSOLUTE CORRELATIONS ===")
for m in ['sam_sharpness', 'asam_sharpness']:
    rho = pg.corr(df[m], df['final_acc'], method='spearman')
    print(f"  {m:>16}: r = {rho['r'].values[0]:+.3f} (p = {rho['p_val'].values[0]:.2e})")

print()
print("=== M-BIAS CHECK (Conditioning on Train Loss) ===")
for m in metrics:
    mbe_mbias = pg.partial_corr(data=df, x=m, y='final_acc', covar='train_loss', method='spearman')
    print(f"  {m:>16}: partial r = {mbe_mbias['r'].values[0]:+.3f} (p = {mbe_mbias['p_val'].values[0]:.2e})")

print()
print("=== TABLE 2: Temporal Ablation (controlling for LR, WD) ===")
for ep in [5, 10, 20, 50]:
    mbe_sam = pg.partial_corr(data=df, x=f'sam_sharpness_ep{ep}', y='final_acc', covar=['lr', 'wd'], method='spearman')
    mbe_asam = pg.partial_corr(data=df, x=f'asam_sharpness_ep{ep}', y='final_acc', covar=['lr', 'wd'], method='spearman')
    print(f"  Epoch {ep:>2} SAM : r = {mbe_sam['r'].values[0]:+.3f} (p = {mbe_sam['p_val'].values[0]:.2e})")
    print(f"  Epoch {ep:>2} ASAM: r = {mbe_asam['r'].values[0]:+.3f} (p = {mbe_asam['p_val'].values[0]:.2e})")

print()
print("=== ALIGNMENT CHECK ===")
sam20_t1 = pg.partial_corr(data=df, x='sam_sharpness', y='final_acc', covar=['lr', 'wd'], method='spearman')['r'].values[0]
sam20_t2 = pg.partial_corr(data=df, x='sam_sharpness_ep20', y='final_acc', covar=['lr', 'wd'], method='spearman')['r'].values[0]
print(f"  Table1 SAM (ep20): {sam20_t1:+.6f}")
print(f"  Table2 SAM (ep20): {sam20_t2:+.6f}")
print(f"  MATCH: {sam20_t1 == sam20_t2}")
