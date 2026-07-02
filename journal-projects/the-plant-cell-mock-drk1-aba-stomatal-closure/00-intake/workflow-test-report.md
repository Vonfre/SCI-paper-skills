# Workflow Test Report

## Test Scenario

Target journal: The Plant Cell

Mock project: DRK1 promotes ABA-induced stomatal closure by ubiquitinating ABI1 in Arabidopsis.

Test purpose: Stress-test the SCI skills suite with invented data while preserving real target-journal constraints.

## Modules Exercised

| Stage | Module | Result |
|---|---|---|
| Intake | `sci-journal-paper` | Passed: created full project structure and stage handoffs |
| Journal intelligence | `sci-journal-intelligence` | Passed: Plant Cell dossier and desk-rejection risks recorded |
| Paper reading | `sci-paper-reading` | Partially passed: mock benchmark archetypes generated; real same-journal papers still required |
| Manuscript architecture | `sci-manuscript-architecture` | Passed: story spine, article type, figure plan, and claim tree generated |
| Citation control | `sci-citation-control` | Passed with warning: unsupported claims and citation needs were flagged instead of fabricating references |
| Writing | `sci-paper-writing` | Passed: mock title, abstract, outline, limitations, and supplement plan generated |
| Submission/revision | `sci-submission-revision` | Passed: readiness verdict, blocking issues, and mock cover letter generated |

## What Worked

- The workflow correctly refused to treat mock data as submission-ready.
- The Plant Cell fit logic emphasized mechanism, conceptual advance, and main-figure evidence.
- The claim tree exposed which claims require data, citation, or softer wording.
- Citation control avoided fake DOI/reference generation.
- Submission readiness separated structural progress from real blocking issues.

## What Still Needs Real Inputs

- Real target research topic and organism/species.
- Real gene/protein/material identifiers.
- Real raw data, figures, replicate counts, statistical tests, P values, effect sizes.
- Public repository accession numbers for omics or large-scale datasets.
- Verified references with DOI/PMID metadata.
- Real same-journal benchmark papers from the same field.
- Author list, affiliations, ORCID, funding, conflict statement, data/material availability.

## Skill Improvements Suggested By This Test

1. Add a journal-specific "high-bar desk rejection rubric" reference for top-tier journals.
2. Add a script that creates a `workflow-test-report.md` automatically.
3. Add a benchmark-paper search log template that separates real papers from mock archetypes.
4. Add a citation metadata checker script for DOI/PMID/BibTeX validation.
5. Add figure-readiness scoring for Plant Cell-style main-figure vs supplement decisions.
