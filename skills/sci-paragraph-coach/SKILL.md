---
name: sci-paragraph-coach
description: Paragraph-level coaching and paragraph-plan enforcement for SCI manuscript writing. Use when a user does not know how to write an Introduction, Results, Discussion, Abstract, figure legend, or cover-letter paragraph; when paragraph counts need planning or repair; or when a Results subsection should be kept to 2-3 natural paragraphs. Provide paragraph purpose, paragraph index/role, evidence needs, citation needs, target-journal figure/table/supplement callout handling, sentence-by-sentence scaffold, example wording, and feedback on user drafts.
---

# SCI Paragraph Coach

## Overview

Coach one paragraph or paragraph type at a time. Make the paragraph do one job, carry the right evidence, and connect to the manuscript logic.
Use the paragraph plan to decide whether the paragraph should exist, merge, split, or move to another section.

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

## Paragraph Count Rules

- Check `storyline.paragraph_plan` before coaching a paragraph inside a full section.
- Abstract should usually be 1 paragraph unless the journal requires structured headings.
- Introduction should usually be 4 paragraphs for concise Nature Communications/PNAS-like articles.
- Results subsections should usually be 2-3 natural paragraphs: setup/purpose, evidence/statistics/figure support, and bridge/limited interpretation.
- Discussion should usually be 3-4 paragraphs for concise articles.
- If the user's draft exceeds the planned count, recommend merge/split/move actions before polishing sentences.

## Workflow

1. Define the paragraph purpose.
2. Locate it in the paragraph plan: section, paragraph index, target paragraph count, and paragraph job.
3. List required evidence and citations.
4. Create a sentence-by-sentence scaffold.
5. Check whether the paragraph has enough evidence density for its section type.
6. Apply `journal_format_profile` for figure/table/supplement callouts or mark the format rule as `[NEED: target-journal figure/table callout style]`.
7. Write an example paragraph using placeholders when facts are missing.
8. If the user provides a draft, diagnose issue, explain why it hurts, and revise.

## Teaching Rule

For novice users, give a scaffold first, then a filled example, then one sentence explaining why the logic works. Avoid only returning polished text.

## State Coupling

Consume:

- `storyline.section_registry`, `storyline.paragraph_plan`, target `section_id`, paragraph index/role, draft paragraph if available, and linked `claim_id`, `figure_id`, and `source_id` values.
- `claim_registry` for safe wording and claim strength.
- `journal_landscape.journal_format_profile` when the paragraph cites figures, tables, supplements, legends, or headings.

Update:

- `draft_registry.sections` for the coached paragraph.
- `draft_registry.open_needs`, `open_citations`, and high-risk claim IDs.
- Format placeholders when paragraph-level callout style is unknown.
- Paragraph-plan status: within count, over count, under-evidenced, merge/split/move needed.
- Section status: `skeleton`, `drafted`, or `needs evidence`.

Block:

- If the paragraph lacks purpose, claim, evidence, or citation need, produce a scaffold before prose.
- If the requested paragraph would exceed the planned count, explain the structural fix before writing another paragraph.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Paragraph type`.
- `Purpose`.
- `Paragraph plan position`.
- `Required inputs`.
- `Sentence scaffold`.
- `Example paragraph` or `Revised paragraph`.
- `Why this works`.
- `Format note` when figure/table/supplement callouts appear.
- `Remaining placeholders`.

Read `references/paragraph-coach-template.md` for the template.
