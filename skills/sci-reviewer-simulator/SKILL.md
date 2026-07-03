---
name: sci-reviewer-simulator
description: Simulate reviewer and editor objections before SCI submission. Use when the user wants to know what reviewers will question, whether conclusions are overclaimed, what controls or analyses are missing, why a target journal might desk-reject, whether journal-format issues remain, or how to prioritize revisions before submission.
---

# SCI Reviewer Simulator

## Overview

Stress-test the manuscript as an editor and reviewer would. Prioritize objections that can block acceptance, not every possible nitpick.

## Reviewer Modes

Use the relevant modes:

- `Editor screen`: scope, novelty, article type, and desk-rejection risk.
- `Method reviewer`: design, controls, statistics, reproducibility, reporting.
- `Statistical reviewer`: test/model choice, assumptions, effect sizes, uncertainty, multiple testing, power, and replicate logic.
- `Mechanism reviewer`: causality, pathway depth, alternative explanations.
- `Field expert`: novelty, prior work, citation omissions, overclaiming.
- `Figure reviewer`: whether each figure's visual argument, source data, statistics, accessibility, and export quality can survive review.
- `Data/reproducibility reviewer`: data/code availability, repository/accession status, software versions, source data, and FAIR or reporting requirements.
- `Writing reviewer`: structure, figure clarity, paragraph logic, tone.
- `Format reviewer`: target-journal callouts, legends, table titles, references, headings, and supplementary-material naming.

Run separate passes when enough input is available. Do not merge all concerns into one generic critique; preserve which reviewer type would raise each issue.

## Severity Scale

- `Blocking`: likely desk reject or major rejection if unresolved.
- `Major`: revision required before submission or rebuttal.
- `Moderate`: fix improves credibility.
- `Minor`: wording, clarity, or formatting.

## Minimum Inputs

Use any available package:

- Target journal and article type.
- Core story or abstract.
- Result-to-claim matrix.
- Figure story map.
- Analysis provenance or statistical report when quantitative claims are present.
- Data/code availability notes when the manuscript is near submission.
- Draft sections.
- Literature evidence map.

If inputs are incomplete, run a provisional review and mark which risks cannot be assessed.

## Workflow

1. Read the target journal, story, claims, figures, and draft if available.
2. Identify the submission bar and most likely reviewer expertise.
3. Score journal fit, novelty, evidence strength, method rigor, statistical credibility, figure logic, data/code availability, citation health, journal-format consistency, and writing logic.
4. List objections with severity and evidence.
5. Separate fixes that need new data from fixes possible by writing, analysis, citation, or figure reorganization.
6. Recommend submit, revise before submission, do more work, or reconsider journal.

## Severity Rules

- `Blocking`: likely desk rejection or major revision unless fixed.
- `Major`: likely reviewer concern that needs analysis, experiment, or substantial rewrite.
- `Moderate`: fixable with clarification, citation, figure change, or limitation.
- `Minor`: style, wording, or formatting.

For every blocking or major issue, give both the smallest credible fix and the stronger fix.

## State Coupling

Consume:

- `journal_landscape`, `journal_landscape.journal_format_profile`, `analysis_registry`, `source_ledger`, `claim_registry`, `figure_registry`, `data_availability_plan`, `story`, `storyline`, `draft_registry`, and `citation_audit` if available.

Update:

- `reviewer_risk.scorecard`, `blocking_objections`, `major_objections`, `repair_queue`, and `decision`.
- Reviewer issue IDs `R#`.
- `claim_registry.claims[].status` when overclaims are found.
- `analysis_registry.statistical_plan[].status` and `figure_registry.figures[].figure_contract` risks when analysis or figure readiness blocks submission.
- `storyline.draft_readiness` when reviewer risk blocks drafting.

Block:

- If blocking objections remain, route to the specific repair module before drafting or submission.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Desk-rejection risk`.
- `Reviewer scorecard`.
- `Reviewer objection matrix`.
- `Overclaim audit`.
- `Missing control/analysis`.
- `Statistics, figure, and data-availability risks`.
- `Prioritized repair plan`.
- `Decision`.

Read `references/reviewer-risk-report.md` for the template.
Read `references/multi-reviewer-rubric.md` when running a full pre-submission or revision risk simulation.
