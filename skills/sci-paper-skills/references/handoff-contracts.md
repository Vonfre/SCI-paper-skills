# Handoff Contracts

These contracts define how each stage consumes and updates `manuscript_state`. A skill may run provisionally with missing upstream fields, but it must mark missing fields and avoid pretending that the gate has passed.

## Contract Format

Each stage follows:

- `Consumes`: upstream state fields or user inputs the stage must inspect.
- `Produces`: state fields the stage owns and must update.
- `Blocks`: conditions that prevent a confident downstream handoff.
- `Next`: normal route after the stage.

## Stage Contracts

| Stage | Skill | Consumes | Produces | Blocks | Next |
|---:|---|---|---|---|---|
| 0 | `sci-stage-diagnosis` | user request, any existing `manuscript_state` | `current_stage`, `global_blockers`, `next_skill`, user task | no topic and no material | `sci-intake-router` or earliest blocker |
| 1 | `sci-intake-router` | current user context, existing `project` | `project`, `available_artifacts`, `missing_inputs`, `next_skill` | no topic/material/goal | `sci-journal-landscape`, `sci-result-to-claim`, or diagnosed blocker |
| 2 | `sci-journal-landscape` | `project.target_journal`, `project.topic`, `project.article_type` | `journal_landscape`, `journal_landscape.journal_format_profile`, comparable paper IDs `P#`, journal blockers | no target journal or insufficient topic keywords | `sci-literature-evidence` |
| 3 | `sci-literature-evidence` | `project`, `journal_landscape`, candidate claims/questions, dataset or accession context when present | `source_ledger`, literature support/conflict, related-paper roles, dataset companion-paper links, citation needs, novelty boundaries | unverified sources for precise claims; unresolved dataset companion paper when it affects a claim | `sci-result-to-claim` or `sci-citation-control` |
| 4 | `sci-result-to-claim` | results, figure descriptions, `analysis_registry`, dataset evidence cards, `source_ledger`, `journal_landscape` | `analysis_registry` updates, `claim_registry` with IDs `C#`, dataset suitability notes, evidence gaps, safe wording | no results or observations; analysis-derived claims lack provenance/statistical status; dataset-derived claims lack suitability or source-role status | `sci-core-story-finder` |
| 5 | `sci-core-story-finder` | `claim_registry`, `journal_landscape`, `source_ledger`, optional figures | `story`, selected/excluded claim IDs, manuscript boundary | no draftable claims | `sci-figure-story-builder` |
| 6 | `sci-figure-story-builder` | `story`, `claim_registry`, `analysis_registry`, `journal_landscape.journal_format_profile`, figure/table inventory | `figure_registry` with IDs `F#`, figure contracts, claim-figure map, result skeleton, label/export notes | central claim lacks main-text evidence; figure source data/statistics/export needs unresolved | `sci-storyline-planner` |
| 7 | `sci-storyline-planner` | `story`, `claim_registry`, `figure_registry`, `journal_landscape`, `journal_landscape.journal_format_profile`, `source_ledger`, comparable/model-paper paragraph patterns | `storyline`, `section_registry`, `storyline.paragraph_plan`, result order, drafting brief | no story or no claim/figure map; paragraph counts unsupported for full drafting | `sci-reviewer-simulator` |
| 8 | `sci-reviewer-simulator` | `journal_landscape`, `journal_landscape.journal_format_profile`, `analysis_registry`, `claim_registry`, `figure_registry`, `storyline`, draft if present | `reviewer_risk`, scorecard, repair queue, overclaim/statistics/figure fixes | blocking objections unresolved | repair stage or `sci-draft-mimic` |
| 9 | `sci-draft-mimic` | `journal_landscape`, `journal_landscape.journal_format_profile`, `analysis_registry`, `source_ledger`, `claim_registry`, `figure_registry`, `data_availability_plan`, `storyline`, `storyline.paragraph_plan`, `document_output.word_format_profile`, `reviewer_risk` | `draft_registry`, `document_output`, section drafts, open needs/citations, high-risk claims, paragraph-plan adherence notes, format and analysis/source-data notes | missing journal/format/analysis/claim/story/figure gates; missing paragraph plan for full sections; unchecked Word profile for DOCX final output | `sci-paragraph-coach` or `sci-citation-control` |
| 10 | `sci-paragraph-coach` | `section_registry`, `storyline.paragraph_plan`, target paragraph, linked `C#`, `F#`, `S#`, `journal_landscape.journal_format_profile` | paragraph block, updated `draft_registry` section status, paragraph count note, format note | paragraph lacks purpose/evidence or exceeds planned paragraph role without justification | `sci-language-polisher` |
| 11 | `sci-language-polisher` | `draft_registry`, source text, `claim_registry`, journal tone, `journal_landscape.journal_format_profile` | polished text, meaning-change notes, format corrections, remaining risk IDs | meaning, claim support, or target-journal format unstable | `sci-citation-control` |
| 12 | `sci-citation-control` | `claim_registry`, `source_ledger`, `draft_registry`, target style, `journal_landscape.journal_format_profile`, data/software citation needs | `citation_audit`, verified source IDs, `dataset_software_citation_issues`, unsupported claims, placement plan, format issue list | unresolved unsupported claims, format issues, metadata risks, or missing dataset/software citations | `sci-submission-revision` |
| 13 | `sci-submission-revision` | `journal_landscape`, `journal_landscape.journal_format_profile`, `storyline.paragraph_plan`, `document_output`, `analysis_registry`, `draft_registry`, `figure_registry`, `citation_audit`, `data_availability_plan`, reviewer comments | `data_availability_plan`, `document_output`, `submission_package`, file checklist, paragraph/Word format compliance check, rebuttal matrix, final readiness | placeholders, unknown requirements, unsupported claims, unresolved paragraph-plan, Word/DOCX format, data/source-code issues | final repair or submission |

## Gate Rules

1. A downstream skill must not silently replace a missing upstream artifact with invented content.
2. If a required upstream field is missing, the skill must either ask for it or create a clearly provisional artifact.
3. `sci-draft-mimic` may only produce a full draft when the journal, journal-format, claim, story, figure, and citation gates are at least provisionally controlled.
4. `sci-language-polisher` must not strengthen claims unless `claim_registry` supports the stronger wording.
5. Analysis-derived results must keep provenance, sample size/replicate unit, statistical status, and effect/uncertainty visible until submission.
6. Dataset-derived or benchmark-derived claims must keep accession/repository, version or release status, companion paper, sample unit, suitability limits, access restrictions, and citation requirements visible until submission.
7. Full-manuscript and major-section drafts must have a `storyline.paragraph_plan`; Results subsections default to 2-3 natural paragraphs unless the target journal or model papers justify a different count.
8. Word/DOCX outputs must have continuous line numbering, Times New Roman, black 12 pt text, 1.5 spacing, justified body text, and left-aligned headings checked through `document_output.word_format_profile`.
9. `sci-submission-revision` must not mark the package ready while `[NEED: ...]`, `[CITE: ...]`, unresolved journal-format placeholders, paragraph-plan gaps, DOCX format failures, data/source-code gaps, or missing dataset/software citations remain in submission-facing text.

## Handoff Footer

Every skill output should end with:

```markdown
## Handoff
- Consumed:
- Produced:
- Blockers:
- Next:
```

This footer keeps the workflow tight even when the user jumps into the middle of the pipeline.
