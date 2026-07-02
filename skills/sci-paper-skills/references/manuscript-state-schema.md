# Manuscript State Schema

Use `manuscript_state` as the shared state object across all SCI-paper-skills modules. A module does not need to fill every field, but it must read the relevant upstream fields, update the fields it owns, and preserve unresolved gaps as `[NEED: ...]` or `[CITE: ...]`.

## State Header

```yaml
manuscript_state:
  state_version: "0.4"
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

citation_audit:
  unsupported_claim_ids: []
  verified_reference_ids: []
  metadata_risks: []
  citation_placement_plan: []
  citation_health: "pass | needs repair | blocked"

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
- Figures and tables use `F1`, `F2`, `T1`.
- Sources use `S1`, `S2`, `S3`.
- Papers used as comparable models use `P1`, `P2`, `P3`.
- Sections use `SEC1`, `SEC2`, `SEC3`.
- Reviewer issues use `R1`, `R2`, `R3`.

Every draftable sentence that makes a scientific claim should be traceable to at least one claim ID and either a figure/table ID, user-data note, or source ID.

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
