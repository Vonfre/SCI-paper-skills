---
name: sci-submission-revision
description: SCI journal submission package preparation, compliance checking, cover letters, declarations, supplementary-file organization, reviewer suggestions, reviewer-response strategy, rebuttal letters, revision plans, and post-decision manuscript repair. Use when the user is preparing files for submission, checking target-journal requirements, responding to editor or reviewer comments, resubmitting, or tracking changes after peer review.
---

# SCI Submission Revision

## Overview

Own the final mile from manuscript draft to journal submission and peer-review revision. Convert journal requirements or reviewer comments into a precise file checklist, cover/rebuttal strategy, and manuscript repair plan.

## Submission Workflow

1. Confirm target journal, article type, and submission goal.
2. Use `sci-journal-landscape` constraints for author instructions, article type, files, limits, and policies.
3. Build a file inventory: manuscript, title page, figures, tables, supplements, cover letter, highlights, graphical abstract, reporting checklists, declarations.
4. Check compliance: word limits, abstract format, figure/table limits, supplement naming, data/code availability, ethics/consent/animal approval, funding, conflicts, author contributions, AI-use disclosure when relevant.
5. Draft or repair cover-letter content with exact scope fit, contribution, novelty, and declarations.

## Readiness Rule

Do not call a manuscript ready if any of these are unresolved:

- Target article type or journal requirements are unknown.
- Required statements are missing.
- Figures/supplements do not match journal rules.
- Major claims lack data or citation support.
- References are unverified.
- Placeholders remain in submission-facing text.

## Revision Workflow

1. Parse editor and reviewer comments into atomic issues.
2. Classify each issue: scope/novelty, method detail, statistics, missing experiment/analysis, interpretation too strong, literature/citation gap, figure/table clarity, language/organization, ethics/data availability.
3. Choose a strategy: agree and revise, add analysis, add citation, add limitation, clarify existing text, respectfully disagree with evidence, or defer as outside current scope.
4. Map every promised change to a manuscript location.
5. Draft a calm response that states what changed or why no change was made.

## Quality Gate

Do not claim a file is submission-ready until:

- Journal requirements are verified from current sources.
- Every placeholder is listed.
- Every declaration need is resolved or marked missing.
- Every reviewer response maps to a manuscript change or justified no-change decision.

## Response Rule

Every reviewer response must map to one of three outcomes:

- Manuscript changed, with location.
- Additional analysis/experiment added, with location and evidence.
- No change made, with a concise evidence-based reason.

Do not promise data, experiments, or analyses the user has not performed.

## State Coupling

Consume:

- `journal_landscape`, `draft_registry`, `figure_registry`, `citation_audit`, `reviewer_risk`, and reviewer/editor comments when available.

Update:

- `submission_package.file_checklist`, `required_statements`, `unresolved_placeholders`, `cover_letter_status`, `rebuttal_matrix_status`, and `final_readiness`.
- Reviewer issue IDs `R#` when parsing decision letters.
- `global_blockers` for unresolved requirements, placeholders, unsupported claims, or missing declarations.

Block:

- If `[NEED: ...]` or `[CITE: ...]` remains in submission-facing text, mark the package blocked.
- If target-journal requirements are unknown, route to `sci-journal-landscape` before final submission packaging.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Submission checklist` or `Rebuttal matrix`.
- `Cover letter/rebuttal draft` when requested.
- `Required manuscript changes`.
- `Additional evidence/citation needs`.
- `Risk flags before submission/resubmission`.

Read `references/submission-revision-schema.md` for templates.
