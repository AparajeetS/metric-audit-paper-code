import numpy as np
import pandas as pd

from .core import audit_metrics


def simulate_mbe_evaluation(seed: int = 42) -> pd.DataFrame:
    """Run a small synthetic MBE audit."""

    rng = np.random.default_rng(seed)
    n_runs = 80

    learning_rate = rng.choice([1e-4, 3e-4, 1e-3, 3e-3], size=n_runs)
    weight_decay = rng.choice([0.0, 1e-5, 1e-4], size=n_runs)
    architecture = rng.choice(["mlp_small", "mlp_wide"], size=n_runs)

    difficulty = -np.log10(learning_rate) + 0.25 * (architecture == "mlp_small")
    final_accuracy = 0.78 - 0.06 * difficulty - 8.0 * weight_decay + rng.normal(0, 0.025, n_runs)
    validation_loss = 1.5 - final_accuracy + rng.normal(0, 0.04, n_runs)

    loss_proxy_metric = validation_loss + rng.normal(0, 0.04, n_runs)
    residual_metric = final_accuracy - 0.30 * validation_loss + rng.normal(0, 0.03, n_runs)
    random_metric = rng.normal(size=n_runs)

    df = pd.DataFrame(
        {
            "loss_proxy_metric": loss_proxy_metric,
            "residual_metric": residual_metric,
            "random_metric": random_metric,
            "validation_loss": validation_loss,
            "learning_rate": learning_rate,
            "weight_decay": weight_decay,
            "architecture": architecture,
            "final_accuracy": final_accuracy,
        }
    )

    report = audit_metrics(
        df,
        metrics=["loss_proxy_metric", "residual_metric", "random_metric"],
        target="final_accuracy",
        controls=["validation_loss", "learning_rate", "weight_decay", "architecture"],
    )
    print(report[["metric", "raw_r", "partial_r", "classification"]].to_string(index=False))
    return report


if __name__ == "__main__":
    simulate_mbe_evaluation()
