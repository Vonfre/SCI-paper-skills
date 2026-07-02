---
name: sci-storyline-planner
description: Manuscript logic and storyline planning for SCI papers. Use when the user asks how to organize the paper, has or lacks a proposed writing logic, wants alternative result-order plans, needs to arrange several key cases/figures, or wants to imitate how comparable literature structures the argument before drafting.
---

# SCI Storyline Planner

## Overview

Turn literature findings, user conclusions, and key cases into a manuscript logic. This module decides the order of the argument before any full draft is written.

## First Move

Ask whether the user already has a preferred logic:

- If yes: request the current outline or key cases and improve the order.
- If no: use journal landscape and literature evidence to propose multiple logic plans.

Ask for the key cases/figures only if the user has data. If not, propose evidence modules needed for each plan.

## Workflow

1. Identify available story materials.
   - Journal landscape, literature evidence, result-to-claim matrix, core story memo, figure story map, conclusions, figures, cases, methods, and benchmark paper patterns.

2. Choose storyline type.
   - Mechanism-first.
   - Phenotype-to-mechanism.
   - Resource-to-validation.
   - Method-to-application.
   - Clinical/cohort-to-mechanism.
   - Comparative/evolutionary.

3. Generate plans.
   - If the user has no plan, give 2-4 plausible structures with pros/cons.
   - If the user has a plan, reorganize it and flag weak transitions.

4. Map figures/cases.
   - Decide which case is main text, supplementary, or not needed.
   - Keep target-journal constraints in view.

5. Create writing briefs.
   - Give paragraph-level or subsection-level instructions for `sci-draft-mimic` and `sci-paragraph-coach`.

6. Hand off risks.
   - Send weak transitions, overclaims, and missing controls to `sci-reviewer-simulator`.

## Output Contract

Produce:

- `Recommended storyline`.
- `Alternative plans`.
- `Figure/case order`.
- `Transition logic`.
- `Weak links and missing evidence`.
- `Drafting brief`.

Read `references/storyline-plan-schema.md` for templates.
