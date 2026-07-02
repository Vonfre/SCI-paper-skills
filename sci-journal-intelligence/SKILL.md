---
name: sci-journal-intelligence
description: DEPRECATED. Do not use for new work. Replaced by sci-journal-landscape in the final SCI manuscript workflow.
---

# SCI Journal Intelligence

## Overview

Build an evidence-backed dossier for a target journal before manuscript planning. This skill owns journal identity, policy verification, author requirements, fit risks, and benchmark-paper discovery.

## First Move

If the target journal is missing, ask for it first. If the name is ambiguous, resolve exact identity using title, publisher, ISSN/eISSN, official website, and submission system.

Use current web research for journal facts. Journal policies, impact factors, indexing, APCs, OA status, and author guidelines change; do not rely on memory.

Ask at most three missing-context questions at a time:

- Article type or intended output.
- Research field/topic and main methods.
- Core novelty or main finding.

## Source Priority

1. Official journal and publisher pages.
2. Official author instructions, editorial policies, submission system, PDF templates, and checklists.
3. Authoritative metrics/indexing sources such as Clarivate/JCR when available, PubMed/MEDLINE, Web of Science/SCIE claims, Scopus/CiteScore, DOAJ, Crossref, ISSN Portal, and SCImago.
4. Recent article pages, full-text HTML/PDF, supplements, and journal issue archives.

Always include source links and retrieval dates. If a metric, indexing claim, APC, or acceptance rate cannot be verified, mark it as unverified.

## Workflow

1. Resolve journal identity.
   - Confirm exact title, publisher/society, ISSN/eISSN, official domain, journal family, and submission system.
   - Flag lookalikes, fake impact-factor claims, inconsistent ISSNs, missing editorial boards, or suspicious domains.

2. Capture positioning.
   - Summarize aims and scope, audience, article types, editorial priorities, novelty threshold, disciplinary boundaries, and likely desk-rejection risks.

3. Verify metrics and publication model.
   - Record impact factor/year/source if available, CiteScore/SJR/quartile if useful, indexing, OA/hybrid/subscription status, APC amount, currency, license options, waivers, and preprint/data policies.

4. Extract author requirements.
   - Capture article-type limits, word counts, abstract format, section order, figures/tables, references, supplements, ethics, data/code statements, AI-use policies, reporting guidelines, declarations, and file requirements.

5. Find benchmark papers.
   - Select 3-8 recent accessible same-journal papers from the same or closest topic.
   - Prefer the last 1-3 years, same article type, similar methods, similar system/population/material, or similar translational/mechanistic claim.
   - Hand papers to `sci-paper-reading` for deep deconstruction when the user needs structure and style modeling.

6. Deliver a target journal dossier.
   - Include a fit verdict, mandatory constraints, opportunities, risks, benchmark-paper list, and next-step recommendation.

## Output Contract

Produce:

- `Journal identity`: exact title, publisher, ISSN/eISSN, official URLs.
- `Positioning`: scope, audience, article types, novelty expectations.
- `Metrics and indexing`: verified values with source and year.
- `OA/APC`: model, costs, licenses, waivers, source.
- `Author requirements`: concrete constraints that affect writing/submission.
- `Benchmark candidates`: papers with DOI/URL and why included.
- `Fit risks`: reasons for desk rejection and fixes.
- `Next handoff`: usually `sci-paper-reading` or `sci-manuscript-architecture`.

Read `references/dossier-schema.md` for the detailed dossier template.
