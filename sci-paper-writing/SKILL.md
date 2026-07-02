---
name: sci-paper-writing
description: DEPRECATED. Do not use for new work. Replaced by sci-draft-mimic, sci-paragraph-coach, and sci-language-polisher in the final SCI manuscript workflow.
---

# SCI Paper Writing

## Overview

Write only after the target journal, section purpose, evidence, and claim strength are clear. This skill turns architecture and evidence into polished scientific prose aligned with the target journal.

## Inputs

Prefer:

- Journal dossier and voice model.
- Section blueprint from `sci-manuscript-architecture`.
- Claim-evidence-citation map from `sci-citation-control`.
- User's data, results, figure legends, methods details, or existing draft.

If a required scientific fact is missing, use `[NEED: ...]`; never invent data, statistics, approvals, accession numbers, or references.

## Writing Modes

- `Draft`: create a section from structured inputs.
- `Rewrite`: improve flow, logic, and claim discipline while preserving meaning.
- `Polish`: refine scientific English, concision, hedging, transitions, and journal voice.
- `Translate`: convert Chinese scientific text into idiomatic English, not literal word-for-word English.
- `Compress`: reduce to word limit without removing essential evidence.
- `Reviewer-facing revision`: rewrite text to address review comments with precise changes.

## Workflow

1. Identify the section and purpose.
   - Title, abstract, introduction, results, discussion, methods, limitations, cover text, or declarations.

2. Check claim strength.
   - Distinguish observation, association, prediction, mechanism, causality, validation, and clinical/application implication.

3. Use the journal voice model.
   - Match section length, title style, abstract structure, result flow, supplement citation style, and degree of hedging from benchmark papers.
   - Do not copy benchmark wording.

4. Draft with traceability.
   - Tie result statements to figures/tables/supplements.
   - Tie literature claims to citation placeholders or verified references.
   - Mark missing facts clearly.

5. Return revision notes.
   - List assumptions, unresolved placeholders, high-risk claims, and suggested next module.

## Section Priorities

- Title: concise, specific, claim-appropriate, journal-compatible.
- Abstract: context, gap, objective, methods, main evidence, implication.
- Introduction: move quickly from field problem to precise gap and study objective.
- Results: one scientific question per subsection; evidence before interpretation.
- Discussion: principal findings, relation to prior work, implications, limitations, future work, measured conclusion.
- Methods: reproducibility, software/version details, statistics, ethics, data/code availability.

## Output Contract

Return polished text plus:

- `Assumptions`.
- `Missing inputs`.
- `Claims needing citation`.
- `Claims needing data support`.
- `Fit/style notes`.

Read `references/section-writing-protocol.md` for section-specific templates.
