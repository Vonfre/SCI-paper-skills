---
name: sci-result-to-claim
description: Convert experimental or analytical results into defensible SCI manuscript claims. Use when a user has data, figures, tables, cases, observations, or conclusions but cannot tell what they prove, what they cannot prove, what evidence is missing, or how strongly each result can be written for a target journal.
---

# SCI Result To Claim

## Overview

Turn results into evidence-bounded claims. This module protects the manuscript from saying mechanism, causality, novelty, or application when the current data only support observation or association.

## First Move

Ask for results in the easiest available form:

- Figure/table list.
- Key observations.
- Current conclusions.
- Raw result bullets.
- Draft result paragraphs.

If the user lacks polished figures, work from rough result descriptions and mark missing evidence.

## Claim Ladder

Use the weakest accurate claim level:

1. `Descriptive`: X changes under Y.
2. `Association`: X correlates with Y.
3. `Regulation`: perturbing X changes Y.
4. `Mechanism`: X changes Y through Z.
5. `Causality`: X is necessary/sufficient under tested conditions.
6. `Application`: X improves a practical outcome or predicts utility.

## Minimum Input Format

Accept rough input. Convert any of these into a normalized result table:

- Figure list.
- Bullet-point observations.
- Draft result paragraphs.
- Figure legends.
- Conclusions without figures.
- PDF-derived or screenshot-derived figure descriptions when available.

For each result, recover: condition, comparison, method, observation, quantification/statistics if known, and what the user thinks it proves.

## Workflow

1. List each result/figure and what it directly shows.
2. Separate direct observation from interpretation.
3. Assign the strongest defensible claim and the claims it does not support.
4. Identify the smallest missing control, analysis, or citation that would unlock a stronger claim.
5. Recommend safe wording and a next module.

## Claim Discipline

Use these boundaries:

- Observation: the data show a change or pattern.
- Association: two variables move together.
- Regulation: perturbing X changes Y.
- Mechanism: X changes Y through Z.
- Causality: X is necessary or sufficient under tested conditions.
- Application: X improves prediction, intervention, diagnosis, engineering, or practical outcome.

Do not allow phenotype-only data to become a mechanism claim. Do not allow correlation to become causation. Do not allow one model system to become a universal statement without support.

## Output Contract

Return:

- `Result-to-claim matrix`.
- `Claim-strength summary`.
- `Evidence gaps` ranked by importance.
- `Safe wording` and `stronger wording if fixed`.
- `Next module`: usually `sci-core-story-finder`, `sci-figure-story-builder`, or `sci-citation-control`.

Read `references/result-claim-matrix.md` for the output template.
