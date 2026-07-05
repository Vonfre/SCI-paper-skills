---
name: sci-result-to-claim
description: Convert experimental or analytical results into defensible SCI manuscript claims. Use when a user has data, figures, tables, cases, observations, or conclusions but cannot tell what they prove, what they cannot prove, what evidence is missing, or how strongly each result can be written for a target journal.
---

# SCI Result To Claim

## Overview

Turn results into evidence-bounded claims. This module protects the manuscript from saying mechanism, causality, novelty, or application when the current data only support observation or association.

## First Move

Ask for results in the easiest available form:

- Figure/table list.
- Key observations.
- Current conclusions.
- Raw result bullets.
- Draft result paragraphs.
- Raw data files, analysis outputs, notebooks, statistical tables, or existing plots if claim strength depends on analysis.

If the user lacks polished figures, work from rough result descriptions and mark missing evidence.
If the user has raw data or unclear statistics rather than stable results, route to adjacent exploratory data analysis, statistical analysis, or domain-specific analysis skills before treating the result as claim-ready.

## Claim Ladder

Use the weakest accurate claim level:

1. `Descriptive`: X changes under Y.
2. `Association`: X correlates with Y.
3. `Regulation`: perturbing X changes Y.
4. `Mechanism`: X changes Y through Z.
5. `Causality`: X is necessary/sufficient under tested conditions.
6. `Application`: X improves a practical outcome or predicts utility.

## Minimum Input Format

Accept rough input. Convert any of these into a normalized result table:

- Figure list.
- Bullet-point observations.
- Draft result paragraphs.
- Figure legends.
- Conclusions without figures.
- PDF-derived or screenshot-derived figure descriptions when available.
- Algorithm, software, workflow, platform, or resource-construction descriptions when the result is a named artifact, module, interface, or inspectable output rather than a conventional measurement.

For each result, recover: condition, comparison, method, observation, quantification/statistics if known, sample size, replicate unit, effect/uncertainty, analysis provenance, named artifact/module/interface when relevant, and what the user thinks it proves.

## Workflow

1. List each result/figure and what it directly shows.
2. Separate direct observation from interpretation.
3. For algorithm, tool, workflow, platform, or resource-building sections, build a process-to-result map: each invisible action should produce a tangible result object such as a named graph, resolver, scoring layer, refinement module, interface, evidence report, dataset, or quality-control output.
4. Assign the strongest defensible claim and the claims it does not support.
5. Build the evidence package for each result: experimental design, controls, quantification, statistics, representative figure, replicate logic, analysis provenance, named artifact/module/interface, and relevant literature context.
6. Classify the result as confirmatory, exploratory, descriptive, methodological, resource-building, or not yet interpretable.
7. For non-ideal, mixed, or locally weaker results, define the boundary before drafting: affected count or subgroup, rank/margin/dispersion, likely data or design condition, whether it is comparator-specific, and why it does not overturn the main claim.
8. Identify the smallest missing control, analysis, diagnostic, effect-size report, artifact description, module definition, boundary explanation, or citation that would unlock a stronger claim.
9. Recommend safe wording, result-paragraph bridge language, and a next module.

## Claim Discipline

Use these boundaries:

- Observation: the data show a change or pattern.
- Association: two variables move together.
- Regulation: perturbing X changes Y.
- Mechanism: X changes Y through Z.
- Causality: X is necessary or sufficient under tested conditions.
- Application: X improves prediction, intervention, diagnosis, engineering, or practical outcome.

Do not allow phenotype-only data to become a mechanism claim. Do not allow correlation to become causation. Do not allow one model system to become a universal statement without support.
Do not allow p-values alone to carry a strong claim. Require direction, effect or estimate, uncertainty, sample size, replicate unit, and appropriate statistical/model assumptions whenever the claim depends on quantitative analysis.
For tool or algorithm results, do not present a procedural step as if it were validation. State what the step produced, such as an evidence graph, label resolver, candidate-gene module, online interface, agent-callable wrapper, output table, or audit trail, and reserve performance claims for benchmark or validation data.

## State Coupling

Consume:

- User result descriptions, figure/table inventory, draft result paragraphs, and existing `figure_registry` if available.
- `analysis_registry` when data provenance, preprocessing, statistics, or computational workflow status already exists.
- `journal_landscape` and `source_ledger` when they exist.

Update:

- `analysis_registry.datasets` and `analysis_registry.statistical_plan` when analysis provenance, statistical status, or diagnostics are part of the claim.
- `claim_registry.claims` with stable IDs `C1`, `C2`, `C3`.
- `linked_result_or_figure_ids`, `claim_level`, `safe_wording`, `stronger_wording_if_fixed`, `evidence_needed_for_stronger_claim`, `citation_needs`, and `status`.
- `global_blockers` for missing decisive controls, statistics, validation, or user data.

Block:

- If no result, observation, figure, or draft result text is available, route back to intake or ask for a result list.
- If analysis-derived results lack provenance, sample size/replicate unit, appropriate statistical test/model, or diagnostic status, mark claims provisional and route to analysis repair before drafting.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Result-to-claim matrix`.
- `Evidence package table`.
- `Analysis provenance and statistical status`.
- `Process-to-result map` when method, software, platform, workflow, or resource-building content lacks conventional figure/data support.
- `Result paragraph bridge notes`.
- `Claim-strength summary`.
- `Evidence gaps` ranked by importance.
- `Safe wording` and `stronger wording if fixed`.
- `Next module`: usually `sci-core-story-finder`, `sci-figure-story-builder`, or `sci-citation-control`.

Read `references/result-claim-matrix.md` for the output template.
