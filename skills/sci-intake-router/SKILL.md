---
name: sci-intake-router
description: First-step intake and routing for an adaptive SCI manuscript coaching workflow. Use when the user invokes SCI paper writing/help without enough context, especially inexperienced researchers who have results or conclusions but weak logic/expression; ask target journal, research field, research content, manuscript stage, available figures/results, and route to the correct next module.
---

# SCI Intake Router

## Overview

Start the workflow with the minimum useful questions, then route to the correct next skill. Avoid generic writing help by anchoring the project in journal target, research content, available materials, and current bottleneck.

## First Response

Ask only the missing high-impact items, up to three:

1. Target journal, candidate journals, or target level.
2. Research topic, field, organism/material/system, and main method.
3. Current materials: question, conclusions, figures/data, outline, draft, reviewer comments, deadline.

If the user answers partially, do not restart intake. Fill the brief with what is known and mark unknowns as `[NEED: ...]`.

## Minimum Useful Intake

Collect only what changes the next action:

- Target journal, candidate journals, or target level.
- Research topic, field, organism/material/system, and article type if known.
- Current materials: question, conclusions, figure list, result bullets, outline, draft, PDFs/model papers, deadline, or reviewer comments.

Do not request full methods, all raw data, author information, or final declarations during intake unless the user is already preparing submission.

## Routing Logic

- Target journal plus topic given -> `sci-journal-landscape`.
- No target journal but clear research direction -> `sci-literature-evidence` or `sci-stage-diagnosis`.
- Results/figures given but claims unclear -> `sci-result-to-claim`.
- Claims given but story unclear -> `sci-core-story-finder`.
- Figure inventory given -> `sci-figure-story-builder`.
- Draft given -> `sci-reviewer-simulator` for logic risk or `sci-language-polisher` for expression-only polish.
- Reviewer comments given -> `sci-submission-revision`.

## Intake Quality Gate

Before handing off, record enough context for the next module to start without re-asking basics:

- Target journal or journal level.
- Topic and model system/material.
- Current manuscript stage.
- Available artifacts.
- Desired output and deadline if any.
- Biggest uncertainty.

## Novice Guidance

After routing, explain why that stage comes next in one short paragraph. End with one concrete user task, such as:

- "List your 3-8 most important results, one sentence each."
- "Send the target journal and 5 keywords for comparable-paper search."
- "Paste your current abstract or figure legend for paragraph coaching."

## State Coupling

Consume:

- Existing `manuscript_state.project` if present.
- User-provided journal, topic, system, materials, stage, deadline, draft, PDFs, figures, or reviewer comments.

Update:

- `project.user_goal`, `target_journal`, `candidate_journals`, `target_level`, `article_type`, `topic`, `field`, `organism_material_system`, and `main_methods`.
- `project.available_artifacts` and `project.missing_inputs`.
- `manuscript_state.current_stage` and `next_skill`.

Block:

- If no topic/material/goal is known, do not route to literature, claim, or drafting modules. Keep intake open with a concrete user task.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return an `SCI workflow intake brief` with:

- `User goal`.
- `Available inputs`.
- `Missing inputs` grouped by downstream stage.
- `Route`: next skill, reason, first action.

Read `references/intake-brief-schema.md` for the template.
