import numpy as np
import pandas as pd

from mbe_eval import MBEEvaluator, audit_metric, audit_metrics, partial_rank_corr


def synthetic_frame(seed=0, n=300):
    rng = np.random.default_rng(seed)
    learning_rate = rng.choice([1e-4, 3e-4, 1e-3, 3e-3], size=n)
    weight_decay = rng.choice([0.0, 1e-5, 1e-4], size=n)
    architecture = rng.choice(["cnn", "resnet"], size=n)
    baseline = -np.log10(learning_rate) + 0.2 * (architecture == "cnn") + rng.normal(0, 0.05, n)
    target = -baseline + rng.normal(0, 0.08, n)
    proxy_metric = baseline + rng.normal(0, 0.05, n)
    residual_metric = target - 0.3 * baseline + rng.normal(0, 0.05, n)
    return pd.DataFrame(
        {
            "proxy_metric": proxy_metric,
            "residual_metric": residual_metric,
            "baseline": baseline,
            "learning_rate": learning_rate,
            "weight_decay": weight_decay,
            "architecture": architecture,
            "target": target,
        }
    )


def test_audit_metrics_shows_proxy_signal_collapses_after_controls():
    df = synthetic_frame()
    report = audit_metrics(
        df,
        metrics=["proxy_metric", "residual_metric"],
        target="target",
        controls=["baseline", "learning_rate", "weight_decay", "architecture"],
    )
    by_metric = report.set_index("metric")

    assert abs(by_metric.loc["proxy_metric", "raw_r"]) > 0.6
    assert abs(by_metric.loc["proxy_metric", "partial_r"]) < 0.2
    assert by_metric.loc["proxy_metric", "partial_p"] > 0.05
    assert by_metric.loc["residual_metric", "classification"] in {
        "survives",
        "hidden-after-control",
    }


def test_partial_rank_corr_accepts_categorical_controls():
    df = synthetic_frame()
    r, p, n = partial_rank_corr(
        df,
        metric="proxy_metric",
        target="target",
        controls=["baseline", "architecture"],
    )

    assert n == len(df)
    assert np.isfinite(r)
    assert np.isfinite(p)


def test_backward_compatible_evaluator():
    df = synthetic_frame()
    evaluator = MBEEvaluator(metric_name="proxy", baseline_name="baseline")
    report = evaluator.evaluate(
        df["proxy_metric"].to_numpy(),
        df["baseline"].to_numpy(),
        df["target"].to_numpy(),
    )

    assert report.metric_name == "proxy"
    assert report.baseline_name == "baseline"
    assert np.isfinite(report.absolute_r)
    assert np.isfinite(report.partial_r)


def test_audit_metric_ignores_metric_when_it_is_also_a_control():
    df = synthetic_frame()
    row = audit_metric(
        df,
        metric="baseline",
        target="target",
        controls=["baseline", "learning_rate", "architecture"],
    )

    assert row["metric"] == "baseline"
    assert np.isfinite(row["raw_r"])
    assert np.isfinite(row["partial_r"])
