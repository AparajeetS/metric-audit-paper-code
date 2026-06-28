from __future__ import annotations

import os


os.environ.setdefault("CEI_SUITE", "image")
os.environ.setdefault("CEI_ARCHS", "cnn,resnet,wide_resnet,vit")
os.environ.setdefault("CEI_MODELS_PER_ARCH", "40")
os.environ.setdefault("CEI_EPOCHS", "25")
os.environ.setdefault("CEI_N_TRAIN", "20000")
os.environ.setdefault("CEI_N_TEST", "5000")
os.environ.setdefault("CEI_METRIC_N", "16")
os.environ.setdefault("CEI_BATCH_SIZE", "128")
os.environ.setdefault("CEI_OUT", "jmlr_scale_image_results.csv")

from jmlr_scale_experiment import main


if __name__ == "__main__":
    main()
