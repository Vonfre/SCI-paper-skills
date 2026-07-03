# Manuscript Outputs

## Contents

- Core Deliverables
- Writing Rules
- Section Guidance
- Supplementary-Material Strategy
- Cover Letter Skeleton
- Final Checklist

Use this reference after the journal landscape, evidence map, result-to-claim matrix, and storyline plan exist.

## Core Deliverables

For a full journal-specific writing engagement, produce these in order:

1. Fit verdict
   - Strong fit, conditional fit, risky fit, or poor fit.
   - One-paragraph rationale grounded in journal scope and comparable papers.
   - Desk-rejection risks and fixes.

2. Positioning statement
   - One sentence: problem, gap, approach, main finding, journal-relevant value.
   - Avoid inflated novelty claims unless the evidence supports them.

3. Story spine
   - Opening problem.
   - Precise knowledge gap.
   - Hypothesis or objective.
   - Key method.
   - Main result sequence.
   - Interpretation.
   - Journal-specific significance.

4. Article architecture
   - Target article type.
   - Proposed title options.
   - Abstract plan or full abstract.
   - Section headings and paragraph purposes.
   - Figure/table plan.
   - Journal-format strategy for in-text figure/table/supplement callouts, legends, headings, references, and statements.
   - Supplementary-material plan.
   - Reference strategy.

5. Submission package
   - Cover letter.
   - Highlights or significance statement if required.
   - Data availability, code availability, ethics, funding, conflict, author contribution, acknowledgments.
   - Reviewer suggestions/exclusions if requested.
   - Final compliance checklist.

## Writing Rules

- Do not invent sample sizes, statistical tests, approvals, datasets, accession numbers, references, or conclusions.
- Use `[NEED: ...]` placeholders for missing scientific facts.
- Use `[CITE: ...]` placeholders for citation needs that have not been verified.
- Match claim strength to evidence: association, prediction, regulation, mechanism, causality, validation, and application are different claims.
- Keep the journal voice, but do not copy phrases from benchmark papers.
- Preserve the user's scientific contribution; do not overfit to superficial style.
- Use `journal_landscape.journal_format_profile` when inserting figure, table, supplementary-material, legend, heading, reference, and back-matter text.
- For Chinese-to-English work, produce idiomatic scientific English rather than literal translation.

## Quality Bar

A manuscript is not full-draft quality until it passes five gates:

1. Introduction: literature-backed funnel from background to known mechanisms, unresolved gap, scientific question, and study objective.
2. Results: evidence-dense subsections with controls, quantification/statistics, figure links, and short transition or reliability sentences.
3. Discussion: result-anchored expansion into prior work, mechanism, alternative explanations, implications, limitations, and future experiments.
4. Methods: reproducible procedural detail, including materials, treatments, replicates, instruments/software, quantification, statistics, and data/code availability.
5. Journal format: in-text callouts, figure legends, table titles, supplementary-material naming, headings, references, and declarations match the target-journal profile or are explicitly marked unknown.

If one gate fails, produce a repair plan or placeholders instead of presenting the manuscript as complete.

## Section Guidance

### Title

Generate 5-10 title options when requested:

- Mechanistic title: `X regulates Y through Z in context W`.
- Translational title: `X predicts Y and identifies Z in population W`.
- Method title: `A method/tool/resource for X in Y`.
- Cautious descriptive title when evidence is preliminary.

Mirror the target journal's preference for colon titles, declarative titles, or noun-phrase titles only if observed in comparable papers.

### Abstract

Use the journal's required structure. If unstructured, write a single coherent paragraph with:

1. Context and gap.
2. Objective or hypothesis.
3. Methods and data.
4. Primary results with concrete evidence.
5. Interpretation and journal-relevant implication.

Do not include numbers unless supplied by the user or extracted from the user's materials.

### Introduction

Build 4-6 paragraphs unless comparable papers show a different norm:

1. Field-level problem and journal-relevant stakes.
2. What is known.
3. What remains unresolved.
4. Why current approaches are insufficient.
5. Study objective/hypothesis and design.
6. Concise contribution statement.

