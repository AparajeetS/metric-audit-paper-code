from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path


KERNELS = {
    "image": "aparajeetshadangi/cei-mbe-jmlr-scale-image",
    "text": "aparajeetshadangi/cei-mbe-jmlr-scale-text",
    "confirm_image": "aparajeetshadangi/cei-mbe-jmlr-confirm-image",
    "confirm_text": "aparajeetshadangi/cei-mbe-jmlr-confirm-text",
}

KAGGLE_EXE = Path(r"C:\Users\apara\AppData\Local\Python\pythoncore-3.14-64\Scripts\kaggle.exe")


def run_kaggle(args: list[str]) -> subprocess.CompletedProcess[str]:
    exe = str(KAGGLE_EXE) if KAGGLE_EXE.exists() else "kaggle"
    return subprocess.run([exe, *args], check=False, text=True, capture_output=True)


def status(kernel: str) -> tuple[str, str]:
    proc = run_kaggle(["kernels", "status", kernel])
    text = (proc.stdout + proc.stderr).strip()
    if proc.returncode != 0:
        return "ERROR", text
    if "COMPLETE" in text:
        return "COMPLETE", text
    if "RUNNING" in text:
        return "RUNNING", text
    if "ERROR" in text or "CANCEL" in text or "FAILED" in text:
        return "ERROR", text
    return "UNKNOWN", text


def download(name: str, kernel: str, root: Path) -> None:
    out = root / name
    out.mkdir(parents=True, exist_ok=True)
    proc = run_kaggle(["kernels", "output", kernel, "-p", str(out), "--force"])
    sys.stdout.write(proc.stdout)
    sys.stderr.write(proc.stderr)
    if proc.returncode != 0:
        print(f"download command exited with code {proc.returncode}; CSV files may still have downloaded")


def main() -> None:
    parser = argparse.ArgumentParser(description="Poll Kaggle JMLR-scale kernels and download completed outputs.")
    parser.add_argument("--download-root", type=Path, default=Path("kaggle_downloads"))
    parser.add_argument("--interval", type=int, default=300)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()

    downloaded: set[str] = set()
    while True:
        all_done = True
        for name, kernel in KERNELS.items():
            state, text = status(kernel)
            print(f"{name}: {state} ({text})")
            if state == "COMPLETE" and name not in downloaded:
                download(name, kernel, args.download_root)
                downloaded.add(name)
            elif state == "ERROR":
                if name not in downloaded:
                    download(name, kernel, args.download_root)
                    downloaded.add(name)
            else:
                all_done = False
        if args.once or all_done:
            break
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
