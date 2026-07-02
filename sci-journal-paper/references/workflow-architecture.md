# Final SCI Manuscript Workflow Architecture

Use this reference when coordinating the final SCI skills collection.

## Principle

The workflow must adapt to the user's real state. A novice with results but no story should not be pushed into full drafting. A user with a draft should not be sent back to early ideation unless the draft has a structural flaw.

## Stage Map

| Stage | Skill | Core Question | Artifact |
|---:|---|---|---|
| 0 | `sci-stage-diagnosis` | Where is the project stuck? | Stage diagnosis |
| 1 | `sci-intake-router` | What journal, topic, and materials exist? | Intake brief |
| 2 | `sci-journal-landscape` | What does the target journal publish, and are there similar papers? | Journal landscape |
| 3 | `sci-literature-evidence` | What does literature support, contradict, or leave open? | Evidence map |
| 4 | `sci-result-to-claim` | What can the user's results actually claim? | Result-to-claim matrix |
| 5 | `sci-core-story-finder` | What is the paper's central story? | Story decision memo |
| 6 | `sci-figure-story-builder` | How should figures/cases teach the story? | Figure story map |
| 7 | `sci-storyline-planner` | What is the best manuscript logic? | Storyline plan |
| 8 | `sci-reviewer-simulator` | What will editors/reviewers challenge? | Reviewer risk report |
| 9 | `sci-draft-mimic` | How should the first draft imitate target/model papers? | Draft mimic package |
| 10 | `sci-paragraph-coach` | How should each paragraph be built? | Paragraph coaching blocks |
| 11 | `sci-language-polisher` | How should expression be polished without changing meaning? | Polish report |
| 12 | `sci-citation-control` | Are claims, evidence, and citations aligned? | Citation map |
| 13 | `sci-submission-revision` | Is the manuscript ready for submission or revision? | Submission/rebuttal package |

## Recommended Folder Tree

```text
00-stage-diagnosis/
01-intake/
02-journal-landscape/
03-literature-evidence/
04-result-to-claim/
05-core-story/
06-figure-story/
07-storyline-planning/
08-reviewer-simulation/
09-draft-mimic/
10-paragraph-coach/
11-language-polish/
12-citation-control/
13-submission-revision/
14-deconstruction-archive/
```

## Gate Checks

Gate 1: project understood
- Target journal or target level is known.
- Research topic, model system, and material status are known.

Gate 2: journal and field understood
- Target-journal rules and article expectations are recorded.
- Same-journal similar papers or peer-journal fallbacks are identified.

Gate 3: claims are controlled
- Each result maps to what it can and cannot claim.
- Evidence gaps are prioritized.

Gate 4: story is chosen
- One central story and one backup story exist.
- The story fits the target journal bar or the mismatch is explicit.

Gate 5: figures teach the story
- Main figures answer sequential questions.
- Supplements support but do not carry the decisive proof.

Gate 6: reviewer risk is handled
- Blocking objections are fixed or assigned.
- Overclaims are softened.

Gate 7: draft is traceable
- Draft text follows model-paper structure without copying language.
- Missing facts and citations are visible.

Gate 8: final text is submission-aware
- Meaning is preserved.
- References, statements, figures, supplements, and journal requirements are checked.

## Artifact Contracts

Every stage should leave a file or structured output that the next stage can use:

- Stage diagnosis: stage label, next best action.
- Intake brief: target journal, topic, current materials.
- Journal landscape: journal portrait, similar papers, landscape opinion.
- Evidence map: support/conflict literature, possible directions, gap assessment.
- Result-to-claim matrix: defensible claims and evidence gaps.
- Story memo: recommended central story and manuscript boundary.
- Figure story map: main/supplement/cut decisions and result transitions.
- Storyline plan: section order and drafting brief.
- Reviewer report: predicted objections and fixes.
- Draft package: style brief and section draft.
- Paragraph coach: paragraph purpose, scaffold, example.
- Polish report: polished text and claim-strength changes.
- Citation map: claim-reference placement and verification.
- Submission package: checklist, cover letter, rebuttal matrix when needed.
