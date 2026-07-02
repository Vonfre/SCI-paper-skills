---
name: sci-journal-landscape
description: Target journal profile plus comparable-paper landscape scan for SCI manuscripts. Use after intake when the user provides a target journal and research direction, or asks whether a journal has similar papers; produce journal positioning, author requirements, OA/metrics, same-journal similar articles, same-level fallback articles when same-journal matches are absent, and a high-level strategic opinion for submission.
---

# SCI Journal Landscape

## Overview

Answer: "What kind of journal is this, and how does my topic fit the papers it publishes?" This module combines journal profiling with same-journal/same-level paper scouting.

## Required Inputs

- Target journal or candidate journals.
- Research topic/direction.
- Article type if known.

If article type is missing, infer likely choices and mark as provisional.

## Evidence Rules

Use current web research. Journal information and recent article lists change. Prioritize official journal/publisher pages, author guidelines, PubMed/Crossref/DOI records, journal issue pages, and reputable metrics/indexing sources.

## Workflow

1. Resolve the journal.
   - Confirm title, publisher, ISSN/eISSN, official website, author instructions, article types, OA/APC, metrics, indexing, and submission system.

2. Build the journal portrait.
   - Scope, audience, paper types, novelty threshold, preferred evidence depth, desk-rejection risks.

3. Search for same-journal similar papers.
   - Use topic keywords, model system, method keywords, disease/organism/material terms, and article type.
   - Prefer the last 1-3 years when possible.

4. If same-journal matches are weak or absent, search peer journals.
   - Select journals at similar level/scope or sister journals in the same publisher/society family.
   - State why each peer journal is considered comparable.

5. Score journal fit.
   - Assess novelty, evidence depth, article type fit, audience breadth, field saturation, and desk-rejection risk.

6. Provide landscape opinion.
   - What the field has already done.
   - What the target journal seems to reward.
   - What the user's manuscript must prove to fit.
   - Whether the current target is ambitious, reasonable, or risky.

## Output Contract

Produce:

- `Journal portrait`.
- `Author-rule constraints`.
- `Same-journal article scan`.
- `Peer-journal fallback scan` if needed.
- `Journal fit rubric`.
- `Landscape opinion`.
- `Next handoff`: usually `sci-literature-evidence`, `sci-result-to-claim`, or `sci-core-story-finder`.

Read `references/landscape-output-schema.md` for the template.
