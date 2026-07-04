---
name: sci-draft-mimic
description: Initial SCI manuscript drafting and Word/DOCX manuscript preparation by imitating target-journal and user-provided model papers at the level of structure, paragraph counts, rhetorical moves, section flow, claim strength, figure/table/supplement callout style, Word formatting constraints, and expression style without copying text. Use when the user has journal research, journal format profile, literature evidence, storyline or paragraph plan, PDFs/model articles, Word manuscript requirements, or asks to draft title, abstract, introduction, results, discussion, methods, figure legends, cover letter, or DOCX manuscript in the style and format of comparable papers.
---

# SCI Draft Mimic

## Overview

Draft manuscript text by imitating patterns, not wording. Use model papers to learn structure, rhetorical moves, figure/table/supplement callout behavior, claim strength, and section rhythm while preserving the user's evidence.
Use paragraph plans to control natural paragraph counts before writing full sections. Use Word format profiles when the deliverable is `.docx`.

## Inputs

Prefer:

- Target journal portrait and article type.
- Target-journal `journal_format_profile`.
- Benchmark/model papers, comparable papers, or user-provided PDFs.
- Storyline plan and figure/case order.
- Paragraph plan with target paragraph counts and paragraph roles.
- Result-to-claim matrix and citation placeholders.
- Analysis provenance, statistical status, figure contracts, and source-data notes when results are quantitative or computational.
- Word/DOCX output requirements and `document_output.word_format_profile` when a file is requested.
- User's data, methods, statistics, approvals, and wording constraints.

If PDFs or links are provided, analyze their structure and rhetorical moves before drafting. Do not copy sentences, distinctive phrasing, or title formulas too closely.

## Mimic Extraction

Before drafting from model papers or PDFs, extract only reusable patterns:

- Article type and section order.
- Title shape and specificity.
- Abstract move order.
- Introduction funnel and gap statement.
- Results subsection rhythm and exact figure/table/supplement callout behavior.
- Natural paragraph count per major section and per Results subsection.
- Discussion opening, limitation style, and final implication.
- Supplement naming and citation pattern.
- Citation density, placement, claim strength, and hedging.

Imitate these patterns only at the level of structure and rhetorical function.

## Drafting Rules

- Start with title, abstract, or section outline unless the user asks for a specific section.
- Before a full manuscript or major section, consume or create a paragraph plan; do not write uncontrolled long sections.
- Follow the planned paragraph counts. Ordinary Results subsections should be 2-3 natural paragraphs unless the paragraph plan records a model-paper or journal exception.
- Use `[NEED: ...]` for missing scientific facts.
- Use `[CITE: claim]` for unverified literature support.
- Tie results to figures/tables/supplements using the exact target-journal callout style in `journal_format_profile`.
- Normalize all manuscript-facing callouts during drafting, including `Fig1`, `Fig. 1`, `Figure 1A`, `Figs. 1 and 2`, `Table 1`, `Supplementary Fig. 1`, `Fig. S1`, and `Table S1`; if the target rule is unknown, use `[NEED: target-journal figure/table callout style]`.
- Preserve internal state IDs (`F#`, `T#`, `C#`, `S#`) while converting them to journal-facing labels in prose.
- Keep claim strength no stronger than the result-to-claim matrix.
- Do not turn exploratory, underdiagnosed, or source-data-missing analysis into stable Results prose; keep `[NEED: analysis/statistics/source data]` placeholders visible.
- Make the Introduction literature-backed: move from field background to known mechanisms, unresolved gap, scientific question, and study objective with sources assigned to each role.
- Make Results evidence-dense: each subsection needs direct data, controls, quantification/statistics, figure references, and a brief interpretive bridge that connects to the next result without over-discussing.
- Make Discussion multi-angle: start from the main result, then expand through prior work, mechanism, alternative explanations, significance, limitations, and future experiments.
- Make Methods reproducible: include biological material, treatment details, sample sizes, controls, instrumentation, analysis software, statistical model, and data availability when known.
- For Word/DOCX output, apply continuous line numbering, Times New Roman, black 12 pt text, 1.5 line spacing, justified body paragraphs, and left-aligned headings; after file creation, run `../sci-paper-skills/scripts/enforce_manuscript_docx_format.py` and `--check` unless an equivalent validated tool is used.
- List which model patterns were used and what must be verified.

## Drafting Gate

If journal landscape, journal format profile, result-to-claim mapping, and storyline are missing, draft only a skeleton or partial section with placeholders. Do not create a confident full manuscript from vague conclusions, unstable analysis, source-data gaps, or mixed target-journal formats.
If a full manuscript or major section lacks a paragraph plan, create the plan first. If a DOCX deliverable lacks a Word format profile, create it first and mark validation as `not checked` until the file is inspected.

## State Coupling

Consume:

- `journal_landscape`, `journal_landscape.journal_format_profile`, `analysis_registry`, `source_ledger`, `claim_registry`, `figure_registry`, `data_availability_plan`, `story`, `storyline`, `storyline.paragraph_plan`, `document_output.word_format_profile`, and `reviewer_risk`.
- Model paper IDs `P#` and source IDs `S#` when available.

Update:

- `draft_registry.sections` with section IDs `SEC#` from `storyline.section_registry`.
- `draft_registry.open_needs`, `open_citations`, and `high_risk_claim_ids`.
- Section drafts that preserve linked claim IDs `C#`, figure/table IDs `F#`/`T#`, and source placeholders `S#` or `[CITE: ...]`.
- Draft-level format notes listing the journal-facing callout forms used and any unresolved format placeholders.
- Draft-level analysis/source-data notes listing unresolved statistics, source data, and data/code availability placeholders.
- Paragraph-plan adherence notes for each full section or Results subsection.
- `document_output` when a DOCX is requested, including the Word format profile, generated file path if available, enforcement script status, and validation status.

Block:

- If journal, format, analysis, claim, story, figure, source-data, or citation gates are missing, produce a skeleton or section scaffold only.
- If paragraph planning is missing for full drafting, produce a paragraph plan before prose or mark the draft as a scaffold.
- If DOCX formatting cannot be checked, do not call the Word manuscript final.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Style brief`.
- `Draft output` for the requested section(s).
- `Journal format notes`.
- `Paragraph plan` or `Paragraph-plan adherence`.
- `Word/DOCX format notes` when a file is requested.
- `Citation placeholders`.
- `Missing inputs`.
- `Pattern-use notes`.
- `High-risk claims`.

Read `references/draft-mimic-schema.md` for templates.
Read `references/manuscript-section-quality.md` before drafting a full manuscript, Introduction, Results, Discussion, or Methods section.
Read `../sci-paper-skills/references/word-manuscript-format.md` before creating a DOCX file or planning paragraph counts from model papers.
