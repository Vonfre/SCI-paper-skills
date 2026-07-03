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
| 3 | `sci-literature-evidence` | `project`, `journal_landscape`, candidate claims/questions | `source_ledger`, literature support/conflict, citation needs, novelty boundaries | unverified sources for precise claims | `sci-result-to-claim` or `sci-citation-control` |
| 4 | `sci-result-to-claim` | results, figure descriptions, `source_ledger`, `journal_landscape` | `claim_registry` with IDs `C#`, evidence gaps, safe wording | no results or observations | `sci-core-story-finder` |
| 5 | `sci-core-story-finder` | `claim_registry`, `journal_landscape`, `source_ledger`, optional figures | `story`, selected/excluded claim IDs, manuscript boundary | no draftable claims | `sci-figure-story-builder` |
| 6 | `sci-figure-story-builder` | `story`, `claim_registry`, `journal_landscape.journal_format_profile`, figure/table inventory | `figure_registry` with IDs `F#`, claim-figure map, result skeleton, label notes | central claim lacks main-text evidence | `sci-storyline-planner` |
| 7 | `sci-storyline-planner` | `story`, `claim_registry`, `figure_registry`, `journal_landscape`, `journal_landscape.journal_format_profile`, `source_ledger` | `storyline`, `section_registry`, result order, drafting brief | no story or no claim/figure map | `sci-reviewer-simulator` |
| 8 | `sci-reviewer-simulator` | `journal_landscape`, `journal_landscape.journal_format_profile`, `claim_registry`, `figure_registry`, `storyline`, draft if present | `reviewer_risk`, scorecard, repair queue, overclaim fixes | blocking objections unresolved | repair stage or `sci-draft-mimic` |
| 9 | `sci-draft-mimic` | `journal_landscape`, `journal_landscape.journal_format_profile`, `source_ledger`, `claim_registry`, `figure_registry`, `storyline`, `reviewer_risk` | `draft_registry`, section drafts, open needs/citations, high-risk claims, format notes | missing journal/format/claim/story/figure gates | `sci-paragraph-coach` or `sci-citation-control` |
| 10 | `sci-paragraph-coach` | `section_registry`, target paragraph, linked `C#`, `F#`, `S#`, `journal_landscape.journal_format_profile` | paragraph block, updated `draft_registry` section status, format note | paragraph lacks purpose/evidence | `sci-language-polisher` |
| 11 | `sci-language-polisher` | `draft_registry`, source text, `claim_registry`, journal tone, `journal_landscape.journal_format_profile` | polished text, meaning-change notes, format corrections, remaining risk IDs | meaning, claim support, or target-journal format unstable | `sci-citation-control` |
| 12 | `sci-citation-control` | `claim_registry`, `source_ledger`, `draft_registry`, target style, `journal_landscape.journal_format_profile` | `citation_audit`, verified source IDs, unsupported claims, placement plan, format issue list | unresolved unsupported claims, format issues, or metadata risks | `sci-submission-revision` |
| 13 | `sci-submission-revision` | `journal_landscape`, `journal_landscape.journal_format_profile`, `draft_registry`, `figure_registry`, `citation_audit`, reviewer comments | `submission_package`, file checklist, format compliance check, rebuttal matrix, final readiness | placeholders, unknown requirements, unsupported claims, unresolved format issues | final repair or submission |

## Gate Rules

1. A downstream skill must not silently replace a missing upstream artifact with invented content.
2. If a required upstream field is missing, the skill must either ask for it or create a clearly provisional artifact.
3. `sci-draft-mimic` may only produce a full draft when the journal, journal-format, claim, story, figure, and citation gates are at least provisionally controlled.
4. `sci-language-polisher` must not strengthen claims unless `claim_registry` supports the stronger wording.
5. `sci-submission-revision` must not mark the package ready while `[NEED: ...]`, `[CITE: ...]`, or unresolved journal-format placeholders remain in submission-facing text.

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
