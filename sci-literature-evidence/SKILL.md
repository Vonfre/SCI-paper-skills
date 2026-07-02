---
name: sci-literature-evidence
description: Literature search and evidence evaluation around scientific questions, hypotheses, and conclusions for SCI manuscripts. Use when the user has a scientific question, tentative direction, or research conclusion and needs supporting/conflicting literature, plausibility evaluation, gap analysis, possible research directions when conclusions are absent, or a map of what previous papers did and how they handled similar problems.
---

# SCI Literature Evidence

## Overview

Map what the literature supports, contradicts, leaves open, or makes risky. The goal is not a broad bibliography; it is to decide what the manuscript can safely say and what work is still needed.

## Branches

Use one branch based on the user's state:

- `Existing conclusion`: break each conclusion into claim units, search supporting/conflicting/adjacent literature, evaluate plausibility and missing controls, and recommend safe wording.
- `Open question`: identify recent and foundational work, extract methods/models/variables, define unresolved gaps, and propose 2-4 feasible directions.
- `Target-journal framing`: find same-journal or same-level papers that shape the problem, gap, and novelty frame.

For each conclusion or possible direction, state whether the literature directly supports it, supports only a nearby idea, contradicts it, or leaves it untested.

## Search Priorities

- Primary papers for specific mechanisms, methods, or findings.
- Recent reviews for field framing, not as sole proof for precise claims.
- Same-journal or same-level papers when journal fit matters.
- Official database records for DOI/PMID and retraction checks when available.

## Citation Role Control

Explain whether each source is useful for background framing, gap identification, claim support, alternative explanation, method precedent, or discussion comparison. Do not treat one review as direct evidence for a precise mechanism when a primary paper is needed.

## Evidence Grading

- `Strong`: direct primary evidence plus user data can plausibly support the claim.
- `Moderate`: related evidence exists but controls, mechanism, or context remain incomplete.
- `Weak`: only indirect or neighboring literature supports the idea.
- `Conflicting`: credible literature suggests an alternative explanation.
- `Unknown`: search coverage is insufficient.

## Output Contract

Return:

- `Evidence map` for each user question or conclusion.
- `Support/conflict summary`.
- `Gap assessment`.
- `Writing recommendation`: safe wording, citations needed, or claim to avoid.
- `Next module`: usually `sci-result-to-claim`, `sci-core-story-finder`, or `sci-citation-control`.

Read `references/evidence-map-schema.md` for templates.
