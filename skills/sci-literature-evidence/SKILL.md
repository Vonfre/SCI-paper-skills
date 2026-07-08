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
- Dataset descriptor papers, repository records, benchmark papers, and software/model papers when datasets or computational resources affect the claim.
- Recent reviews for field framing, not as sole proof for precise claims.
- Same-journal or same-level papers when journal fit matters.
- Official database records for DOI/PMID, accession, version, license/access route, companion paper, and retraction/status checks when available.

Do not answer related-paper or seminal-paper requests from memory alone when real citations will enter the manuscript. Resolve DOI/PMID/URL metadata through available scholarly or repository sources before treating a source as verified.

## Related-Paper And Dataset Context

When the task asks for related papers, comparable papers, source datasets, benchmark resources, or dataset companion papers, use a retrieval-first map rather than a reading list:

1. Run topic, organism/system, method, dataset/accession, and target-journal query variants.
2. For the most relevant papers, inspect reference and citation neighborhoods when available to recover foundational work, recent extensions, contradictions, and uptake.
3. Separate source roles: direct claim support, conflicting evidence, method precedent, dataset descriptor, benchmark comparator, journal-style model, background review, or discussion boundary.
4. Link dataset records to companion papers and claim IDs when datasets affect user claims.
5. Synthesize what the paper set collectively establishes, contests, or leaves open; do not summarize one paper per bullet unless the output is explicitly a ledger.

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
- Literature support, conflict, novelty boundaries, related-paper roles, dataset companion-paper links, and source confidence.
- `claim_registry.claims[].citation_needs`, `evidence_needed_for_stronger_claim`, and status when claims already exist.

Block:

- If sources are unverified or only indirectly related, mark the evidence level and do not allow strong novelty/mechanism wording.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Research question matrix`.
- `Source ledger` with source role, metadata status, evidence location, and confidence.
- `Related-paper map` when the user asks for comparable papers, seminal papers, citation context, dataset companion papers, or method/dataset precedent.
- `Dataset-source links` when public datasets, benchmark resources, or repository records affect the claim.
- `Evidence map` for each user question or conclusion.
- `Introduction evidence ladder` when drafting or improving an Introduction.
- `Support/conflict summary`.
- `Gap assessment`.
- `Writing recommendation`: safe wording, citations needed, or claim to avoid.
- `Next module`: usually `sci-result-to-claim`, `sci-core-story-finder`, or `sci-citation-control`.

Read `references/evidence-map-schema.md` for templates.
Read `references/source-ledger-template.md` when source tracking, novelty checks, or contradiction checks are needed.
