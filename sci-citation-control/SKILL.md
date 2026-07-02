---
name: sci-citation-control
description: Evidence, reference, and citation management for SCI manuscripts. Use when the user asks to find or verify references, build a claim-evidence map, decide where citations belong, audit unsupported claims, format references for a target journal, compare citation behavior in benchmark papers, manage DOI/PMID/BibTeX metadata, cite supplementary materials, or prevent fabricated/outdated/irrelevant citations.
---

# SCI Citation Control

## Overview

Control the relationship between claims, evidence, and references. This skill prevents unsupported statements, fabricated citations, weak literature framing, and target-journal citation-style errors.

## First Move

Determine whether the task is:

- `Claim audit`: inspect manuscript claims and identify missing evidence.
- `Reference discovery`: find suitable sources for specific claims.
- `Reference verification`: confirm metadata, DOI, PMID, journal, year, and relevance.
- `Citation placement`: decide where citations belong in the manuscript.
- `Style adaptation`: match target journal reference and supplement citation style.
- `Bibliography cleanup`: normalize and flag duplicates, retractions, stale reviews, or irrelevant citations.

Use current web or database verification when real references, current status, retractions, or exact metadata matter. Do not invent citations.

## Workflow

1. Build a claim inventory.
   - Extract major background claims, method claims, result claims, mechanistic claims, translational claims, novelty claims, and limitation claims.

2. Classify evidence needs.
   - User data, figure/table, supplement, primary literature, review/meta-analysis, guideline, database, or no citation needed.

3. Verify or find references.
   - Prefer primary sources for factual claims and recent high-quality reviews for broad context.
   - Use DOI/PMID/official article pages when possible.
   - Flag retracted, superseded, predatory, off-topic, or low-relevance sources.

4. Place citations.
   - Put citations next to the claim they support.
   - Avoid citation clusters that hide weak support.
   - Match benchmark-paper behavior and target journal style.

5. Format and audit.
   - Adapt in-text citation style, reference list style, DOI/URL requirements, reference order, and supplement citation style.
   - Return a risk list before submission.

## Output Contract

Produce:

- `Claim-evidence-citation map`.
- `Unsupported claim list`.
- `Reference candidates` with DOI/PMID/URL and relevance notes.
- `Citation placement plan`.
- `Journal style notes`.
- `Risk flags`: missing primary source, outdated review, unsupported causality, unverifiable citation, metadata mismatch.

Read `references/citation-audit-schema.md` for templates.
