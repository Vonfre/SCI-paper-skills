---
name: sci-core-story-finder
description: Identify the central scientific story for an SCI manuscript. Use when a user has scattered results, several possible conclusions, weak narrative confidence, or does not know what the paper is really about; generate story options, choose the best angle for the target journal, and define the one-sentence takeaway.
---

# SCI Core Story Finder

## Overview

Find the manuscript's center of gravity. Convert scattered results into one memorable, evidence-bounded scientific story that fits the target journal or explicitly names the mismatch.

## First Move

Ask up to three missing items:

1. What are the strongest 3-5 results or claims?
2. What is the target journal or journal level?
3. What broader problem or gap should the work address?

If results are messy, first ask for a rough bullet list; do not force a polished abstract.

## Story Selection Criteria

Compare candidate stories by:

- Evidence strength.
- Novelty and field relevance.
- Target-journal fit.
- Audience breadth.
- Risk of overclaiming.
- Writing feasibility with available data.

The recommended story is not always the flashiest result; it is the best-supported publishable argument.

## Story Types

Classify candidate stories before choosing:

- Mechanism: explains how X controls Y through Z.
- Resource: provides a dataset, atlas, germplasm, platform, or benchmark.
- Method: introduces or validates a technique, workflow, or tool.
- Phenotype: reports an important biological, clinical, ecological, or material pattern.
- Application: improves prediction, diagnosis, engineering, treatment, or management.
- Comparative/evolutionary: explains differences across species, populations, tissues, or conditions.

## Workflow

1. Generate 2-4 possible story angles.
2. Write a one-sentence takeaway for each.
3. Score each angle by evidence, fit, risk, and feasibility.
4. Choose one central story and one backup story.
5. Define what belongs in the main text, supplement, or later paper.

## Recommendation Rule

Give a clear recommendation. Do not leave the user with equal options unless the evidence is genuinely tied. Include a backup story for a lower-risk journal, shorter manuscript, or reduced evidence package.

## Output Contract

Return:

- `Candidate stories`.
- `Recommended core story`.
- `Backup story`.
- `Manuscript boundary`.
- `Next step`: usually `sci-figure-story-builder` or `sci-storyline-planner`.

Read `references/story-decision-memo.md` for the template.
