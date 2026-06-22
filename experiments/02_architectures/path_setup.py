"""
Path setup for experiments.
Adds the repository root and sibling experiment directories to sys.path
so that `from metric_audit.sci_tracker import effective_rank` and
cross-directory imports (e.g., `from fim_full_study import MLP`) work
regardless of working directory.
"""
import sys
from pathlib import Path

_repo_root = Path(__file__).resolve().parent.parent.parent
_exp_root  = _repo_root / "experiments"

# Add repo root (for `from metric_audit.sci_tracker import ...`)
if str(_repo_root) not in sys.path:
    sys.path.insert(0, str(_repo_root))

# Add all sibling experiment directories (for cross-imports like `from fim_full_study import MLP`)
for d in _exp_root.iterdir():
    if d.is_dir() and not d.name.startswith('.'):
        if str(d) not in sys.path:
            sys.path.insert(0, str(d))

# Backward-compatible alias: `from sci_tracker import effective_rank` still works
from metric_audit.sci_tracker import effective_rank, sci_from_weight, sci_spectrum
sys.modules['sci_tracker'] = sys.modules['metric_audit.sci_tracker']
