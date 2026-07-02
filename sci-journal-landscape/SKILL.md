---
name: sci-journal-landscape
description: Target journal profile plus comparable-paper landscape scan for SCI manuscripts. Use after intake when the user provides a target journal and research direction, or asks whether a journal has similar papers; produce journal positioning, author requirements, OA/metrics, same-journal similar articles, same-level fallback articles when same-journal matches are absent, and a high-level strategic opinion for submission.
---

# SCI Journal Landscape

## Overview

Answer: what kind of journal is this, what does it actually publish, and how does the user's topic fit? Combine journal facts, author-rule constraints, comparable-paper scouting, and a strategic submission opinion.

## Required Inputs

- Target journal or candidate journals.
- Topic, field, organism/material/system, and main method.
- Intended article type if known.
- Main finding or expected contribution if available.

## Evidence Rules

Use current web research. Journal information and recent article lists change. Prioritize official journal/publisher pages, author instructions, PubMed/Crossref/DOI records, journal issue pages, and reputable metrics/indexing sources.

Always separate verified facts from inferred patterns. Include retrieval dates for journal facts.

## Search Strategy

Use layered searches rather than one broad query:

1. Exact journal identity and author rules from official sources.
2. Same journal plus topic keywords.
3. Same journal plus organism, material, or system.
4. Same journal plus method or claim type.
5. Same publisher/society family or same-level journals when same-journal matches are weak.

Do not say "no similar papers" until several query variants have been tried. If only peer-journal papers are found, label them as fallback evidence and explain why they are comparable.

## Search Ladder

1. Resolve the exact journal identity: title, publisher/society, ISSN/eISSN, official domain, submission system.
2. Capture author-facing constraints: scope, article types, limits, data/code/ethics/reporting requirements, APC/OA when relevant.
3. Search same-journal similar papers using topic, organism/material, method, mechanism, disease/context, and article type.
4. If same-journal matches are weak, search comparable journals and explain why they are comparable.
5. Score fit and state what the manuscript must prove to be plausible for the target.

## Fit Judgment

Use a plain verdict:

- `Strong`: scope, article type, novelty bar, and evidence depth plausibly match.
- `Possible but risky`: topic fits, but evidence depth, novelty, or audience breadth is uncertain.
- `Weak`: scope or article type mismatch is likely.
- `Unknown`: insufficient manuscript or journal evidence.

## Strategic Output

Always translate journal facts into writing strategy:

- How fast the introduction should move from broad context to exact gap.
- Whether the journal rewards mechanistic depth, resource value, method validation, field breadth, or conceptual novelty.
- What evidence would be expected in main figures.
- What should be moved to supplements or removed.

## State Coupling

Consume:

- `project.target_journal`, `candidate_journals`, `target_level`, `article_type`, `topic`, `field`, `organism_material_system`, and `main_methods`.
- Existing `source_ledger` only when previous sources are already available.

Update:

- `journal_landscape.journal_portrait`, `author_constraints`, `article_type_constraints`, `fit_verdict`, `manuscript_must_prove`, `retrieval_dates`, and `journal_blockers`.
- `journal_landscape.comparable_papers` using stable IDs `P1`, `P2`, `P3`.
- `source_ledger.sources` for official journal pages and comparable papers when cited.

Block:

- If no target journal or target level is known, route back to `sci-intake-router`.
- If topic keywords are too vague, produce a provisional landscape and mark `[NEED: topic keywords]`.

Always end with `Manuscript State Update` and `Handoff`.

## Output Contract

Return:

- `Target journal portrait`.
- `Same-journal article scan`.
- `Peer-journal fallback scan` if needed.
- `Journal fit rubric`.
- `Landscape opinion`: field saturation, gap, target-journal fit, needed evidence, recommended next step.
- `Search log`.

Read `references/landscape-output-schema.md` for the template.
