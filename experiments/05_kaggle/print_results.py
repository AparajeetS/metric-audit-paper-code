import pandas as pd
import pingouin as pg

df = pd.read_csv('kaggle_cifar10_results.csv')
metrics = ['fim_norm', 'sam_sharpness', 'fisher_trace', 'grad_norm', 'weight_norm']

print("=== CIFAR-10 Kaggle Results (CNN w/ BatchNorm) ===")
print("=== ABSOLUTE CORRELATIONS ===")
for m in metrics:
    rho = pg.corr(df[m], df['final_acc'], method='spearman')
    print(f"  {m:>16}: r = {rho['r'].values[0]:+.3f} (p = {rho['p_val'].values[0]:.2e})")

print("\n=== MBE PARTIAL CORRELATIONS (Controlling for LR, WD) ===")
for m in metrics:
    mbe = pg.partial_corr(data=df, x=m, y='final_acc', covar=['lr', 'wd'], method='spearman')
    print(f"  {m:>16}: partial r = {mbe['r'].values[0]:+.3f} (p = {mbe['p_val'].values[0]:.2e})")
