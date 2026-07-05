# Manuscript Outputs

## Contents

- Core Deliverables
- Writing Rules
- Section Guidance
- Paragraph And Word Output Planning
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
   - Section headings, paragraph counts, and paragraph purposes.
   - Figure/table plan.
   - Journal-format strategy for in-text figure/table/supplement callouts, legends, headings, references, and statements.
   - Word/DOCX format strategy when the user requests a manuscript file.
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
- Use `storyline.paragraph_plan` before drafting major sections; if absent, create one rather than writing a full section with uncontrolled paragraph counts.
- Use `document_output.word_format_profile` for DOCX deliverables and verify line numbering, font family, text color, font size, spacing, and alignment before calling a file final.
- For Chinese-to-English work, produce idiomatic scientific English rather than literal translation.

## Quality Bar

A manuscript is not full-draft quality until it passes five gates:

1. Introduction: literature-backed funnel from background to known mechanisms, unresolved gap, scientific question, and study objective.
2. Results: evidence-dense subsections with controls, quantification/statistics, figure links, and short transition or reliability sentences.
3. Discussion: result-anchored expansion into prior work, mechanism, alternative explanations, implications, limitations, and future experiments.
4. Methods: reproducible procedural detail, including materials, treatments, replicates, instruments/software, quantification, statistics, and data/code availability.
5. Journal format: in-text callouts, figure legends, table titles, supplementary-material naming, headings, references, and declarations match the target-journal profile or are explicitly marked unknown.
6. Word format: DOCX outputs have continuous line numbers, Times New Roman, black 12 pt text, 1.5 line spacing, justified body text, and left-aligned headings, unless a target-journal exception is recorded.

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

Build 4 paragraphs by default when the target journal resembles the local Nature Communications/PNAS bamboo-reference pattern; use 4-6 paragraphs when comparable papers show a broader norm:

1. Research background and current field status, including the main source-backed context the target audience needs.
2. The central problem, gap, or scientific question that follows from that status.
3. The concrete difficulty, boundary, or technical/biological details that make the problem nontrivial and explain why existing approaches are insufficient.
4. This study's viewpoint, objective or hypothesis, design, and concise contribution statement.

Avoid generic textbook openings when comparable papers move quickly to a precise gap.
Each paragraph should have a source role, and the gap should emerge from the literature rather than appearing as an unsupported assertion.
When introducing the study's contribution, avoid formulaic or conversational openers such as `Here, we...`; prefer a precise bridge from the previous gap or problem, such as `To address this challenge...` or `To address this need...`.

### Results

Each result subsection should have:

- Purpose sentence.
- Method, comparison, or named result object.
- Main observation.
- Quantitative/statistical support.
- Link to figure/table/supplement.
- Short interpretive bridge to the next result.

