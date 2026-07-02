---
name: sci-paper-reading
description: DEPRECATED. Do not use for new work. Replaced by sci-journal-landscape and sci-draft-mimic in the final SCI manuscript workflow.
---

# SCI Paper Reading

## Overview

Turn scientific papers into reusable writing intelligence. This skill reads papers not only for content, but for structure, claims, figure logic, citation behavior, supplement use, and journal voice.

## Inputs

Accept:

- PDFs, full-text HTML, article URLs, DOIs, PubMed records, abstracts, supplementary files, or user-pasted text.
- A target journal dossier from `sci-journal-intelligence`.
- User topic keywords for selecting comparable papers.

If a specific paper/link is referenced and its contents were not provided, retrieve current source material when possible. If full text is unavailable, mark the analysis as abstract-only or metadata-only.

## Reading Modes

- `Fast triage`: decide whether a paper is relevant.
- `Article card`: extract one paper into a reusable structured note.
- `Benchmark matrix`: compare 3-8 same-journal papers.
- `Journal voice model`: infer title, abstract, introduction, results, discussion, figure, supplement, and citation conventions.
- `Method extraction`: isolate reusable methods, statistics, datasets, and reporting details.
- `Post-publication deconstruction`: learn from the user's final/accepted paper for future manuscripts.

## Workflow

1. Identify the reading goal.
   - Ask whether the user needs content summary, writing structure, journal-style benchmarking, method extraction, citation mining, or supplement analysis.

2. Capture bibliographic identity.
   - Title, journal, year, authors when useful, DOI, PMID if available, article type, URL/PDF availability.

3. Map article architecture.
   - Section order, heading pattern, abstract structure, result subsections, methods placement, declarations, supplements.

4. Extract the argument.
   - Problem, gap, hypothesis/objective, main evidence sequence, central claim, limitation framing, final implication.

5. Decode figures and tables.
   - For each figure/table: question answered, evidence type, panel logic, statistical support, and connection to the narrative.

6. Inspect citation and supplement behavior.
   - Citation density, primary vs review sources, where citations cluster, supplement naming, in-text supplement citation format, data/code/ethics statements.

7. Produce outputs.
   - For one paper: article card.
   - For multiple papers: benchmark matrix plus cross-paper patterns.
   - For manuscript planning: handoff notes to `sci-manuscript-architecture`, `sci-citation-control`, or `sci-paper-writing`.

## Output Contract

Always distinguish:

- What the paper actually says.
- What is inferred about the journal style.
- What is useful for the user's manuscript.
- What cannot be assessed due to unavailable full text/supplements.

Read `references/paper-deconstruction-schema.md` for article card and benchmark templates.
