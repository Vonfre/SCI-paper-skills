---
name: sci-intake-router
description: First-step intake and routing for an adaptive SCI manuscript coaching workflow. Use when the user invokes SCI paper writing/help without enough context, especially inexperienced researchers who have results or conclusions but weak logic/expression; ask target journal, research field, research content, manuscript stage, available figures/results, and route to the correct next module.
---

# SCI Intake Router

## Overview

Start the workflow with the minimum useful questions, then route to the correct next skill. This module prevents generic writing and helps novice users understand what they should do next.

## First Response

If the user only says they want to write or submit an SCI paper, ask exactly these three questions:

1. What target journal do you want to submit to? If undecided, list 1-3 candidate journals or say the target level.
2. What is your research field/topic and model system?
3. What do you already have: scientific question only, results/figures, conclusions, outline, draft, or reviewer comments?

If the user provides some answers, ask only for the missing high-impact item. Do not ask for all metadata at once.

## Routing Logic

- User does not know where to start -> `sci-stage-diagnosis`.
- Target journal plus topic given -> `sci-journal-landscape`.
- Results/figures exist but claims are unclear -> `sci-result-to-claim`.
- Conclusions/scientific question need literature -> `sci-literature-evidence`.
- Multiple conclusions exist but no center -> `sci-core-story-finder`.
- Figures/cases exist but order is unclear -> `sci-figure-story-builder`.
- User asks how to arrange full manuscript logic -> `sci-storyline-planner`.
- User wants pre-submission criticism -> `sci-reviewer-simulator`.
- User wants initial draft from known logic/style -> `sci-draft-mimic`.
- User asks how to write a specific paragraph -> `sci-paragraph-coach`.
- User has text and wants final language improvement -> `sci-language-polisher`.
- User is preparing submission or revision -> `sci-submission-revision`.

## Output Contract

Produce an intake brief:

- Target journal/candidate level.
- Field/topic/model system.
- Current manuscript stage.
- Available conclusions/data/figures.
- User experience level if stated.
- Missing critical inputs.
- Next skill to run and why.

Read `references/intake-brief-schema.md` for the template.
