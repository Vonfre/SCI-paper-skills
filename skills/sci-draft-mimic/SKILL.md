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
- Make the Introduction literature-backed: move from field background to known mechanisms, unresolved gap, scientific question, and study objective with sources assigned to each role.
- Make Results evidence-dense: each subsection needs direct data, controls, quantification/statistics, figure references, and a brief interpretive bridge that connects to the next result without over-discussing.
- Make Discussion multi-angle: start from the main result, then expand through prior work, mechanism, alternative explanations, significance, limitations, and future experiments.
- Make Methods reproducible: include biological material, treatment details, sample sizes, controls, instrumentation, analysis software, statistical model, and data availability when known.
- List which model patterns were used and what must be verified.

## Drafting Gate

If journal landscape, result-to-claim mapping, and storyline are missing, draft only a skeleton or partial section with placeholders. Do not create a confident full manuscript from vague conclusions.

## State Coupling

Consume:

- `journal_landscape`, `source_ledger`, `claim_registry`, `figure_registry`, `story`, `storyline`, and `reviewer_risk`.
- Model paper IDs `P#` and source IDs `S#` when available.

Update:

- `draft_registry.sections` with section IDs `SEC#` from `storyline.section_registry`.
- `draft_registry.open_needs`, `open_citations`, and `high_risk_claim_ids`.
- Section drafts that preserve linked claim IDs `C#`, figure/table IDs `F#`/`T#`, and source placeholders `S#` or `[CITE: ...]`.

Block:

- If journal, claim, story, figure, or citation gates are missing, produce a skeleton or section scaffold only.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Style brief`.
- `Draft output` for the requested section(s).
- `Citation placeholders`.
- `Missing inputs`.
- `Pattern-use notes`.
- `High-risk claims`.

Read `references/draft-mimic-schema.md` for templates.
Read `references/manuscript-section-quality.md` before drafting a full manuscript, Introduction, Results, Discussion, or Methods section.
