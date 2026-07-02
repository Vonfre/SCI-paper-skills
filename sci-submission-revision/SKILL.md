---
name: sci-submission-revision
description: SCI journal submission package preparation, compliance checking, cover letters, declarations, supplementary-file organization, reviewer suggestions, reviewer-response strategy, rebuttal letters, revision plans, and post-decision manuscript repair. Use when the user is preparing files for submission, checking target-journal requirements, responding to editor or reviewer comments, resubmitting, or tracking changes after peer review.
---

# SCI Submission Revision

## Overview

Own the final mile from manuscript draft to journal submission and peer-review revision. This skill checks compliance, prepares submission materials, and converts reviewer comments into a precise response and revision plan.

## Submission Workflow

1. Confirm target journal and article type.
   - Use the journal landscape and author-rule constraints from `sci-journal-landscape`.

2. Build file inventory.
   - Main manuscript, title page, cover letter, figures, tables, supplements, graphical abstract, highlights, reporting checklists, declarations, and source data if required.

3. Check journal compliance.
   - Word limits, abstract format, section order, reference style, figure resolution, supplement naming, data/code availability, ethics, conflict, funding, author contributions, AI-use disclosure, and reporting guidelines.

4. Prepare cover letter and metadata.
   - State article type, title, fit to journal scope, core contribution, originality, approval by authors, conflicts, and required declarations.

5. Produce readiness verdict.
   - Ready, conditionally ready, or not ready.
   - List blocking issues separately from polish issues.

## Readiness Rule

Do not call a manuscript ready if any of these are unresolved:

- Target article type or journal requirements are unknown.
- Required statements are missing.
- Figures/supplements do not match journal rules.
- Major claims lack data or citation support.
- References are unverified.
- Placeholders remain in submission-facing text.

## Revision Workflow

1. Parse decision letter and reviewer comments.
   - Separate editor requirements, reviewer concerns, mandatory experiments/analyses, writing clarifications, and optional suggestions.

2. Build a rebuttal matrix.
   - Reviewer, comment, issue type, response strategy, manuscript change, location, evidence, and status.

3. Decide response strategy.
   - Agree and change, agree with clarification, respectfully disagree with evidence, add analysis, add limitation, or defer when outside scope.

4. Draft responses.
   - Be specific, polite, evidence-based, and traceable to manuscript changes.
   - Quote only short comment fragments if needed; avoid long verbatim reproduction unless the user provided the letter and needs a working response.

5. Prepare revised manuscript notes.
   - Identify where text, figures, tables, supplements, methods, or citations must change.

## Response Rule

Every reviewer response must map to one of three outcomes:

- Manuscript changed, with location.
- Additional analysis/experiment added, with location and evidence.
- No change made, with a concise evidence-based reason.

Do not promise data, experiments, or analyses the user has not performed.

## Output Contract

For submission:

- `Submission readiness verdict`.
- `Required file checklist`.
- `Compliance issues`.
- `Cover letter`.
- `Declarations and statements`.
- `Blocking missing inputs`.

For revision:

- `Reviewer-response strategy`.
- `Rebuttal matrix`.
- `Draft response letter`.
- `Manuscript change list`.
- `Additional evidence/citation needs`.

Read `references/submission-revision-schema.md` for templates.
