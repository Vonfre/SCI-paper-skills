---
name: sci-manuscript-architecture
description: DEPRECATED. Do not use for new work. Replaced by sci-result-to-claim, sci-core-story-finder, sci-figure-story-builder, and sci-storyline-planner.
---

# SCI Manuscript Architecture

## Overview

Design the manuscript before writing. This skill turns journal intelligence, benchmark patterns, and the user's results into a clear scientific story, claim hierarchy, section plan, figure/table sequence, and writing brief.

## Required Inputs

Prefer these inputs before architecture work:

- Target journal dossier from `sci-journal-intelligence`.
- Benchmark matrix or article cards from `sci-paper-reading`.
- User's research topic, article type, main findings, methods, figures/tables, and constraints.

If inputs are incomplete, proceed with explicit `[NEED: ...]` placeholders and a missing-input list.

## Workflow

1. Establish the fit frame.
   - State the target article type, audience, journal-specific value, and desk-rejection risks.

2. Define the contribution.
   - Write a positioning sentence: problem, gap, approach, main finding, and why the journal's readers should care.

3. Build the story spine.
   - Problem -> gap -> objective/hypothesis -> approach -> result sequence -> interpretation -> significance.

4. Build the claim tree.
   - Separate main claim, subclaims, data-supported claims, literature-supported claims, speculative implications, and unsupported gaps.

5. Plan the figure/table sequence.
   - Assign each figure/table a question, evidence type, narrative role, required statistics, and supplement links.
   - Check whether the journal favors mechanism-first, phenotype-first, cohort-first, method-first, or validation-first sequencing.

6. Create the section outline.
   - Title options, abstract architecture, introduction paragraph plan, result subsection order, discussion moves, methods requirements, declarations, and supplement plan.

7. Hand off.
   - Send claim tree to `sci-citation-control`.
   - Send section briefs to `sci-paper-writing`.
   - Send supplement and submission constraints to `sci-submission-revision`.

## Output Contract

Produce:

- `Fit frame`: target journal, article type, audience, and risks.
- `Positioning statement`: one precise contribution sentence.
- `Story spine`: the manuscript's argument path.
- `Claim tree`: claims mapped to evidence and citation needs.
- `Figure/table plan`: ordered narrative sequence.
- `Section blueprint`: paragraph-level purpose for each section.
- `Missing inputs`: exact facts, data, or decisions needed before writing.

Read `references/architecture-canvas.md` for templates.
