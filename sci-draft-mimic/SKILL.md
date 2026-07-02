---
name: sci-draft-mimic
description: Initial SCI manuscript drafting by imitating target-journal and user-provided model papers at the level of structure, rhetorical moves, section flow, claim strength, figure citation behavior, and expression style without copying text. Use when the user has journal research, literature evidence, storyline plan, PDFs/model articles, or asks to draft title, abstract, introduction, results, discussion, or cover letter in the style of comparable papers.
---

# SCI Draft Mimic

## Overview

Draft manuscript text by imitating patterns, not wording. Use model papers to learn structure, rhetorical moves, figure/citation behavior, claim strength, and section rhythm while preserving the user's evidence.

## Inputs

Prefer:

- Target journal portrait and article type.
- Benchmark/model papers, comparable papers, or user-provided PDFs.
- Storyline plan and figure/case order.
- Result-to-claim matrix and citation placeholders.
- User's data, methods, statistics, approvals, and wording constraints.

If PDFs or links are provided, analyze their structure and rhetorical moves before drafting. Do not copy sentences, distinctive phrasing, or title formulas too closely.

## Mimic Extraction

Before drafting from model papers or PDFs, extract only reusable patterns:

- Article type and section order.
- Title shape and specificity.
- Abstract move order.
- Introduction funnel and gap statement.
- Results subsection rhythm and figure citation behavior.
- Discussion opening, limitation style, and final implication.
- Supplement naming and citation pattern.
- Citation density, placement, claim strength, and hedging.

Imitate these patterns only at the level of structure and rhetorical function.

## Drafting Rules

- Start with title, abstract, or section outline unless the user asks for a specific section.
- Use `[NEED: ...]` for missing scientific facts.
- Use `[CITE: claim]` for unverified literature support.
- Tie results to figures/tables/supplements.
- Keep claim strength no stronger than the result-to-claim matrix.
- List which model patterns were used and what must be verified.

## Drafting Gate

If journal landscape, result-to-claim mapping, and storyline are missing, draft only a skeleton or partial section with placeholders. Do not create a confident full manuscript from vague conclusions.

## Output Contract

Return:

- `Style brief`.
- `Draft output` for the requested section(s).
- `Citation placeholders`.
- `Missing inputs`.
- `Pattern-use notes`.
- `High-risk claims`.

Read `references/draft-mimic-schema.md` for templates.
