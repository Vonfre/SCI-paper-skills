# Manuscript State Schema

Use `manuscript_state` as the shared state object across all SCI-paper-skills modules. A module does not need to fill every field, but it must read the relevant upstream fields, update the fields it owns, and preserve unresolved gaps as `[NEED: ...]` or `[CITE: ...]`.

## State Header

```yaml
manuscript_state:
  state_version: "0.5"
  project_id: "[NEED: project id or short topic]"
  updated_by_skill: "[skill name]"
  current_stage: "[stage label]"
  next_skill: "[recommended next skill]"
  global_blockers: []
```

## Project

```yaml
project:
  user_goal: ""
  target_journal: ""
  candidate_journals: []
  target_level: ""
  article_type: ""
  topic: ""
  field: ""
  organism_material_system: ""
  main_methods: []
  available_artifacts: []
  deadline_or_decision_context: ""
  missing_inputs: []
```

## Journal Landscape

```yaml
journal_landscape:
  journal_portrait: ""
  author_constraints: []
  article_type_constraints: []
  journal_format_profile:
    source_basis:
      figure_table_callouts: "official | benchmark | fallback | unknown"
      supplement_callouts: "official | benchmark | fallback | unknown"
      references: "official | benchmark | fallback | unknown"
      abstract_headings: "official | benchmark | fallback | unknown"
      figure_legends_tables: "official | benchmark | fallback | unknown"
    in_text_callouts:
      main_figure: ""
      main_figure_panel: ""
      multiple_figures: ""
      main_table: ""
      supplementary_figure: ""
      supplementary_table: ""
      supplementary_data: ""
      parenthetical_or_narrative: ""
    section_and_back_matter:
      abstract: ""
      heading_order: []
      methods_placement: ""
      figure_legend_title: ""
      table_title: ""
      reference_style: ""
      data_code_statement_label: ""
    rewrite_rules:
      - mixed_form: ""
        correct_form: ""
        scope: ""
    format_unknowns: []
  comparable_papers:
    - paper_id: "P1"
      citation: ""
      doi_or_url: ""
      why_comparable: ""
      pattern_to_reuse: ""
  fit_verdict: "Strong | Possible but risky | Weak | Unknown"
  manuscript_must_prove: []
  retrieval_dates: []
  journal_blockers: []
```

## Source Ledger

```yaml
source_ledger:
  research_questions: []
  sources:
    - source_id: "S1"
      citation: ""
      doi_pmid_url: ""
      source_type: "primary | review | method | dataset | guideline | preprint | other"
      metadata_status: "verified | needs check | user-provided"
      evidence_location: ""
      supports_claim_ids: []
      contradicts_or_qualifies_claim_ids: []
      confidence: "verified | plausible | weak | conflicting | unknown"
```

## Analysis Registry

```yaml
analysis_registry:
  datasets:
    - dataset_id: "D1"
      file_or_source: ""
      data_type: ""
      provenance_status: "verified | user-provided | needs check"
      preprocessing_summary: ""
      quality_risks: []
  statistical_plan:
    - analysis_id: "A1"
      linked_claim_ids: []
      endpoint_or_metric: ""
      comparison_or_model: ""
      sample_size_and_replicate_unit: ""
      test_or_model: ""
      assumptions_checked: []
      effect_size_or_estimate: ""
      uncertainty: ""
      multiple_testing_or_posthoc: ""
      status: "ready | exploratory | needs diagnostics | blocked"
```

## Claim Registry

```yaml

claim_registry:
  claims:
    - claim_id: "C1"
      linked_result_or_figure_ids: []
      observation: ""
      user_interpretation: ""
      claim_level: "descriptive | association | regulation | mechanism | causality | application | novelty"
      safe_wording: ""
      stronger_wording_if_fixed: ""
      evidence_needed_for_stronger_claim: []
      citation_needs: []
      status: "draftable | needs evidence | too strong | unsupported"
```

## Figure Registry

```yaml
figure_registry:
  figures:
    - figure_id: "F1"
      title_or_label: ""
      figure_contract:
        core_conclusion: ""
        evidence_chain: []
        statistics_integrity_notes: []
        export_requirements: []
      role: "opening | central proof | validation | extension | method | supplement | cut"
      answered_question: ""
      linked_claim_ids: []
      placement: "main | supplement | cut | undecided"
      missing_panels_controls_stats: []
      transition_to_next_figure: ""
```

