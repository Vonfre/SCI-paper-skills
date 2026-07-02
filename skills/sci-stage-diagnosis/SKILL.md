---
name: sci-stage-diagnosis
description: Diagnose where a novice SCI manuscript project is stuck and choose the next best action. Use when the user has no clear workflow, feels unable to write despite having results, does not know whether to do literature search, story planning, figure organization, drafting, polishing, submission checks, or reviewer-response work.
---

# SCI Stage Diagnosis

## Overview

Tell the user what stage they are really in and what to do next. Prevent premature drafting when the story, evidence, journal fit, or claim boundaries are not ready.

## Diagnosis Questions

Ask no more than three:

1. Do you have a target journal or target level?
2. What do you already have: data/figures, conclusions, outline, draft, or reviewer comments?
3. What feels stuck: literature, claims, story, figure order, wording, citations, submission, or revision?

If the user gives partial context, diagnose from it and mark missing facts as `[NEED: ...]`.

## Diagnosis Logic

Classify by the earliest missing foundation:

- No target journal/level and no clear output -> start with intake.
- Results exist but conclusion strength is unclear -> result-to-claim first.
- Conclusions exist but literature support is unknown -> literature evidence first.
- Claims exist but no central message -> core story first.
- Story exists but figures are unordered -> figure story first.
- Story and figure order exist but no section logic -> storyline planning first.
- Logic exists but no text -> draft mimic or paragraph coach.
- Text exists but claims/citations are risky -> reviewer simulator or citation control.
- Text is logically sound but expression is weak -> language polisher.
- Manuscript is near final or decision letter exists -> submission revision.

## Stage Labels

- `No intake`: journal, field, material, or goal is missing.
- `Journal unknown`: target journal fit and comparable papers are unknown.
- `Evidence unknown`: literature support or conflict is unknown.
- `Claim unclear`: results exist but defensible claims are not defined.
- `Story unclear`: claims exist but no central manuscript message is chosen.
- `Figure logic unclear`: figures/cases exist but the reader path is weak.
- `Draft not ready`: story or evidence gaps block drafting.
- `Draft repair`: a draft exists but structure, claims, or paragraphs need work.
- `Final polish`: meaning is stable and expression/citation/style remain.
- `Submission/revision`: journal files, cover letter, or reviewer response are needed.

## Decision Rules

- Recommend only one next primary module.
- Do not recommend full drafting if claims or figure order are still unclear.
- If two stages are plausible, choose the earlier blocker and explain the tradeoff.
- Give the user one concrete 30-minute task, not a long wishlist.

## Do-Not-Do-Yet Guidance

Every diagnosis must name one premature action to avoid, for example:

- Do not draft the abstract before the central claim is known.
- Do not polish language before unsupported claims are fixed.
- Do not choose a high-impact target before evidence depth is assessed.
- Do not add citations randomly before claims are decomposed.

## State Coupling

Consume:

- User request and any existing `manuscript_state`.
- Existing `project`, `current_stage`, `global_blockers`, and `next_skill` fields if provided.

Update:

- `manuscript_state.current_stage`.
- `manuscript_state.global_blockers`.
- `manuscript_state.next_skill`.
- `project.missing_inputs` when the diagnosis reveals missing intake fields.

Block:

- If no topic, material, goal, or artifact is available, route to `sci-intake-router` and ask only the next useful intake questions.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Current stage`.
- `Why this is the stage`.
- `Do not do yet`.
- `Next best action`.
- `Route`: next skill, input needed, expected output.
- `30-minute task for user`.
- `Missing information`.

Read `references/stage-diagnosis-template.md` for the template.
