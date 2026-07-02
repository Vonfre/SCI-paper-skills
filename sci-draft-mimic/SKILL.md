---
name: sci-draft-mimic
description: Initial SCI manuscript drafting by imitating target-journal and user-provided model papers at the level of structure, rhetorical moves, section flow, claim strength, figure citation behavior, and expression style without copying text. Use when the user has journal research, literature evidence, storyline plan, PDFs/model articles, or asks to draft title, abstract, introduction, results, discussion, or cover letter in the style of comparable papers.
---

# SCI Draft Mimic

## Overview

Draft the first manuscript text by imitating patterns, not wording. This module uses same-journal papers or user-provided PDFs as style models and writes a traceable first draft.

## Inputs

Prefer:

- Target journal portrait and article type.
- Benchmark/model papers or PDFs.
- Storyline plan and figure/case order.
- Claim-evidence map.
- User's data or conclusions.

If the user provides PDFs, analyze their structure and rhetorical moves before drafting. Do not copy sentences or distinctive phrasing.

## Workflow

1. Extract model-paper patterns.
   - Title type, abstract moves, introduction funnel, result-section rhythm, figure citation style, discussion structure, hedging.

2. Create a style brief.
   - What to imitate, what to avoid, and what must be adapted to the user's topic.

3. Draft by section.
   - Start with title/abstract/section outline unless the user asks for a specific section.
   - Use `[NEED: ...]` placeholders for missing facts.
   - Keep citations as verified references or `[CITE: claim]` placeholders.

4. Return traceability notes.
   - List which model patterns were used and which claims need data/citation.

## Output Contract

Produce:

- `Model-paper style brief`.
- `Draft text`.
- `Imitation notes`: structure/style only.
- `Missing data`.
- `Citation placeholders`.
- `Risks for overclaiming`.

Read `references/draft-mimic-schema.md` for templates.