## Story And Storyline

```yaml
story:
  candidate_stories: []
  recommended_story:
    story_id: "ST1"
    one_sentence_takeaway: ""
    selected_claim_ids: []
    excluded_or_supplement_claim_ids: []
    target_journal_fit_reason: ""
    risk: ""
  backup_story: ""
  manuscript_boundary: ""

storyline:
  result_order: []
  paragraph_plan:
    basis: "official | model papers | local bamboo-reference baseline | fallback | unknown"
    reference_papers:
      - paper_id: "P1"
        citation: ""
        paragraph_pattern: ""
    sections:
      - section_id: "SEC1"
        section_type: "abstract | introduction | results | discussion | methods | figure_legend | cover_letter"
        target_paragraphs: "1 | 2-3 | 3-4 | 4 | subheaded | [NEED: ...]"
        paragraph_roles: []
        linked_claim_ids: []
        linked_figure_ids: []
        needed_source_ids: []
        basis_note: ""
  section_registry:
    - section_id: "SEC1"
      section_type: "title | abstract | introduction | results | discussion | methods | cover_letter | rebuttal"
      purpose: ""
      linked_claim_ids: []
      linked_figure_ids: []
      needed_source_ids: []
      draft_status: "not started | skeleton | drafted | polished | citation-checked | submission-ready"
  drafting_brief: ""
  draft_readiness: "ready | skeleton only | blocked"
  draft_blockers: []
```

## Review, Draft, Citation, And Submission

```yaml
reviewer_risk:
  scorecard: []
  blocking_objections: []
  major_objections: []
  repair_queue: []
  decision: "submit | revise before submission | add work | change journal | unknown"

draft_registry:
  sections: []
  open_needs: []
  open_citations: []
  high_risk_claim_ids: []

document_output:
  requested_formats: []
  word_format_profile:
    line_numbering: "continuous | newPage | newSection | none | unknown"
    text_color: "000000 | unknown"
    font_size_pt: 12
    line_spacing: 1.5
    body_alignment: "justified | left | unknown"
    heading_alignment: "left | unknown"
    enforcement_script: "scripts/enforce_manuscript_docx_format.py"
    validation_status: "not requested | not checked | pass | needs repair | journal exception"
    exceptions: []

citation_audit:
  unsupported_claim_ids: []
  verified_reference_ids: []
  dataset_software_citation_issues: []
  metadata_risks: []
  format_issues: []
  citation_placement_plan: []
  citation_health: "pass | needs repair | blocked"

data_availability_plan:
  supporting_artifacts: []
  repository_or_accession_status: []
  source_data_requirements: []
  software_code_requirements: []
  unresolved_data_fields: []

submission_package:
  file_checklist: []
  required_statements: []
  unresolved_placeholders: []
  cover_letter_status: ""
  rebuttal_matrix_status: ""
  final_readiness: "ready | needs repair | blocked"
```

## ID Rules

- Claims use `C1`, `C2`, `C3`.
- Datasets use `D1`, `D2`, `D3`.
- Analyses use `A1`, `A2`, `A3`.
- Figures and tables use `F1`, `F2`, `T1`.
- Sources use `S1`, `S2`, `S3`.
- Papers used as comparable models use `P1`, `P2`, `P3`.
- Sections use `SEC1`, `SEC2`, `SEC3`.
- Reviewer issues use `R1`, `R2`, `R3`.

Every draftable sentence that makes a scientific claim should be traceable to at least one claim ID and either a figure/table ID, user-data note, or source ID. Every full-section draft should also trace to a paragraph-plan entry unless the user explicitly asks for a quick sketch.

For Word/DOCX manuscript outputs, `document_output.word_format_profile.validation_status` should be `pass` before final delivery unless the target journal explicitly requires a different format and the exception is recorded.

## State Update Block

Every module should end with a compact state update:

```markdown
## Manuscript State Update
- Updated fields:
- New IDs created:
- Blockers:
- Next skill:
- User task:
```
