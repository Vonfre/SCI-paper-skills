# Shared Operating Standards

Use these standards when coordinating more than one SCI-paper-skills module.

## Stage Discipline

- Diagnose the earliest unresolved blocker before drafting.
- Route to one primary next skill unless the user explicitly asks for parallel outputs.
- Treat journal fit, literature evidence, claim strength, core story, figure logic, reviewer risk, draft quality, citation control, and submission compliance as different gates.
- If two stages seem plausible, choose the earlier blocker and explain why.

## Evidence Boundaries

- Do not invent data, references, approvals, accession numbers, methods, statistics, findings, or journal requirements.
- Separate verified facts, user-provided facts, literature support, interpretation, speculation, and unsupported claims.
- Use `[NEED: ...]` for missing user facts.
- Use `[CITE: ...]` for claims that need citation support.
- Use retrieval dates and source links when reporting current journal facts or recent literature.

## Handoff Artifact

Each stage should produce a named artifact with:

- Inputs used.
- Key decisions.
- Evidence or rationale.
- Missing information.
- Next recommended skill.
- One concrete user task when progress depends on the user.

## Shared State Discipline

- Read `manuscript_state` if it exists; otherwise initialize only the fields supported by the user's input.
- Preserve stable IDs across stages: claims `C#`, figures/tables `F#`/`T#`, sources `S#`, comparable papers `P#`, sections `SEC#`, reviewer issues `R#`.
- Each output must include `Manuscript State Update` and `Handoff` blocks.
- If a required upstream artifact is missing, mark the missing gate and produce a provisional artifact rather than inventing continuity.
- Do not rename, merge, or discard upstream IDs unless the output explicitly records the change.

## Drafting And Mimicry

- Draft only after the main gates are controlled, or label the draft as a skeleton.
- Imitate model-paper structure, rhetorical moves, section rhythm, and figure-citation behavior only.
- Do not copy distinctive wording, title formulas, sentence order, or phrasing from model papers.
- Keep claim strength no stronger than the result-to-claim matrix supports.
