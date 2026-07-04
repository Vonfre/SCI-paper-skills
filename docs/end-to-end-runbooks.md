# End-To-End Runbooks

These runbooks show how the tight workflow should behave in common real manuscript situations. They complement `skills/sci-paper-skills/references/handoff-contracts.md`.

## Runbook 1: Results Exist, No Paper Logic

Use when the user has data, figures, or result bullets but cannot turn them into a paper.

1. `sci-stage-diagnosis`: classify stage and record the current blocker.
2. `sci-intake-router`: capture topic, system, target level, and available artifacts.
3. `sci-result-to-claim`: create claim IDs `C#` from every result/figure.
4. `sci-literature-evidence`: build source ledger `S#` for support, conflict, and novelty boundaries.
5. `sci-core-story-finder`: choose one story using claim IDs.
6. `sci-figure-story-builder`: assign figure IDs `F#` and map figures to claims.
7. `sci-storyline-planner`: create section IDs `SEC#`, paragraph plan, and a drafting brief.
8. `sci-reviewer-simulator`: repair blocking objections before drafting.
9. `sci-draft-mimic`: draft only sections whose claim/figure/source links are known.

Do not begin a confident full draft until `claim_registry`, `story`, `figure_registry`, and `storyline.paragraph_plan` exist.

## Runbook 2: Target Journal Known, Story Weak

Use when the user says "I want to submit to Journal X" but the manuscript angle is unclear.

1. `sci-intake-router`: collect journal, topic, system, article type, and materials.
2. `sci-journal-landscape`: create journal constraints, `journal_format_profile`, and comparable paper IDs `P#`.
3. `sci-literature-evidence`: identify journal-shaped gaps and source ledger `S#`.
4. `sci-result-to-claim`: normalize available results into claim IDs `C#`.
5. `sci-core-story-finder`: choose the strongest journal-fit story.
6. `sci-storyline-planner`: create a structure and paragraph plan that match the journal's article pattern and preserve exact figure/table/supplement callout rules for drafting.
7. `sci-reviewer-simulator`: test fit, novelty, evidence depth, and overclaiming.

If journal fit is weak, either lower the claim/story strength or route to a different journal before drafting.

## Runbook 3: Draft Exists, Needs Repair

Use when the user already has text and wants polishing, but the argument may be unstable.

1. `sci-reviewer-simulator`: identify structural, evidence, claim, and reviewer risks.
2. `sci-result-to-claim`: extract claim IDs from the draft when claims are not already mapped.
3. `sci-citation-control`: check whether each claim has an adjacent and appropriate source.
4. `sci-paragraph-coach`: rebuild weak paragraphs with claim/figure/source IDs.
5. `sci-language-polisher`: polish after meaning, claim strength, and journal-specific format are stable.
6. `sci-submission-revision`: prepare files, declarations, cover letter, or response matrix.

Do not language-polish unsupported claims into smoother but riskier statements.

## Runbook 4: Word Manuscript Requested

Use when the user asks for a `.docx` manuscript, line numbers, or Word-style formatting.

1. `sci-storyline-planner`: create or repair the paragraph plan before full-section drafting.
2. `sci-draft-mimic`: draft using the paragraph plan and target-journal/model-paper rhythm.
3. Create or convert the manuscript to DOCX.
4. Run `skills/sci-paper-skills/scripts/enforce_manuscript_docx_format.py input.docx output.docx`.
5. Run the same script with `--check`.
6. `sci-submission-revision`: record the Word/DOCX compliance result before calling the file ready.

Default Word profile: continuous line numbering, Times New Roman, black 12 pt text, 1.5 spacing, justified body paragraphs, and left-aligned headings.
