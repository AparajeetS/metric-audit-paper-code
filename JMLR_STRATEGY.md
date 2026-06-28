# JMLR Strategy: MBE as the Main Contribution

## Recommended Narrative

The strongest paper is not "FIM_norm is universally bad" and not "we found a better metric."

The strongest paper is:

> Many proposed generalization metrics appear predictive under raw pooled correlation. We introduce Marginal Baseline Evaluation (MBE), an empirical audit protocol for testing whether a metric carries marginal predictive information beyond known training determinants and ordinary baselines. Across 680 image and language-model runs, MBE reveals washout, sign reversal, hidden-after-control effects, and task/architecture dependence.

This narrative survives the current artifact state:

- FIM_norm survives in image-only audits, washes out in text-only audits, and reverses sign in the full image+text pool.
- MBE weakens feature-rank, distance/update, and weight-norm artifacts.
- Several metrics survive, including validation loss, gradient/Fisher magnitude metrics, logit confidence metrics, and metric-batch accuracy.
- The instability itself is evidence for the methodological claim: isolated raw correlations are not a reliable basis for metric claims.

## Claims We Should Make

1. Parameter-space metric evaluations require explicit marginal controls.
2. Learning rate, weight decay, dropout, optimizer, task, architecture, and seed are not nuisance details; they can determine both the metric and the target.
3. Metrics should be evaluated within and across suites, because pooling can change signs and classes.
4. A credible metric paper should report raw correlations, controlled correlations, strict baseline controls, and stability across design axes.
5. MBE is a reusable protocol for falsifying or qualifying metric claims.

## Claims We Should Avoid

1. Avoid claiming that all geometric metrics universally invert.
2. Avoid claiming FIM_norm is universally useless.
3. Avoid claiming MBE proves causal effects of metrics.
4. Avoid saying validation-loss controls are always right or always wrong. Treat strict loss-control MBE as a robustness audit.
5. Avoid implying that a single pooled table is the whole result.

## Current Evidence Map

### 680-Model JMLR-Scale Evidence

The current backbone is the confirmed 680-model audit:

- 480 CIFAR-10 image models across CNN, ResNet, ViT, and WideResNet.
- 200 character-transformer language models.
- More than 20 metrics audited under raw correlation, design-variable MBE, and strict validation-loss MBE.

FIM_norm:

- image-only default: `-0.662 -> -0.218`, survives
- text-only default: `-0.291 -> +0.014`, washout
- full pooled default: `+0.225 -> -0.203`, reverse-inversion
- full pooled strict: `+0.225 -> -0.300`, reverse-inversion

Safe interpretation:

> FIM_norm is not a robust universal generalization metric. Its conclusion depends on task, architecture mix, and pooling. MBE exposes this instability while preserving several other signals.

### Earlier MLP/CNN Evidence

The earlier MLP and CNN grids are now supporting context, not the central claim.

- MLP grids show confounding and inversion for SAM-like metrics.
- Earlier CNN/BatchNorm runs showed checkpoint and sample-size sensitivity.
- These experiments motivated the broader JMLR-scale audit.

Safe interpretation:

> Earlier inconsistencies are not a liability if framed correctly: they are why MBE needs to be a protocol with controls, grouping, and replication rather than a single raw-correlation table.

## JMLR-Level Experiment Plan

### Experiment A: Frozen Holdout Replication

Goal: verify that the 680-model qualitative conclusions replicate without narrative tuning.

Design:

- Same code path and metric battery.
- New seeds.
- Fixed analysis protocol.
- Report raw, MBE, and strict MBE before changing the story.

Expected analysis:

- raw Spearman correlation
- partial rank correlation controlling design variables
- strict partial rank correlation also controlling validation loss
- bootstrap confidence intervals
- replication-level variance
- class stability across suites and architectures

What JMLR gets:

- the core finding is not a one-shot artifact
- the paper becomes a reproducible audit protocol, not a tuned result

### Experiment B: Independent Suite

Goal: show the method is not overfit to CIFAR-10 plus Tiny Shakespeare.

Design:

- one additional image dataset or one additional text dataset
- smaller but cleanly reproducible
- same metric battery and analysis protocol

Expected analysis:

- compare metric classes to the current 680-model evidence
- identify which conclusions are stable across tasks

What JMLR gets:

- evidence that MBE is a method, not a one-dataset artifact

### Experiment C: Negative Control and Positive Control

Goal: prove the audit can distinguish useless, confounded, and genuinely informative signals.

Negative controls:

- random metric column
- permuted metric column
- metric computed on randomly initialized networks after matching hyperparameters

Positive controls:

- validation loss or validation accuracy, clearly labeled as ordinary predictive baselines
- train loss as a post-training diagnostic, while keeping the causal caveat explicit

Expected analysis:

- negative controls should wash out
- validation baselines should remain predictive
- geometric metrics should be compared against both

What JMLR gets:

- the audit is calibrated
- reviewers cannot say the protocol just destroys every signal mechanically

### Experiment D: Uncertainty and Sensitivity

Goal: make the reported classes statistically credible.

Required additions:

- bootstrap CIs for raw and partial correlations
- threshold sensitivity tables
- permutation tests
- suite-level and architecture-level resampling

What JMLR gets:

- uncertainty-aware metric classes
- less dependence on arbitrary thresholds

## Manuscript Shape

1. Motivation: metric papers often overclaim from raw correlations.
2. MBE protocol: define the audit and the causal intuition.
3. Main evidence: 680-model audit across image and text.
4. Case study: FIM_norm survives, washes out, or reverses depending on task/pooling.
5. Metric taxonomy: which families survive, wash out, invert, or appear after control.
6. Controls: negative and positive controls calibrate the audit.
7. Robustness: strict validation-loss controls, within-suite analysis, bootstrap CIs.
8. Discussion: MBE as a reporting standard for future metric papers.

## Working Title Options

- "Marginal Baseline Evaluation for Generalization Metrics"
- "Auditing Generalization Metrics Beyond Pooled Correlation"
- "When Generalization Metrics Fail Their Baselines"

Best current title:

> Marginal Baseline Evaluation: Auditing Generalization Metrics Beyond Pooled Correlation

This title lets the data go where it wants. It does not force every experiment to prove inversion.

## Decision

Take the MBE-methodology path.

The durable JMLR paper is a protocol paper with multiple failure modes:

- inversion
- washout
- hidden-after-control effects
- task/architecture sensitivity
- pooling artifacts

That is broader, truer to the current evidence, and much harder for reviewers to dismiss.
