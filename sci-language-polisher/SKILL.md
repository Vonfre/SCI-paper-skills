---
name: sci-language-polisher
description: Final scientific-language polishing for SCI manuscripts. Use when the user has draft text and wants clearer, more precise, journal-appropriate English or Chinese-to-English polishing; improve logic, concision, transitions, claim strength, hedging, terminology, abstract flow, results wording, discussion tone, cover letters, and reviewer responses without changing the scientific meaning or inventing evidence.
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
- If only expression, clarity, concision, tone, or idiomatic English is weak, continue polishing.

## Workflow

1. Identify paragraph/section purpose and claim strength.
2. Remove ambiguity, redundancy, vague verbs, and unsupported superlatives.
3. Improve transitions and sentence order when logic is local.
4. Return before/after examples for recurring problems when useful.
5. Flag claims that still need data, citation, or upstream logic repair.

## Polishing Rule

Do not silently strengthen claims. If a sentence changes from association to mechanism, mechanism to causality, or observation to application, flag it and provide a safer alternative.

## State Coupling

Consume:

- `draft_registry.sections`, source text, `claim_registry`, `citation_audit`, and target-journal tone/style when available.

Update:

- `draft_registry.sections[].draft_status` to `polished` only when meaning is stable.
- `draft_registry.high_risk_claim_ids` when polishing reveals overclaiming.
- A meaning-change log that lists any softened or preserved claims by `claim_id`.

Block:

- If meaning, evidence, or citation support is unstable, do not present the text as final-polished. Route to claim or citation repair.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Polished text`.
- `Meaning preservation note`.
- `Claim-strength changes`.
- `Before -> after examples` when helpful.
- `Remaining placeholders`.
- `Claims needing data/citation`.

Read `references/polish-checklist.md` for the checklist.
