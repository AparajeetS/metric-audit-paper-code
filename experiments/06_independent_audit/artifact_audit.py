from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse
import json
import math

import numpy as np
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DOWNLOAD = Path(r"C:\Users\apara\Downloads\kaggle_cifar10_results (2).csv")


@dataclass
class DatasetSpec:
    name: str
    path: Path
    family: str
    control_covars: list[str]
    metrics: list[str]
    temporal_metrics: list[str] | None = None


def rank_values(series: pd.Series) -> np.ndarray:
    return series.rank(method="average").to_numpy(dtype=float)


def pearson_corr(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) < 2:
        return math.nan
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    return float(np.corrcoef(a, b)[0, 1])


def spearman_like_corr(df: pd.DataFrame, x: str, y: str) -> float:
    clean = df[[x, y]].dropna()
    return pearson_corr(rank_values(clean[x]), rank_values(clean[y]))


def partial_rank_corr(df: pd.DataFrame, x: str, y: str, covars: list[str]) -> float:
    cols = [x, y, *covars]
    clean = df[cols].dropna()
    if clean.empty:
        return math.nan
    design = [np.ones(len(clean))]
    for covar in covars:
        design.append(rank_values(clean[covar]))
    X = np.column_stack(design)
    rx = rank_values(clean[x]) - X @ np.linalg.lstsq(X, rank_values(clean[x]), rcond=None)[0]
    ry = rank_values(clean[y]) - X @ np.linalg.lstsq(X, rank_values(clean[y]), rcond=None)[0]
    return pearson_corr(rx, ry)


def classify_narrative(abs_r: float, part_r: float) -> str:
    if np.isnan(abs_r) or np.isnan(part_r):
        return "insufficient-data"
    if abs(part_r) < 0.10:
        return "washout-after-control"
    if abs_r < -0.20 and part_r > 0.20:
        return "sign-inversion"
    if abs_r > 0.20 and part_r < -0.20:
        return "reverse-inversion"
    if abs_r < -0.20 and part_r < -0.20:
        return "negative-signal-survives"
    if abs_r > 0.20 and part_r > 0.20:
        return "positive-signal-survives"
    return "weak-or-mixed"


def dataset_specs(extra_csv: Path | None) -> list[DatasetSpec]:
    specs = [
        DatasetSpec(
            name="mlp_large_grid_v3_asam",
            path=REPO_ROOT / "experiments" / "04_falsification" / "out" / "large_grid_v3_asam.csv",
            family="mlp",
            control_covars=["lr", "wd"],
            metrics=["sam_sharpness", "asam_sharpness", "fim_norm", "fisher_trace", "grad_norm", "weight_norm"],
        ),
        DatasetSpec(
            name="mlp_unified_grid_current",
            path=REPO_ROOT / "experiments" / "04_falsification" / "out" / "unified_grid.csv",
            family="mlp",
            control_covars=["lr", "wd"],
            metrics=["sam_sharpness", "asam_sharpness", "fim_norm", "fisher_trace", "grad_norm", "weight_norm"],
            temporal_metrics=["sam_sharpness", "asam_sharpness"],
        ),
        DatasetSpec(
            name="cnn_kaggle_local_50",
            path=REPO_ROOT / "experiments" / "05_kaggle" / "kaggle_cifar10_results.csv",
            family="cnn",
            control_covars=["lr", "wd"],
            metrics=["sam_sharpness", "grad_norm", "weight_norm", "fisher_trace", "fim_norm", "val_loss"],
        ),
    ]
    if extra_csv and extra_csv.exists():
        specs.append(
            DatasetSpec(
                name="cnn_kaggle_download_250",
                path=extra_csv,
                family="cnn",
                control_covars=["lr", "wd"],
                metrics=["sam_sharpness", "asam_sharpness", "grad_norm", "weight_norm", "fisher_trace", "fim_norm", "val_loss"],
                temporal_metrics=["sam_sharpness", "asam_sharpness"],
            )
        )
    return specs


def summarize_dataset(spec: DatasetSpec) -> dict:
    df = pd.read_csv(spec.path)
    summary = {
        "name": spec.name,
        "path": str(spec.path),
        "rows": int(len(df)),
        "cols": int(len(df.columns)),
        "family": spec.family,
        "final_acc_mean": float(df["final_acc"].mean()) if "final_acc" in df.columns else math.nan,
        "metrics": {},
        "temporal": {},
    }
    for metric in spec.metrics:
        if metric not in df.columns or "final_acc" not in df.columns:
            continue
        abs_r = spearman_like_corr(df, metric, "final_acc")
        part_r = partial_rank_corr(df, metric, "final_acc", spec.control_covars) if all(
            covar in df.columns for covar in spec.control_covars
        ) else math.nan
        summary["metrics"][metric] = {
            "absolute_r": abs_r,
            "partial_r": part_r,
            "narrative": classify_narrative(abs_r, part_r),
        }
    if spec.temporal_metrics:
        for base in spec.temporal_metrics:
            for epoch in [5, 10, 20, 50]:
                metric = f"{base}_ep{epoch}"
                if metric not in df.columns:
                    continue
                summary["temporal"][metric] = {
                    "partial_r": partial_rank_corr(df, metric, "final_acc", spec.control_covars)
                }
    return summary


def render_report(results: list[dict]) -> str:
    lines: list[str] = []
    lines.append("# Independent Artifact Audit")
    lines.append("")
    lines.append("This report ignores manuscript intent and recomputes rank-based correlations directly from saved CSV artifacts.")
    lines.append("")
    for result in results:
        lines.append(f"## {result['name']}")
        lines.append("")
        lines.append(f"- file: `{result['path']}`")
        lines.append(f"- shape: `{result['rows']} x {result['cols']}`")
        lines.append(f"- family: `{result['family']}`")
        lines.append(f"- mean final accuracy: `{result['final_acc_mean']:.4f}`")
        lines.append("")
        lines.append("| metric | abs_r | partial_r | narrative |")
        lines.append("|---|---:|---:|---|")
        for metric, vals in result["metrics"].items():
            part_val = vals["partial_r"]
            part_str = "nan" if np.isnan(part_val) else f"{part_val:+.3f}"
            lines.append(f"| {metric} | {vals['absolute_r']:+.3f} | {part_str} | {vals['narrative']} |")
        if result["temporal"]:
            lines.append("")
            lines.append("| temporal metric | partial_r |")
            lines.append("|---|---:|")
            for metric, vals in result["temporal"].items():
                lines.append(f"| {metric} | {vals['partial_r']:+.3f} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Independently audit saved CSV artifacts.")
    parser.add_argument(
        "--downloaded-csv",
        default=str(DEFAULT_DOWNLOAD),
        help="Optional external Kaggle CSV to include in the audit.",
    )
    args = parser.parse_args()

    downloaded_csv = Path(args.downloaded_csv)
    specs = dataset_specs(downloaded_csv)
    results = [summarize_dataset(spec) for spec in specs if spec.path.exists()]

    report = render_report(results)
    out_dir = Path(__file__).resolve().parent
    report_path = out_dir / "artifact_audit_report.md"
    json_path = out_dir / "artifact_audit_report.json"
    report_path.write_text(report, encoding="ascii", errors="replace")
    json_path.write_text(json.dumps(results, indent=2), encoding="ascii", errors="replace")

    print(report)
    print(f"Saved markdown report to {report_path}")
    print(f"Saved json report to {json_path}")


if __name__ == "__main__":
    main()
