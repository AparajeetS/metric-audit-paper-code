from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


METRICS = [
    "fim_norm",
    "fim_erank",
    "sam_sharpness",
    "asam_sharpness",
    "fisher_trace",
    "fisher_spectral",
    "fisher_stable_rank",
    "grad_norm",
    "grad_l1",
    "grad_linf",
    "grad_noise_scale",
    "feature_erank",
    "feature_erank_norm",
    "feature_cosine_mean",
    "feature_norm_mean",
    "val_loss",
    "train_loss",
    "metric_batch_loss",
    "random_metric",
]

CONTROL_SETS = {
    "lr_wd": ["lr", "wd"],
    "lr_wd_dropout": ["lr", "wd", "dropout"],
    "train_hparams": ["lr", "wd", "dropout", "optimizer"],
    "arch_task": ["lr", "wd", "dropout", "optimizer", "arch", "task"],
    "full": ["lr", "wd", "dropout", "optimizer", "arch", "task", "seed"],
}


def rank_values(series: pd.Series) -> np.ndarray:
    return series.rank(method="average").to_numpy(dtype=float)


def pearson(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) < 5 or np.nanstd(a) == 0 or np.nanstd(b) == 0:
        return math.nan
    return float(np.corrcoef(a, b)[0, 1])


def design(df: pd.DataFrame, covars: list[str]) -> np.ndarray:
    cols = [np.ones(len(df))]
    for covar in covars:
        if covar not in df.columns:
            continue
        s = df[covar]
        if is_numeric_dtype(s):
            cols.append(rank_values(s.astype(float)))
        else:
            dummies = pd.get_dummies(s.astype(str), drop_first=True)
            for col in dummies.columns:
                cols.append(dummies[col].to_numpy(dtype=float))
    return np.column_stack(cols)


def partial_rank(df: pd.DataFrame, metric: str, target: str, covars: list[str]) -> float:
    cols = [metric, target, *[c for c in covars if c in df.columns]]
    clean = df[cols].replace([np.inf, -np.inf], np.nan).dropna()
    if len(clean) < 8:
        return math.nan
    x = rank_values(clean[metric])
    y = rank_values(clean[target])
    X = design(clean, covars)
    try:
        bx = np.linalg.lstsq(X, x, rcond=None)[0]
        by = np.linalg.lstsq(X, y, rcond=None)[0]
    except np.linalg.LinAlgError:
        return math.nan
    return pearson(x - X @ bx, y - X @ by)


def raw_spearman(df: pd.DataFrame, metric: str, target: str) -> float:
    clean = df[[metric, target]].replace([np.inf, -np.inf], np.nan).dropna()
    if len(clean) < 8:
        return math.nan
    return pearson(rank_values(clean[metric]), rank_values(clean[target]))


def ci(vals: list[float]) -> tuple[float, float]:
    arr = np.asarray([v for v in vals if not np.isnan(v)], dtype=float)
    if len(arr) == 0:
        return math.nan, math.nan
    return float(np.quantile(arr, 0.025)), float(np.quantile(arr, 0.975))


def summarize(df: pd.DataFrame, group: str, target: str, n_boot: int, rng: np.random.Generator) -> list[dict]:
    rows = []
    metrics = [m for m in METRICS if m in df.columns]
    for metric in metrics:
        base = df[[metric, target, *[c for covars in CONTROL_SETS.values() for c in covars if c in df.columns]]]
        base = base.replace([np.inf, -np.inf], np.nan).dropna(subset=[metric, target])
        if len(base) < 20:
            continue
        raw = raw_spearman(base, metric, target)
        for control_name, covars in CONTROL_SETS.items():
            part = partial_rank(base, metric, target, covars)
            raw_bs, part_bs, delta_bs = [], [], []
            idx = np.arange(len(base))
            for _ in range(n_boot):
                sample = base.iloc[rng.choice(idx, size=len(idx), replace=True)]
                r = raw_spearman(sample, metric, target)
                p = partial_rank(sample, metric, target, covars)
                raw_bs.append(r)
                part_bs.append(p)
                delta_bs.append(p - r if not np.isnan(p) and not np.isnan(r) else math.nan)
            raw_lo, raw_hi = ci(raw_bs)
            part_lo, part_hi = ci(part_bs)
            delta_lo, delta_hi = ci(delta_bs)
            rows.append(
                {
                    "group": group,
                    "target": target,
                    "metric": metric,
                    "control_set": control_name,
                    "n": len(base),
                    "raw": raw,
                    "partial": part,
                    "delta": part - raw if not np.isnan(part) and not np.isnan(raw) else math.nan,
                    "raw_ci_lo": raw_lo,
                    "raw_ci_hi": raw_hi,
                    "partial_ci_lo": part_lo,
                    "partial_ci_hi": part_hi,
                    "delta_ci_lo": delta_lo,
                    "delta_ci_hi": delta_hi,
                }
            )
    return rows


def load_inputs(paths: list[Path]) -> pd.DataFrame:
    frames = []
    for path in paths:
        frames.append(pd.read_csv(path))
    return pd.concat(frames, ignore_index=True, sort=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Bootstrap MBE confidence intervals and control-set ablations.")
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--targets", default="final_acc,val_loss")
    parser.add_argument("--n-boot", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260627)
    parser.add_argument("--out", default="jmlr_bootstrap_mbe.csv")
    args = parser.parse_args()

    df = load_inputs(args.inputs)
    if "error" in df.columns:
        df = df[df["error"].isna() | (df["error"].astype(str) == "")]
    rng = np.random.default_rng(args.seed)
    rows = []
    targets = [t.strip() for t in args.targets.split(",") if t.strip()]
    for target in targets:
        if target not in df.columns:
            continue
        rows.extend(summarize(df, "pooled", target, args.n_boot, rng))
        if "suite" in df.columns:
            for suite, g in df.groupby("suite"):
                rows.extend(summarize(g, f"suite={suite}", target, args.n_boot, rng))
        if "arch" in df.columns:
            for arch, g in df.groupby("arch"):
                rows.extend(summarize(g, f"arch={arch}", target, args.n_boot, rng))
    out = pd.DataFrame(rows)
    out.to_csv(args.out, index=False)
    print(f"saved {args.out} rows={len(out)}")
    focus = out[(out["control_set"] == "full") & out["metric"].isin(["fim_norm", "sam_sharpness", "feature_erank", "val_loss", "random_metric"])]
    if not focus.empty:
        print(focus[["group", "target", "metric", "n", "raw", "partial", "partial_ci_lo", "partial_ci_hi", "delta_ci_lo", "delta_ci_hi"]].to_string(index=False))


if __name__ == "__main__":
    main()
