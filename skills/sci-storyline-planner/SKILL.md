---
name: sci-storyline-planner
description: Manuscript logic and storyline planning for SCI papers. Use when the user asks how to organize the paper, has or lacks a proposed writing logic, wants alternative result-order plans, needs to arrange several key cases/figures, or wants to imitate how comparable literature structures the argument before drafting.
---

# SCI Storyline Planner

## Overview

Plan the manuscript's argument path before drafting. Compare possible result orders and choose the one that best teaches the reader, fits the target journal, and keeps claim strength honest.

## First Move

Ask whether the user already has a preferred logic:

- If yes, evaluate it against claims, figure order, and journal fit.
- If no, propose multiple logic plans using the journal landscape, evidence map, and figure story.

Ask for key cases/figures only if the user has data. If not, propose evidence modules needed for each plan.

## Logic Archetypes

Use or combine:

- Problem -> mechanism -> validation.
- Phenotype -> mechanism -> rescue/control.
- Cohort/resource -> discovery -> validation.
- Method -> benchmark -> biological/application insight.
- Case series -> shared pattern -> explanatory model.

## Planning Inputs

Use whichever artifacts exist:

- Journal landscape.
- Evidence map.
- Result-to-claim matrix.
- Core story memo.
- Figure story map.
- Comparable-paper patterns or user-provided PDFs.
- User's current outline or preferred logic.

If a required artifact is missing, make a provisional plan and mark the missing gate.

## Workflow

1. Define the central message and target audience.
2. Generate 2-3 storyline options.
3. Compare strengths, risks, and missing evidence.
4. Choose a recommended result order.
5. Produce a drafting brief for title, abstract, introduction, results, and discussion.

## Draft-Readiness Gate

Drafting is ready only if:

- Each result section answers one scientific question.
- Main figures support the central story in order.
- High-risk claims have evidence or are softened.
- Missing facts are visible as `[NEED: ...]`.

## Plan Quality Bar

A good plan should tell the user:

- Why this order is easier for readers.
- Which figure/case supports each subsection.
- Where citations are needed.
- Where the argument is weakest.
- What can be drafted now and what still needs evidence.

## State Coupling

Consume:

- `journal_landscape`, `source_ledger`, `claim_registry`, `story`, and `figure_registry`.
- User's existing outline or preferred logic if available.

Update:

- `storyline.result_order`.
- `storyline.section_registry` with stable IDs `SEC#`.
- `storyline.drafting_brief`, `draft_readiness`, and `draft_blockers`.
- Section-to-claim, section-to-figure, and section-to-source links.

Block:

- If no story or claim/figure map exists, create only a provisional structure and route to the missing upstream module.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Storyline options`.
- `Recommended plan`.
- `Core message`.
- `Result order`.
- `Main figures`.
- `Weak links`.
- `Drafting brief`.

Read `references/storyline-plan-schema.md` for templates.
