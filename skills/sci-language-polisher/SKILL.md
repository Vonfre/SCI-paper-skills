---
name: sci-language-polisher
description: Final scientific-language, paragraph-plan, Word/DOCX, and journal-format polishing for SCI manuscripts. Use when the user has draft text and wants clearer, more precise, journal-appropriate English or Chinese-to-English polishing; improve logic, concision, transitions, claim strength, hedging, terminology, abstract flow, results wording, discussion tone, paragraph count discipline, figure/table/supplement callout style, Word manuscript formatting notes, headings, cover letters, and reviewer responses without changing the scientific meaning or inventing evidence.
---

# SCI Language Polisher

## Overview

Polish expression after the scientific logic is decided. Improve clarity, precision, flow, tone, and journal fit while preserving meaning and evidence boundaries.

## First Move

Identify the polish mode:

- `Meaning-preserving polish`: improve clarity without changing claims.
- `Claim-strength polish`: soften unsupported causality, novelty, or broad significance.
- `Chinese-to-English`: produce idiomatic scientific English, not literal translation.
- `Compression`: reduce length while preserving evidence.
- `Reviewer-facing polish`: make response or revision wording precise and calm.
- `Journal-style polish`: align with observed target-journal patterns.
- `Journal-format polish`: normalize figure/table/supplement callouts, legend labels, headings, statements, and reference style against `journal_format_profile`.
- `Paragraph-plan polish`: keep sections within planned natural paragraph counts and repair overlong Results subsections.
- `Word-format polish`: preserve or flag DOCX line numbering, black 12 pt text, 1.5 spacing, justified body text, and left-aligned headings.

Ask for target journal, section type, and word limit only when needed.

## Non-Negotiables

- Do not add data, references, conclusions, approvals, or experimental details.
- Do not strengthen claims beyond the supplied evidence.
- Preserve technical terms and sample/context boundaries.
- Keep unresolved facts visible as `[NEED: ...]`.

## Before Polishing

Check whether the problem is language or logic:

- If claims are unsupported, route to `sci-result-to-claim` or `sci-citation-control`.
- If paragraph purpose is unclear, route to `sci-paragraph-coach`.
- If the whole section order is weak, route to `sci-storyline-planner`.
- If only expression, clarity, concision, tone, idiomatic English, or journal-format consistency is weak, continue polishing.

## Workflow

1. Identify paragraph/section purpose and claim strength.
2. Remove ambiguity, redundancy, vague verbs, and unsupported superlatives.
3. Improve transitions and sentence order when logic is local.
4. Normalize journal-format items from `journal_format_profile`: `Fig.`/`Figure` forms, panel letters, multi-figure callouts, supplementary labels, figure legends, table titles, headings, references, and statements.
5. Check the paragraph plan when polishing full sections; do not expand Results subsections beyond 2-3 paragraphs unless already justified.
6. For Results, preserve evidence-first order while adding only short reliability or transition clauses.
7. For Discussion, improve breadth by linking the main result to literature, mechanism, alternative explanations, limitations, and implications without inventing new evidence.
8. For DOCX-facing outputs, flag any action that could disturb Word formatting and route final file checks to `sci-submission-revision`.
9. Return before/after examples for recurring language or format problems when useful.
10. Flag claims that still need data, citation, format-rule verification, or upstream logic repair.

## Polishing Rule

Do not silently strengthen claims. If a sentence changes from association to mechanism, mechanism to causality, or observation to application, flag it and provide a safer alternative.

## State Coupling

Consume:

- `draft_registry.sections`, source text, `claim_registry`, `citation_audit`, `storyline.paragraph_plan`, `document_output.word_format_profile`, `journal_landscape.journal_format_profile`, and target-journal tone/style when available.

Update:

- `draft_registry.sections[].draft_status` to `polished` only when meaning is stable.
- `draft_registry.high_risk_claim_ids` when polishing reveals overclaiming.
- A meaning-change log that lists any softened or preserved claims by `claim_id`.
- A format-correction log for changed figure/table/supplement callouts, headings, legends, tables, references, and statement labels.
- Paragraph-plan repair notes and Word-format follow-up notes when relevant.

Block:

- If meaning, evidence, citation support, or target-journal format rules are unstable, do not present the text as final-polished. Route to claim, citation, or journal-format repair.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Polished text`.
- `Meaning preservation note`.
- `Claim-strength changes`.
- `Format corrections`.
- `Before -> after examples` when helpful.
- `Remaining placeholders`.
- `Claims needing data/citation`.

Read `references/polish-checklist.md` for the checklist.
