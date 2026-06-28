from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


DEFAULT_METRICS = [
    "fim_norm",
    "fim_erank",
    "fisher_trace",
    "fisher_spectral",
    "fisher_stable_rank",
    "fisher_entropy",
    "fisher_condition",
    "grad_noise_scale",
    "grad_norm",
    "grad_l1",
    "grad_linf",
    "grad_mean_abs",
    "per_sample_grad_norm_mean",
    "per_sample_grad_norm_std",
    "sam_sharpness",
    "asam_sharpness",
    "hessian_trace_hutchinson",
    "hessian_top_eig_power",
    "weight_l2",
    "weight_l1",
    "weight_linf",
    "weight_rms",
    "distance_from_init_l2",
    "relative_distance_from_init",
    "update_to_weight_ratio",
    "confidence_mean",
    "entropy_mean",
    "margin_mean",
    "brier",
    "ece",
    "logit_norm_mean",
    "metric_batch_acc",
    "metric_batch_loss",
    "feature_erank",
    "feature_erank_norm",
    "feature_norm_mean",
    "feature_cosine_mean",
    "train_loss",
    "train_acc",
    "val_loss",
    "random_metric",
]


def rank_values(series: pd.Series) -> np.ndarray:
    return series.rank(method="average").to_numpy(dtype=float)


def pearson(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) < 3:
        return math.nan
    if np.nanstd(a) <= 0 or np.nanstd(b) <= 0:
        return math.nan
    return float(np.corrcoef(a, b)[0, 1])


def spearman(df: pd.DataFrame, metric: str, target: str) -> float:
    clean = df[[metric, target]].replace([np.inf, -np.inf], np.nan).dropna()
    return pearson(rank_values(clean[metric]), rank_values(clean[target]))


def design_matrix(df: pd.DataFrame, covars: list[str]) -> np.ndarray:
    blocks = [np.ones(len(df))]
    for covar in covars:
        if covar not in df.columns:
            continue
        series = df[covar]
        if not is_numeric_dtype(series):
            dummies = pd.get_dummies(series.astype(str), prefix=covar, drop_first=True)
            for col in dummies.columns:
                blocks.append(dummies[col].to_numpy(dtype=float))
        else:
            blocks.append(rank_values(series.astype(float)))
    return np.column_stack(blocks)


def partial_rank(df: pd.DataFrame, metric: str, target: str, covars: list[str]) -> float:
    cols = list(dict.fromkeys([metric, target, *[c for c in covars if c in df.columns]]))
    clean = df[cols].replace([np.inf, -np.inf], np.nan).dropna()
    if len(clean) < 5:
        return math.nan
    x = rank_values(clean[metric])
    y = rank_values(clean[target])
    X = design_matrix(clean, covars)
    try:
        bx = np.linalg.lstsq(X, x, rcond=None)[0]
        by = np.linalg.lstsq(X, y, rcond=None)[0]
    except np.linalg.LinAlgError:
        return math.nan
    return pearson(x - X @ bx, y - X @ by)


def classify(raw: float, partial: float) -> str:
    if np.isnan(raw) or np.isnan(partial):
        return "insufficient"
    if abs(partial) < 0.10 and abs(raw) >= 0.20:
        return "washout"
    if raw <= -0.20 and partial >= 0.20:
        return "sign-inversion"
    if raw >= 0.20 and partial <= -0.20:
        return "reverse-inversion"
    if abs(raw) < 0.20 and abs(partial) >= 0.20:
        return "hidden-after-control"
    if np.sign(raw) == np.sign(partial) and abs(partial) >= 0.20:
        return "survives"
    return "weak-or-mixed"


