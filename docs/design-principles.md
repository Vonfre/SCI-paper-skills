# SCI-paper-skills Design Principles

This repository treats manuscript writing as a staged evidence-control workflow, not as one-shot text generation.

## Shared Standards

1. Diagnose before drafting.
2. Keep journal fit, journal-specific formatting, literature support, analysis provenance, statistical credibility, claim strength, figure logic, citation control, data/code availability, and submission compliance as separate checks.
3. Ask only the next useful questions. Prefer three or fewer questions when context is missing.
4. Produce a named handoff artifact at every stage.
5. Read and update `manuscript_state` for every multi-stage workflow.
6. Preserve stable IDs for claims, figures, sources, sections, and reviewer issues.
7. Mark missing user facts as `[NEED: ...]`.
8. Mark unverified citation requirements as `[CITE: ...]`.
9. Separate user data, literature evidence, interpretation, speculation, and unsupported claims.
10. Keep claim strength proportional to evidence. Observation, association, regulation, mechanism, causality, validation, and application are different levels.
11. Use current web research for journal facts, author instructions, article lists, indexing, APC/OA, and recent literature.
12. Never invent data, references, approvals, accession numbers, methods, findings, statistics, repositories, software versions, or journal requirements, including figure/table/supplement callout rules.

## Drafting Gates

Full drafting should not begin until these gates are at least provisionally handled:

- Target journal or target level is known.
- Comparable-paper pattern is known or explicitly unavailable.
- Target-journal format profile is known or explicitly provisional.
- Literature support, conflict, and novelty boundaries are mapped.
- Data provenance, preprocessing, statistical tests/models, assumptions, effect sizes, uncertainty, and replicate units are recorded when results depend on analysis.
- Results are converted into defensible claims.
- One central scientific story is selected.
- Figures, tables, and supplements have a reader-facing order plus source-data, statistics, integrity, and export notes when submission-facing.
- Citation needs are visible.
- Data/code availability and dataset/software citation needs are visible when the manuscript is near submission.

If a user asks for drafting before these gates are ready, create a skeleton or partial draft with visible placeholders instead of inventing a complete manuscript.

## Handoff Rules

Every skill should end with:

- The named artifact it produced.
- `Manuscript State Update`.
- `Handoff`.
- What is verified.
- What is inferred.
- What is missing.
- The next best skill or a concrete user task.

This keeps the workflow inspectable and prevents hidden assumptions from turning into manuscript claims.

## State Coupling Rules

Each skill must define:

- what it consumes from `manuscript_state`;
- what it produces or updates;
- what blocks confident handoff;
- which next skill should run.

See `skills/sci-paper-skills/references/manuscript-state-schema.md` and `skills/sci-paper-skills/references/handoff-contracts.md`.

## Model-Paper Imitation Rules

Model papers are used to learn:

- Section order.
- Abstract move order.
- Introduction funnel shape.
- Results subsection rhythm.
- Figure citation behavior.
- Figure/table/supplement callout format.
- Discussion limitation style.
- Claim strength and hedging.
- Supplement organization.

Do not copy distinctive wording, title formulas, sentence sequences, or rhetorical signatures from model papers.

## Research And Prompt Patterns

High-quality writing assistance should use:

- reusable prompt cards with role, task, inputs, constraints, method, output contract, and verification;
- source-backed outlines before full prose;
- multi-perspective questions before literature synthesis;
- source ledgers that track metadata, evidence location, exactness, and confidence;
- reviewer scorecards before submission decisions.

## Analysis And Figure Integration Rules

When a project includes raw data, statistical outputs, analysis code, plots, or source-data files:

- route file exploration, test selection, modeling, plotting, or data-availability work to adjacent specialized skills when available;
- bring back only stable artifacts such as data-quality notes, statistical status, figure contracts, and repository/accession actions;
- treat p-values alone as insufficient for strong claims; require effect/estimate, uncertainty, sample size, replicate unit, and diagnostic status where relevant;
- make every main figure defend one core conclusion, with each panel linked to a claim and source data;
- block submission-readiness when source data, code, dataset citations, or data-availability routes remain unresolved.
