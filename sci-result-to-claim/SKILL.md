---
name: sci-result-to-claim
description: Convert experimental or analytical results into defensible SCI manuscript claims. Use when a user has data, figures, tables, cases, observations, or conclusions but cannot tell what they prove, what they cannot prove, what evidence is missing, or how strongly each result can be written for a target journal.
---

# SCI Result To Claim

## Overview

Help inexperienced authors translate results into manuscript claims. The goal is to prevent both under-writing and overclaiming.

## First Move

Ask the user for their results in the easiest available form:

- Figure list with one sentence per figure.
- Raw bullet-point results.
- Current conclusions.
- Uploaded draft/figure legends.

If the user has no figure list, ask for 3-8 key observations and the methods used.

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

1. Normalize results.
   - Rewrite each result as: observation, comparison, condition, method, and confidence.

2. Infer possible claims.
   - Separate direct claims, supported interpretations, speculative implications, and claims not yet supported.

3. Grade claim strength.
   - Descriptive, association, regulation, mechanism, causality, application, or resource.

4. Identify evidence gaps.
   - Missing control, replicate, validation, causal test, rescue, orthogonal method, literature support, or statistical detail.

5. Recommend wording.
   - Provide safe manuscript wording and stronger wording only if additional evidence is supplied.

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

Produce a result-to-claim table plus next actions.

Read `references/result-claim-matrix.md` for the output template.
