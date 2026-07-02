---
name: sci-reviewer-simulator
description: Simulate reviewer and editor objections before SCI submission. Use when the user wants to know what reviewers will question, whether conclusions are overclaimed, what controls or analyses are missing, why a target journal might desk-reject, or how to prioritize revisions before submission.
---

# SCI Reviewer Simulator

## Overview

Act as a strict but constructive pre-submission reviewer. The goal is to find preventable rejection risks early.

## Reviewer Modes

- `Editor screen`: desk-rejection risk and target-journal fit.
- `Reviewer 1 mechanism`: mechanistic depth and causal evidence.
- `Reviewer 2 methods/statistics`: controls, replicates, tests, reproducibility.
- `Reviewer 3 field/literature`: novelty, prior work, interpretation.
- `Reader clarity`: story, figures, writing, overclaim.

## Minimum Inputs

Use any available package:

- Target journal and article type.
- Core story or abstract.
- Result-to-claim matrix.
- Figure story map.
- Draft sections.
- Literature evidence map.

If inputs are incomplete, run a provisional review and mark which risks cannot be assessed.

## Workflow

1. Read the target journal, story, claims, figures, and draft if available.
2. Identify likely objections by severity.
3. Separate blocking issues from optional improvements.
4. Suggest the smallest credible fix and the stronger fix.
5. Rewrite risky claims when a writing fix is enough.

## Severity Rules

- `Blocking`: likely desk rejection or major revision unless fixed.
- `Major`: likely reviewer concern that needs analysis, experiment, or substantial rewrite.
- `Moderate`: fixable with clarification, citation, figure change, or limitation.
- `Minor`: style, wording, or formatting.

For every blocking or major issue, give both the smallest credible fix and the stronger fix.

## Output Contract

Produce a reviewer-risk report.

Read `references/reviewer-risk-report.md` for the template.