def load_inputs(paths: list[Path]) -> pd.DataFrame:
    frames = []
    for path in paths:
        if path.is_dir():
            for csv_path in sorted(path.glob("*.csv")):
                frame = pd.read_csv(csv_path)
                frame["source_csv"] = str(csv_path)
                frames.append(frame)
        else:
            frame = pd.read_csv(path)
            frame["source_csv"] = str(path)
            frames.append(frame)
    if not frames:
        raise SystemExit("No CSV inputs found.")
    df = pd.concat(frames, ignore_index=True, sort=False)
    if "error" in df.columns:
        df = df[df["error"].isna() | (df["error"].astype(str) == "")]
    return df


def summarize_group(df: pd.DataFrame, group_name: str, covars: list[str], target: str) -> list[dict]:
    rows = []
    for metric in DEFAULT_METRICS:
        if metric not in df.columns or target not in df.columns:
            continue
        if metric in covars or metric == target:
            continue
        cols = list(dict.fromkeys([metric, target, *[c for c in covars if c in df.columns]]))
        clean = df[cols].replace([np.inf, -np.inf], np.nan).dropna()
        if len(clean) < 8:
            continue
        raw = spearman(clean, metric, target)
        part = partial_rank(clean, metric, target, covars)
        rows.append(
            {
                "group": group_name,
                "n": len(clean),
                "metric": metric,
                "raw_spearman": raw,
                "mbe_partial": part,
                "delta_partial_minus_raw": part - raw if not np.isnan(raw) and not np.isnan(part) else math.nan,
                "classification": classify(raw, part),
            }
        )
    return rows


def render_markdown(summary: pd.DataFrame, out_csv: Path, covars: list[str]) -> str:
    lines = [
        "# JMLR-Scale Metric Audit",
        "",
        f"- summary csv: `{out_csv}`",
        f"- MBE covariates: `{', '.join(covars)}`",
        "",
    ]
    if summary.empty:
        lines.extend(
            [
                "No metric summaries were produced. This usually means the input CSV has fewer than eight completed rows per group.",
                "",
            ]
        )
        return "\n".join(lines)
    for group, group_df in summary.groupby("group", sort=False):
        lines.append(f"## {group}")
        lines.append("")
        lines.append("| metric | n | raw rho | MBE partial rho | class |")
        lines.append("|---|---:|---:|---:|---|")
        for _, row in group_df.sort_values("metric").iterrows():
            lines.append(
                f"| {row['metric']} | {int(row['n'])} | {row['raw_spearman']:+.3f} | "
                f"{row['mbe_partial']:+.3f} | {row['classification']} |"
            )
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze JMLR-scale MBE metric CSV shards.")
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--target", default="final_acc")
    parser.add_argument(
        "--covars",
        default="lr,wd,dropout,optimizer,arch,task,seed",
        help="Comma-separated MBE covariates. Categorical covariates are one-hot encoded.",
    )
    parser.add_argument("--out-prefix", default="jmlr_scale_audit")
    args = parser.parse_args()

    covars = [c.strip() for c in args.covars.split(",") if c.strip()]
    df = load_inputs(args.inputs)
    rows = summarize_group(df, "pooled", covars, args.target)
    if "suite" in df.columns:
        for suite, g in df.groupby("suite"):
            rows.extend(summarize_group(g, f"suite={suite}", covars, args.target))
    if "arch" in df.columns:
        within_covars = [c for c in covars if c != "arch"]
        for arch, g in df.groupby("arch"):
            rows.extend(summarize_group(g, f"arch={arch}", within_covars, args.target))

    summary = pd.DataFrame(rows)
    if summary.empty:
        summary = pd.DataFrame(
            columns=[
                "group",
                "n",
                "metric",
                "raw_spearman",
                "mbe_partial",
                "delta_partial_minus_raw",
                "classification",
            ]
        )
    out_csv = Path(f"{args.out_prefix}_summary.csv")
    out_md = Path(f"{args.out_prefix}_summary.md")
    summary.to_csv(out_csv, index=False)
    out_md.write_text(render_markdown(summary, out_csv, covars), encoding="utf-8")
    print(out_md.read_text(encoding="utf-8"))
    print(f"Saved {out_csv}")
    print(f"Saved {out_md}")


if __name__ == "__main__":
    main()