Avoid generic textbook openings when comparable papers move quickly to a precise gap.
Each paragraph should have a source role, and the gap should emerge from the literature rather than appearing as an unsupported assertion.

### Results

Each result subsection should have:

- Purpose sentence.
- Method or comparison.
- Main observation.
- Quantitative/statistical support.
- Link to figure/table/supplement.
- Short interpretive bridge to the next result.

Use comparable papers to decide whether the journal favors mechanism-first, phenotype-first, cohort-first, resource-first, or method-validation-first sequencing.
Use the target journal's exact callout style from `journal_format_profile`, such as `Fig. 1A`, `Figure 1A`, `Figs. 1 and 2`, `Supplementary Fig. 1`, or `Table S1`; never mix styles inside one manuscript.
Allow brief discussion-like transition sentences in Results only when they improve continuity or explain why the next experiment is needed.

### Discussion

Use 4-7 paragraphs:

1. Principal findings.
2. Relation to prior work.
3. Mechanistic, clinical, methodological, or theoretical implications.
4. Strengths.
5. Limitations, written plainly.
6. Future work.
7. Closing conclusion matched to evidence.

Discussion should expand outward from result IDs and source IDs, not drift into broad claims unsupported by the manuscript.

### Methods

Follow journal requirements exactly. Include enough detail for reproducibility:

- Samples, cohorts, organisms, materials, and inclusion/exclusion criteria.
- Experimental protocols or computational pipeline.
- Statistical analysis.
- Software versions.
- Data and code availability.
- Ethics and approvals.

For wet-lab work, include treatment dose/time, buffer/media conditions, instrument settings, replicate definitions, exclusion rules, normalization, and exact statistical model whenever known.

## Journal-Format Strategy

Before writing or revising target-journal text, build a compact normalization table:

| Element | Required Form | Example In Draft | Source Basis | Action |
|---|---|---|---|---|
| Main figure | | | official / benchmark / fallback / unknown | |
| Main figure panel | | | official / benchmark / fallback / unknown | |
| Main table | | | official / benchmark / fallback / unknown | |
| Supplementary figure/table/data | | | official / benchmark / fallback / unknown | |
| Figure legends/table titles | | | official / benchmark / fallback / unknown | |

Apply the table during drafting, not only at final submission. If the exact target-journal rule is unknown, use a clearly provisional style and mark `[NEED: target-journal figure/table callout style]`.

## Supplementary-Material Strategy

Extract the target journal's observed pattern from comparable papers:

- Naming: `Supplementary Fig. 1`, `Fig. S1`, `Supplementary Table 1`, `Table S1`, `Supplementary Data 1`, etc.
- Placement: parenthetical result citations, end-of-sentence citations, or methods-only citations.
- File organization: one PDF, separate Excel tables, separate datasets, videos, protocols, or source data files.
- Whether supplements include extended methods, raw data, uncropped blots, reporting checklists, or source data.

When drafting, use the journal's exact observed style and maintain a supplement inventory.

## Cover Letter Skeleton

```markdown
Dear [Editor Title/Name],

We are pleased to submit our manuscript, "[Title]," for consideration as a [Article Type] in [Journal].

In this study, we [one-sentence approach] and show that [main finding], addressing [specific gap] that is relevant to [journal audience/scope].

The manuscript may interest readers of [Journal] because [journal-specific fit based on scope and comparable papers].

Key contributions include:
1. [Contribution 1]
2. [Contribution 2]
3. [Contribution 3]

We confirm that the manuscript is original, is not under consideration elsewhere, and all authors have approved submission. [Add ethics/data/conflict statements as required.]

Sincerely,
[Corresponding Author]
```

## Final Checklist

- Journal and article type are exact.
- All mandatory statements are present.
- Figures/tables/supplements match limits and naming style.
- In-text figure/table/supplement callouts match the target-journal format profile.
- References match journal format and are not fabricated.
- Abstract, highlights, keywords, graphical abstract, and cover letter satisfy requirements.
- Data/code/ethics/reporting checklists are included when relevant.
- All placeholders are listed for the user.
