---
name: sci-figure-story-builder
description: Build figure, table, and key-case narrative for SCI manuscripts. Use when the user has figures, cases, tables, experiments, or result blocks but does not know what should be main text vs supplement, how to order figures, what each figure proves, or how figures should connect to the manuscript story.
---

# SCI Figure Story Builder

## Overview

Make figures teach the story. Decide main text, supplement, or cut by asking what question each figure answers and what claim it can support.

## First Move

Ask for a simple figure inventory:

- Figure/case/table name.
- Main observation.
- Evidence type and statistics if available.
- What the user thinks it proves.
- Source data, plotting backend, and export target if the figure is already being prepared for submission.
- Required controls or panels still missing.

## Placement Rules

- Main figures carry the central claim and reader learning path.
- Supplements validate, extend, or document; they should not carry decisive proof.
- Cut or defer figures that do not answer a clear question or distract from the central story.
- Order figures by reader logic, not experiment chronology.
- Keep internal IDs stable as `F#`/`T#`, but let `journal_format_profile` decide the manuscript-facing labels such as `Fig. 1`, `Figure 1`, `Supplementary Fig. 1`, or `Table S1`.
- Treat every main figure as a visual argument: write its core conclusion, panel evidence chain, statistics/integrity notes, and export requirements before drafting Results prose.

## Figure Roles

Assign every figure or table one role:

- Opening phenotype/problem.
- Core mechanism or central proof.
- Validation/control.
- Extension to another system or condition.
- Resource/method performance.
- Supplementary support.
- Source-data or reproducibility support.
- Not needed for this manuscript.

## Workflow

1. Assign each figure a question answered.
2. Write a compact figure contract: core conclusion, evidence chain, figure role, statistics/integrity notes, and export/journal needs.
3. Map each figure to a direct claim and evidence type.
4. Choose main/supplement/cut placement.
5. Identify missing panels, controls, source data, quantification, statistics, image-integrity notes, legends, or export issues.
6. Build a result-section skeleton with transitions between figures.
7. Note the target-journal-facing callout style if `journal_format_profile` is available.

## Ordering Rule

Order by reader learning, not experiment chronology. The reader should move from question to evidence to interpretation with no hidden required proof in the supplement.

## State Coupling

Consume:

- `story.recommended_story.selected_claim_ids`.
- `claim_registry` with safe wording and evidence gaps.
- `analysis_registry` when figure panels depend on statistical outputs, source data, or computational analysis.
- `journal_landscape.journal_format_profile` when available.
- User figure/table/case inventory or existing `figure_registry`.

Update:

- `figure_registry.figures` with stable IDs `F#` or `T#`.
- `figure_registry.figures[].figure_contract` with core conclusion, evidence chain, statistics/integrity notes, and export requirements.
- Each figure's role, answered question, linked claim IDs, placement, missing panels/controls/statistics, and transition.
- Target-journal-facing label notes when the callout style is known.
- `storyline.result_order` provisionally when figure order is clear.

Block:

- If the central story has no main-text evidence, mark the figure gate blocked and route to result/claim repair.
- If figures are absent, produce a needed-figure plan rather than a figure order.
- If source data, statistical annotations, image-integrity handling, or export requirements are unresolved for submission-facing figures, mark them as figure-readiness blockers.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Recommended figure order`.
- `Figure contracts`.
- `Main-text figure plan`.
- `Supplement plan`.
- `Missing panel/control list`.
- `Results section skeleton`.
- `Next module`: usually `sci-storyline-planner` or `sci-reviewer-simulator`.

Read `references/figure-story-map.md` for the template.
