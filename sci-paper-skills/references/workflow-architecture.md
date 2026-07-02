# SCI-paper-skills Workflow Architecture

Use this reference when coordinating the full SCI-paper-skills collection.

## Principle

The workflow adapts to the user's real state. A novice with results but no story should not be pushed into full drafting. A user with a draft should not be sent back to early ideation unless the draft has a structural flaw.

## Stage Map

| Stage | Skill | Core Question | Artifact |
|---:|---|---|---|
| 0 | `sci-stage-diagnosis` | Where is the project stuck? | Stage diagnosis |
| 1 | `sci-intake-router` | What journal, topic, system, and materials exist? | Intake brief |
| 2 | `sci-journal-landscape` | What does the target journal publish, and are there similar papers? | Journal landscape |
| 3 | `sci-literature-evidence` | What does literature support, contradict, or leave open? | Evidence map |
| 4 | `sci-result-to-claim` | What can the user's results actually claim? | Result-to-claim matrix |
| 5 | `sci-core-story-finder` | What is the paper's central story? | Story decision memo |
| 6 | `sci-figure-story-builder` | How should figures/cases teach the story? | Figure story map |
| 7 | `sci-storyline-planner` | What is the best manuscript logic? | Storyline plan |
| 8 | `sci-reviewer-simulator` | What will editors/reviewers challenge? | Reviewer risk report |
| 9 | `sci-draft-mimic` | How should the first draft imitate target/model papers? | Draft package |
| 10 | `sci-paragraph-coach` | How should each paragraph be built? | Paragraph coaching block |
| 11 | `sci-language-polisher` | How should expression be polished without changing meaning? | Polish report |
| 12 | `sci-citation-control` | Are claims, evidence, and citations aligned? | Citation audit |
| 13 | `sci-submission-revision` | Is the manuscript ready for submission or revision? | Submission/rebuttal package |

## Three User Scenarios

### User Has Results But No Paper Logic

Run:

1. `sci-stage-diagnosis`
2. `sci-result-to-claim`
3. `sci-core-story-finder`
4. `sci-figure-story-builder`
5. `sci-storyline-planner`
6. `sci-reviewer-simulator`
7. `sci-draft-mimic`

Do not begin drafting until the result-to-claim matrix and figure story map exist.

### User Has Target Journal But Weak Field Context

Run:

1. `sci-intake-router`
2. `sci-journal-landscape`
3. `sci-literature-evidence`
4. `sci-core-story-finder`
5. `sci-storyline-planner`

If same-journal papers are scarce, use same-level or peer-journal fallback papers and label them clearly.

### User Has Draft But Poor Expression

Run:

1. `sci-reviewer-simulator`
2. `sci-citation-control`
3. `sci-paragraph-coach` for weak sections
4. `sci-language-polisher`
5. `sci-submission-revision`

If reviewer simulation finds a story or claim flaw, return to the earlier stage rather than only polishing sentences.

## Gate Checks

Gate 1: project understood
- Target journal or target level is known.
- Research topic, model system, and material status are known.
- User's current stage is classified.

Gate 2: journal and field understood
- Target-journal rules and article expectations are recorded.
- Same-journal similar papers or peer-journal fallbacks are identified.
- A landscape opinion says what the manuscript must prove to fit.

Gate 3: literature position is known
- Supporting, conflicting, and boundary-setting literature are separated.
- Novelty and "first" claims are checked with extra caution.
- If the user has no conclusion, possible directions are mapped to needed evidence.

Gate 4: claims are controlled
- Each result maps to what it can and cannot claim.
- Evidence gaps are prioritized.
- Strong claim wording is tied to explicit additional evidence.

Gate 5: story is chosen
- One central story and one backup story exist.
- The story fits the target journal bar or the mismatch is explicit.
- The manuscript boundary says what belongs in main text, supplement, or future work.

Gate 6: figures teach the story
- Main figures answer sequential questions.
- Supplements support but do not carry the decisive proof.
- Missing controls, statistics, quantification, or validation are visible.

Gate 7: reviewer risk is handled
- Blocking objections are fixed or assigned.
- Overclaims are softened.
- The smallest credible fix and stronger fix are both listed.

Gate 8: draft is traceable
- Draft text follows model-paper structure without copying language.
- Missing facts and citations are visible.
- Each result claim points to a figure/table/supplement or user data.

Gate 9: final text is submission-aware
- Meaning is preserved.
- References, statements, figures, supplements, and journal requirements are checked.
- Submission files and declarations match the target journal.

## Artifact Contracts

Every stage should leave a structured output the next stage can reuse:

- Stage diagnosis: stage label, reason, do-not-do-yet warning, next action.
- Intake brief: target journal, topic, model system, current materials, missing inputs.
- Journal landscape: journal portrait, author constraints, comparable papers, fit opinion.
- Evidence map: support/conflict literature, possible directions, gap assessment.
- Result-to-claim matrix: defensible claims, unsafe claims, evidence gaps, safe wording.
- Story memo: recommended central story, backup story, manuscript boundary.
- Figure story map: main/supplement/cut decisions, result transitions, missing panels.
- Storyline plan: recommended section order, alternative plans, drafting brief.
- Reviewer report: predicted objections, severity, minimum fixes, claim rewrites.
- Draft package: model-paper style brief, draft text, placeholders, imitation notes.
- Paragraph coach: paragraph purpose, sentence scaffold, example, draft feedback.
- Polish report: polished text, claim-strength changes, unresolved risks.
- Citation audit: claim-reference placement, verification, style and metadata risks.
- Submission package: file checklist, cover letter, declarations, rebuttal matrix when needed.

## User Guidance Pattern

For inexperienced users, end each stage with:

- `What we know`.
- `What is still missing`.
- `Do not do yet`.
- `Your next 30-minute task`.
- `Next skill to run`.
