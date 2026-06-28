import pandas as pd
import pingouin as pg

df = pd.read_csv('experiments/04_falsification/out/large_grid_v3_asam.csv')
metrics = ['fim_norm', 'sam_sharpness', 'asam_sharpness', 'fisher_trace', 'grad_norm', 'weight_norm']

print('--- ABSOLUTE ---')
for b in ['val_loss', 'train_loss'] + metrics:
    r = pg.corr(df[b], df['final_acc'], method='spearman')
    print(f"{b}: {r['r'].values[0]:+.3f} (p={r['p_val'].values[0]:.2e})")

print('\n--- PARTIAL (VAL LOSS) ---')
for m in metrics:
    r = pg.partial_corr(data=df, x=m, y='final_acc', covar='val_loss', method='spearman')
    print(f"{m}: {r['r'].values[0]:+.3f} (p={r['p_val'].values[0]:.2e})")

print('\n--- PARTIAL (TRAIN LOSS) ---')
for m in metrics:
    r = pg.partial_corr(data=df, x=m, y='final_acc', covar='train_loss', method='spearman')
    print(f"{m}: {r['r'].values[0]:+.3f} (p={r['p_val'].values[0]:.2e})")

print('\n--- REVERSE ASYMMETRY ---')
for b in ['val_loss', 'train_loss']:
    for m in ['fim_norm', 'sam_sharpness']:
        r = pg.partial_corr(data=df, x=b, y='final_acc', covar=m, method='spearman')
        print(f"{b} | {m}: {r['r'].values[0]:+.3f} (p={r['p_val'].values[0]:.2e})")
