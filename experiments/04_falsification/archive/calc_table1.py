import pandas as pd
import pingouin as pg
df = pd.read_csv('experiments/04_falsification/out/large_grid_v3_asam.csv')
mbe_sam = pg.partial_corr(data=df, x='sam_sharpness', y='final_acc', covar=['lr', 'wd'], method='spearman')
mbe_asam = pg.partial_corr(data=df, x='asam_sharpness', y='final_acc', covar=['lr', 'wd'], method='spearman')
print(f"SAM: {mbe_sam['r'].values[0]:+.3f} (p={mbe_sam['p_val'].values[0]:.2e})")
print(f"ASAM: {mbe_asam['r'].values[0]:+.3f} (p={mbe_asam['p_val'].values[0]:.2e})")
