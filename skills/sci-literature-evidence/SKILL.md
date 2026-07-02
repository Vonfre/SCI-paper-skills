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

## Research Question Planning

Before summarizing the literature, convert the task into a small question set:

- One question for direct support of the user's claim.
- One question for conflicting or alternative explanations.
- One question for novelty boundary and prior similar work.
- One question for methods, controls, datasets, or model-system precedent.
- One target-journal framing question when a journal is known.

Record these in a source ledger so the final recommendation is traceable.

## Citation Role Control

Explain whether each source is useful for background framing, gap identification, claim support, alternative explanation, method precedent, or discussion comparison. Do not treat one review as direct evidence for a precise mechanism when a primary paper is needed.

## Introduction Evidence Ladder

When literature will feed an Introduction, build a ladder rather than a flat bibliography:

1. Field background and journal-relevant stakes.
2. Established mechanisms, models, or consensus.
3. Competing explanations, unresolved boundaries, or missing controls.
4. The exact scientific question the manuscript answers.
5. Why the user's approach is able to answer that question.

Assign each source to one rung. Prefer multiple primary papers plus one or two reviews for framing. If an Introduction paragraph has no source role, mark it as under-supported.

## Evidence Grading

- `Strong`: direct primary evidence plus user data can plausibly support the claim.
- `Moderate`: related evidence exists but controls, mechanism, or context remain incomplete.
- `Weak`: only indirect or neighboring literature supports the idea.
- `Conflicting`: credible literature suggests an alternative explanation.
- `Unknown`: search coverage is insufficient.

## State Coupling

Consume:

- `project`, `journal_landscape`, existing `claim_registry`, and any user questions/conclusions.
- Existing `source_ledger` to avoid duplicate source IDs.

Update:

- `source_ledger.research_questions` and `source_ledger.sources` with stable IDs `S#`.
- Literature support, conflict, novelty boundaries, and source confidence.
- `claim_registry.claims[].citation_needs`, `evidence_needed_for_stronger_claim`, and status when claims already exist.

Block:

- If sources are unverified or only indirectly related, mark the evidence level and do not allow strong novelty/mechanism wording.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Research question matrix`.
- `Source ledger` with source role, metadata status, evidence location, and confidence.
- `Evidence map` for each user question or conclusion.
- `Introduction evidence ladder` when drafting or improving an Introduction.
- `Support/conflict summary`.
- `Gap assessment`.
- `Writing recommendation`: safe wording, citations needed, or claim to avoid.
- `Next module`: usually `sci-result-to-claim`, `sci-core-story-finder`, or `sci-citation-control`.

Read `references/evidence-map-schema.md` for templates.
Read `references/source-ledger-template.md` when source tracking, novelty checks, or contradiction checks are needed.
