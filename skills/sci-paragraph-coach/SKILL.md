---
name: sci-paragraph-coach
description: Paragraph-level coaching for SCI manuscript writing. Use when a user does not know how to write an Introduction, Results, Discussion, Abstract, figure legend, or cover-letter paragraph; provide paragraph purpose, evidence needs, citation needs, target-journal figure/table/supplement callout handling, sentence-by-sentence scaffold, example wording, and feedback on user drafts.
---

# SCI Paragraph Coach

## Overview

Coach one paragraph or paragraph type at a time. Make the paragraph do one job, carry the right evidence, and connect to the manuscript logic.

## First Move

Ask for the paragraph type if missing:

- Introduction background/gap/objective.
- Results evidence paragraph.
- Discussion interpretation/limitation/implication.
- Abstract sentence block.
- Figure legend.
- Cover-letter fit paragraph.

Ask for data, figure, claim, and citation only when they are needed for that paragraph.

## Paragraph Patterns

- Introduction: broad field context -> source-backed known mechanisms -> unresolved boundary -> exact scientific question -> study objective.
- Results: purpose -> method/comparison -> direct observation -> quantification/statistics/control -> short reliability or transition bridge.
- Discussion: principal finding -> relation to literature -> mechanism or model -> alternative explanation -> implication -> limitation/future work.
- Figure legend: what was tested -> what is shown -> sample/statistics -> abbreviations.
- Cover letter: fit to journal -> contribution -> why readers care.

## Paragraph Jobs

A paragraph should do one job:

- Background: establish known context.
- Gap: show what remains unknown.
- Objective: state what this study tests or provides.
- Result: present evidence before interpretation.
- Discussion: interpret results against literature.
- Limitation: define scope without undermining the paper.
- Transition: move the reader to the next claim.

## Workflow

1. Define the paragraph purpose.
2. List required evidence and citations.
3. Create a sentence-by-sentence scaffold.
4. Check whether the paragraph has enough evidence density for its section type.
5. Apply `journal_format_profile` for figure/table/supplement callouts or mark the format rule as `[NEED: target-journal figure/table callout style]`.
6. Write an example paragraph using placeholders when facts are missing.
7. If the user provides a draft, diagnose issue, explain why it hurts, and revise.

## Teaching Rule

For novice users, give a scaffold first, then a filled example, then one sentence explaining why the logic works. Avoid only returning polished text.

## State Coupling

Consume:

- `storyline.section_registry`, target `section_id`, draft paragraph if available, and linked `claim_id`, `figure_id`, and `source_id` values.
- `claim_registry` for safe wording and claim strength.
- `journal_landscape.journal_format_profile` when the paragraph cites figures, tables, supplements, legends, or headings.

Update:

- `draft_registry.sections` for the coached paragraph.
- `draft_registry.open_needs`, `open_citations`, and high-risk claim IDs.
- Format placeholders when paragraph-level callout style is unknown.
- Section status: `skeleton`, `drafted`, or `needs evidence`.

Block:

- If the paragraph lacks purpose, claim, evidence, or citation need, produce a scaffold before prose.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Paragraph type`.
- `Purpose`.
- `Required inputs`.
- `Sentence scaffold`.
- `Example paragraph` or `Revised paragraph`.
- `Why this works`.
- `Format note` when figure/table/supplement callouts appear.
- `Remaining placeholders`.

Read `references/paragraph-coach-template.md` for the template.
