---
name: sci-citation-control
description: Evidence, reference, and citation management for SCI manuscripts. Use when the user asks to find or verify references, build a claim-evidence map, decide where citations belong, audit unsupported claims, format references for a target journal, compare citation behavior in benchmark papers, manage DOI/PMID/BibTeX metadata, cite supplementary materials, or prevent fabricated/outdated/irrelevant citations.
---

# SCI Citation Control

## Overview

Control the relationship between claims, evidence, and references. Prevent fabricated citations, unsupported statements, weak literature framing, and target-journal citation-style errors.

## First Move

Classify the user's need:

- `Claim audit`: identify what needs support.
- `Reference discovery`: find suitable sources for specific claims.
- `Reference verification`: confirm DOI, PMID, journal, year, metadata, retraction/status, and relevance.
- `Citation placement`: decide where citations belong.
- `Style adaptation`: match target journal reference and supplement citation style.
- `Bibliography cleanup`: normalize, deduplicate, and flag stale or irrelevant sources.

Use current web or database verification when real references, current status, retractions, or exact metadata matter. Do not invent citations.

## Minimum Inputs

Accept a draft paragraph, claim list, result-to-claim matrix, literature evidence map, DOI/PMID/BibTeX list, or target-journal citation style. If references are placeholders, keep them as `[CITE: claim]` until verified.

## Evidence Matching

For each claim, assign the support type:

- User data or figure/table.
- Primary literature.
- Review/meta-analysis.
- Method/tool/database/software citation.
- Guideline/reporting standard.
- No citation needed.
- Unsupported or unverifiable.

Prefer primary papers for precise claims. Use reviews for broad framing unless the journal convention says otherwise.

## Workflow

1. Build a claim inventory.
2. Identify needed evidence type for each claim.
3. Verify citation candidates using DOI/PMID/official article pages when possible.
4. Place citations next to the claims they support.
5. Flag weak clusters, outdated reviews, missing primary sources, retractions, preprints used as definitive evidence, and metadata mismatches.
6. Adapt reference style only after target-journal requirements are known.

## Output Contract

Return:

- `Claim-evidence-citation map`.
- `Unsupported claim list`.
- `Reference candidates` with DOI/PMID/URL and relevance notes.
- `Citation placement plan`.
- `Journal style notes`.
- `Risk flags`.
- `Final citation audit`.

Read `references/citation-audit-schema.md` for templates.