For algorithm, software, platform, workflow, or resource-building Results with limited direct data or figure support, convert process steps into tangible results. Each major action should yield a named artifact, module, interface, output table, evidence report, quality-control layer, or reusable resource. The result claim should be what was produced and why it matters, while benchmark accuracy, biological validation, or user utility should be reserved for sections with supporting data.
For benchmark or head-to-head Results, write the comparison so it is fair but advantage-forward. Start with the shared dataset/task design, report the most granular advantage first, then show stability across groups or conditions, then test an orthogonal comparator or validation setting, and only then discuss the distinctive feature or mechanism behind the advantage. Do not give equal space to secondary wrappers, implementation checks, or exception cases unless they alter the main claim; summarize them briefly and move supporting detail to supplements, but include a conclusion-level number when mentioning them.
For resource-building, computational-analysis, or theory-generating Results, make each subsection a self-contained mini-story rather than a carry-over from the previous Result. Avoid weak openers such as "Next, we asked..." when the section can open with the produced resource, evidence object, or analytical question. Tie the prose to the main figure panel ladder: resource source and scope, representative case or selection logic, grouping or feature structure, functional interpretation with conservative literature support, and real-data example. Combine adjacent panels into one paragraph when they serve the same evidence layer; do not force one paragraph per panel.
For interface, browser, workflow, or implementation panels that precede biological data panels, state what later panel or case the interface enables readers to inspect. Do not treat the interface screenshot as an independent result if its role is to contextualize the data panels.
For refinement, re-clustering, subpopulation, or cell-state Results, first explain the decision logic being compared before reporting the split. For example, distinguish expression-neighbourhood partitioning from graph-guided candidate identity scoring, then show why the new split is biologically meaningful.
When a refinement result identifies a weak, rare, masked, or visually non-obvious state, use controlled wording such as candidate state, weakly marked rare-state signal, or putative missing label. Pair the claim with concise validation numbers, such as cell counts, purity or agreement, GO gene counts and FDR, rather than treating the state as fully resolved.
When GO enrichment, pathway enrichment, ontology terms, or functional annotation are used as biological support without direct experimental validation, pair the strongest terms and numbers with literature-backed biological context. State that the enrichment provides a literature-consistent biological or functional consistency check, not orthogonal validation or mechanistic proof. One brief discussion-like sentence at the start or end of the case is usually enough; do not leave GO terms as an uncited list, and do not turn the Results paragraph into a mini-review.
When adding secondary evidence inside a Results paragraph, keep it conclusion-serving and brief: state the result, the key number or range, and the claim it supports. Do not explain a metric, panel grammar, or intermediate calculation unless readers need it to understand the main claim; low-weight evidence should function as support, not become a methods aside.
Quantify exceptions and weak spots. Avoid vague claims such as "some datasets performed worse"; give counts, ranks, margins, affected groups, or dispersion so readers can see the boundary of the weakness and why it does not overturn the central result.
When a result is non-ideal, write it as a bounded and interpretable condition rather than an unqualified failure. Pair the number with the context that explains where it occurs, such as a data-rich subgroup, sparse reference evidence, a small margin, a comparator-specific advantage, a species/context boundary, or a known analysis constraint. The goal is not to hide weakness, but to show that the limitation is measurable, explainable, and controlled by the study design.
Avoid stiff transition sentences that merely announce a new dimension, such as "Accuracy was only one part of the benchmark result." Prefer a finding-linked bridge that names the added evidence layer, such as decision inspectability, robustness, mechanism, validation, or biological interpretation.
Use comparable papers to decide whether the journal favors mechanism-first, phenotype-first, cohort-first, resource-first, or method-validation-first sequencing.
Use the target journal's exact callout style from `journal_format_profile`, such as `Fig. 1A`, `Figure 1A`, `Figs. 1 and 2`, `Supplementary Fig. 1`, or `Table S1`; never mix styles inside one manuscript.
Plan Results as named subsections, not one long section. Each result subsection should default to 2-3 natural paragraphs: setup/purpose, evidence/statistics/figure support, and a concise interpretation or transition. If two adjacent paragraphs make the same comparison or explain the same figure-panel layer, merge them. Use 4 only for unusually complex multiomics/resource-building subsections when model papers justify it.
Allow brief discussion-like transition sentences in Results only when they improve continuity or explain why the next experiment is needed.

### Discussion

Use 3-4 paragraphs for concise Nature Communications/PNAS-like research articles unless comparable papers show a longer norm. Use 4-7 paragraphs for longer discussion-forward journals:

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

## Paragraph And Word Output Planning

Read `word-manuscript-format.md` before full-manuscript drafting, section paragraph planning, or DOCX generation.

The article architecture must include a paragraph plan:

| Section/Subsection | Target Paragraphs | Paragraph Jobs | Basis | Linked IDs |
|---|---:|---|---|---|
| Abstract | 1 | Context/gap; approach; result; implication | model / fallback | |
| Introduction | 4 | Stakes; known work; gap; objective/contribution | model / fallback | `S#` |
| Result subsection | 2-3 | Purpose; evidence; bridge | model / fallback | `C#`, `F#` |
| Discussion | 3-4 | Principal finding; literature/mechanism; limits; future/conclusion | model / fallback | `C#`, `S#` |

For DOCX deliverables, add or update:

```yaml
document_output:
  requested_formats: ["docx"]
  word_format_profile:
    line_numbering: "continuous"
    font_family: "Times New Roman"
    text_color: "000000"
    font_size_pt: 12
    line_spacing: 1.5
    body_alignment: "justified"
    heading_alignment: "left"
    validation_status: "not checked | pass | needs repair"
```

After creating the DOCX, run `scripts/enforce_manuscript_docx_format.py` and its `--check` mode unless another validated DOCX tool has already proved the same conditions, including Times New Roman font family.

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
- Paragraph counts and paragraph jobs match the paragraph plan or recorded target-journal/model-paper exception.
- Word/DOCX formatting has been applied and checked when a manuscript file is requested.
- Data/code/ethics/reporting checklists are included when relevant.
- All placeholders are listed for the user.
