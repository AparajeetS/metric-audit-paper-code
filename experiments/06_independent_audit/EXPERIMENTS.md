# Independent Checks

These are independent-from-manuscript checks meant to answer one question:

What does the current saved evidence say, even if the working folder has rough edges?

## Experiment 1: Artifact Reproduction

Read saved CSV artifacts directly and recompute:

- absolute rank correlation with `final_acc`
- partial rank correlation controlling for `lr` and `wd`

Why it matters:

- this tests the paper narrative against the saved evidence, not against memory or manuscript prose
- it is robust to script drift as long as the CSV is intact

Implemented in [artifact_audit.py](C:/Research/cei/metric-audit-paper-code/experiments/06_independent_audit/artifact_audit.py).

## Experiment 2: Temporal Checkpoint Audit

For artifacts that contain `*_ep5`, `*_ep10`, `*_ep20`, and `*_ep50`, recompute the partial rank correlation at each checkpoint.

Why it matters:

- it tells us whether the narrative is really "mid-training inversion", "late negative recovery", or simple washout
- it keeps the story tied to checkpoint-specific evidence instead of one aliased summary column

## Experiment 3: Narrative Stability Across Artifacts

Compare the same metric family across:

- `large_grid_v3_asam.csv`
- `unified_grid.csv`
- local 50-row Kaggle CSV
- downloaded 250-row Kaggle CSV

Why it matters:

- this tells us whether a claim is stable, version-sensitive, or just an interim artifact story
- it is the fastest way to decide which claims are safe enough for the manuscript

## Current Use

Run:

```powershell
& 'C:\Users\apara\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'C:\Research\cei\metric-audit-paper-code\experiments\06_independent_audit\artifact_audit.py'
```

This writes:

- [artifact_audit_report.md](C:/Research/cei/metric-audit-paper-code/experiments/06_independent_audit/artifact_audit_report.md)
- [artifact_audit_report.json](C:/Research/cei/metric-audit-paper-code/experiments/06_independent_audit/artifact_audit_report.json)
