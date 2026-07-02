---
name: sci-literature-evidence
description: Literature search and evidence evaluation around scientific questions, hypotheses, and conclusions for SCI manuscripts. Use when the user has a scientific question, tentative direction, or research conclusion and needs supporting/conflicting literature, plausibility evaluation, gap analysis, possible research directions when conclusions are absent, or a map of what previous papers did and how they handled similar problems.
---

# SCI Literature Evidence

## Overview

Connect the user's scientific question or conclusion to the literature. This module decides whether a conclusion is supported, risky, novel, incremental, or needs a different research angle.

## Branches

If the user has conclusions:

1. Break each conclusion into claim units.
2. Search for supporting, conflicting, and adjacent literature.
3. Evaluate plausibility, novelty, evidence level, and missing controls.
4. Recommend how strongly the conclusion can be written.

For each conclusion, decide whether the literature directly supports it, only supports a nearby idea, contradicts it, or leaves it untested.

If the user has only a question/direction:

1. Search recent and foundational literature.
2. Identify what has already been done.
3. Extract methods, models, variables, and unresolved gaps.
4. Propose 2-4 feasible research directions and what evidence each would require.

For each possible direction, state what previous papers already did and what new evidence would be needed for the user's target journal.

## Search Priorities

- Recent primary research in the last 3-5 years.
- Foundational mechanism papers.
- High-quality reviews only for broad framing.
- Same-journal or same-level papers when relevant to target journal fit.
- Official database records for DOI/PMID and retraction checks when available.

## Citation Role Control

Explain whether each source is useful for:

- Background framing.
- Gap identification.
- Claim support.
- Alternative explanation.
- Method precedent.
- Discussion comparison.

Do not treat one review as direct evidence for a precise mechanism when a primary paper is needed.

## Output Contract

Produce:

- `Question/claim decomposition`.
- `Evidence table`.
- `Support level`: strong, moderate, weak, contradictory, or unknown.
- `Novelty/gap assessment`.
- `Possible directions` if conclusions are absent.
- `Evidence needed next`.
- `Writing risk`: which statements need softening.

Read `references/evidence-map-schema.md` for templates.
