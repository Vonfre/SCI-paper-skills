# Prompt And Research Patterns

Use this reference when a task needs reusable writing prompts, literature research, model-paper analysis, or multi-stage synthesis.

## Prompt Card

Every reusable writing operation should be framed as a prompt card:

| Field | What To Fill |
|---|---|
| Role | Manuscript director, journal analyst, literature mapper, reviewer, paragraph coach, or citation auditor. |
| Task | The exact writing/research operation to perform. |
| Inputs | User data, target journal, model papers, figures, claims, draft text, reviewer comments, or references. |
| Constraints | Evidence boundaries, journal rules, word/section limits, tone, language, and do-not-invent rules. |
| Method | Diagnosis, search ladder, comparison, extraction, drafting, review, or polishing. |
| Output Contract | Named artifact with tables/checklists/placeholders. |
| Verification | What must be checked before the text can be treated as reliable. |

If any field is missing, mark it with `[NEED: ...]` instead of silently assuming it.

## Research-Then-Writing Pattern

For journal, literature, and model-paper tasks:

1. Convert the user request into 3-8 research questions.
2. Search or inspect sources for each question.
3. Record a source ledger before writing.
4. Generate or revise the outline from the evidence.
5. Draft only the section the evidence can support.
6. Leave `[CITE: ...]` and `[NEED: ...]` placeholders for gaps.

This prevents a fluent draft from hiding weak evidence.

## Multi-Perspective Question Pattern

Before synthesis, ask what each perspective would need:

| Perspective | Question Type |
|---|---|
| Target-journal editor | Is this within scope, novel enough, and article-type appropriate? |
| Field expert | What prior work already did this or contradicts it? |
| Method reviewer | What controls, statistics, reproducibility details, or datasets are missing? |
| Mechanism reviewer | What causal or pathway claim is overextended? |
| Reader | What figure order makes the story understandable? |
| Citation auditor | Which claims lack precise source support? |

Use the answers to shape the next skill route.

## Source-Backed Outline Pattern

For any draft section, create a mini outline with:

- Section purpose.
- Key claim.
- User evidence.
- Literature support.
- Figure/table reference.
- Citation placeholders.
- Limitation or boundary statement.

If a paragraph cannot fill these fields, produce a skeleton rather than confident prose.

## Evaluation Pattern

Before handing off a major artifact, score it:

| Dimension | Check |
|---|---|
| Evidence fit | Does every strong claim have user data or primary literature? |
| Journal fit | Does the logic match target-journal scope and article type? |
| Traceability | Can each claim be traced to figure/data/source? |
| Novelty boundary | Are "first", "novel", and "mechanism" claims verified or softened? |
| Reader path | Does the order teach the story without hidden jumps? |
| Citation health | Are metadata, citation placement, and source roles controlled? |

Any failed check becomes either a blocker or a visible placeholder.
