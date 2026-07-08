# SCI-paper-skills Index

Use `sci-paper-skills` as the orchestrator unless the user explicitly requests a focused module. In the tight workflow, every module reads and updates `manuscript_state` and preserves IDs across handoffs.

| Stage | Skill | Use When | Primary Output | Typical Next Step |
|---:|---|---|---|---|
| 0 | `sci-stage-diagnosis` | The project feels stuck or the user does not know where to begin | Stage diagnosis | `sci-intake-router` or earliest blocker |
| 1 | `sci-intake-router` | Journal, topic, material, article type, or available inputs are unclear | Intake brief | `sci-journal-landscape` |
| 2 | `sci-journal-landscape` | A target journal or candidate list is available | Journal portrait, format profile, and comparable-paper landscape | `sci-literature-evidence` |
| 3 | `sci-literature-evidence` | Conclusions, hypotheses, novelty, or gaps need literature support | Evidence map | `sci-result-to-claim` |
| 4 | `sci-result-to-claim` | Figures, tables, data, cases, or result blocks need defensible claims | Result-to-claim matrix | `sci-core-story-finder` |
| 5 | `sci-core-story-finder` | Several manuscript angles are possible | Story decision memo | `sci-figure-story-builder` |
| 6 | `sci-figure-story-builder` | Main/supplement choices and result order are unclear | Figure story map | `sci-storyline-planner` |
| 7 | `sci-storyline-planner` | The manuscript needs structure, section order, paragraph counts, or alternative logic | Storyline and paragraph plan | `sci-reviewer-simulator` |
| 8 | `sci-reviewer-simulator` | Editor or reviewer objections need to be predicted before drafting/submission | Reviewer risk report | Repair blocker or `sci-draft-mimic` |
| 9 | `sci-draft-mimic` | Model papers or target-journal patterns, paragraph rhythms, and formats should guide drafting | Style brief, paragraph notes, format notes, and draft package | `sci-paragraph-coach` |
| 10 | `sci-paragraph-coach` | A specific paragraph, paragraph count, section opening, figure legend, or cover-letter paragraph needs help | Paragraph scaffold, count note, and coached text | `sci-language-polisher` |
| 11 | `sci-language-polisher` | The meaning is stable and expression, paragraph discipline, or journal format needs polishing | Polished text, paragraph notes, format corrections, and claim notes | `sci-citation-control` |
| 12 | `sci-citation-control` | References, citation placement, metadata, unsupported claims, or format callouts need auditing | Citation and format audit | `sci-submission-revision` |
| 13 | `sci-submission-revision` | Files, Word/DOCX checks, cover letter, declarations, format compliance, reviewer response, or revision strategy are needed | Submission/revision package | Final check or resubmission |

## Trigger Examples

- "I have data but cannot write the paper" -> `sci-stage-diagnosis`.
- "I want to submit to The Plant Cell" -> `sci-journal-landscape`.
- "Should I write Fig. 1, Figure 1, or Fig1?" -> `sci-journal-landscape`.
- "Do these conclusions have literature support?" -> `sci-literature-evidence`.
- "I have raw data or statistical outputs but do not know whether the result is reliable" -> adjacent analysis/statistics skill, then `sci-result-to-claim`.
- "Find reusable public datasets, benchmark cohorts, source data, or accession records for this manuscript" -> dataset/domain repository connector, then `sci-result-to-claim` and `sci-citation-control`.
- "Find related papers or the companion paper for this dataset" -> `sci-literature-evidence` or `sci-journal-landscape` depending on whether the goal is evidence support or journal fit.
- "What can Figure 2 prove?" -> `sci-result-to-claim`.
- "Which story should this paper tell?" -> `sci-core-story-finder`.
- "How should I arrange these figures?" -> `sci-figure-story-builder`.
- "Can this figure survive submission?" -> `sci-figure-story-builder` plus figure/source-data readiness checks.
- "Give me two manuscript structures" -> `sci-storyline-planner`.
- "Plan the paragraph counts for each section" -> `sci-storyline-planner`.
- "What will reviewers attack?" -> `sci-reviewer-simulator`.
- "Draft an abstract like these papers" -> `sci-draft-mimic`.
- "Generate a Word manuscript with line numbers" -> `sci-draft-mimic`, then `sci-submission-revision`.
- "Help me write this Discussion paragraph" -> `sci-paragraph-coach`.
- "Polish this SCI English" -> `sci-language-polisher`.
- "Check whether my citations support each claim" -> `sci-citation-control`.
- "Prepare a response to reviewers" -> `sci-submission-revision`.

## Routing Defaults

When two modules are plausible, route to the earliest unresolved gate:

1. Intake and journal target.
2. Journal landscape.
3. Journal-specific format profile.
4. Literature evidence, related-paper context, and dataset companion-paper links.
5. Analysis/statistical provenance when raw data, public datasets, repository records, or computational outputs drive claims.
6. Claim control.
7. Story selection.
8. Figure narrative and source-data readiness.
9. Manuscript structure.
10. Paragraph plan and Word/DOCX output requirements when requested.
11. Reviewer risk.
12. Drafting and paragraph work.
13. Language polishing.
14. Citation audit, including dataset/software citations.
15. Submission or revision.

## Handoff Discipline

Each module should end with:

- `Manuscript State Update`: fields changed, IDs created, blockers, next skill, user task.
- `Handoff`: consumed artifact, produced artifact, blockers, next route.

When a user jumps into the middle of the workflow, reconstruct only the state fields supported by the provided context and mark missing fields with `[NEED: ...]`.
