from __future__ import annotations

import os


os.environ.setdefault("CEI_SUITE", "text")
os.environ.setdefault("CEI_MODELS_PER_ARCH", "80")
os.environ.setdefault("CEI_EPOCHS", "12")
os.environ.setdefault("CEI_N_TRAIN", "80000")
os.environ.setdefault("CEI_N_TEST", "12000")
os.environ.setdefault("CEI_METRIC_N", "12")
os.environ.setdefault("CEI_BATCH_SIZE", "64")
os.environ.setdefault("CEI_OUT", "jmlr_scale_text_results.csv")

from jmlr_scale_experiment import main


if __name__ == "__main__":
    main()
