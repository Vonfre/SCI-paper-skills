# Zero-To-One SCI Manuscript Example

This example shows a full synthetic run of `SCI-paper-skills`: a user starts with rough results and no writing plan, then the orchestrator routes through the skill suite until a draftable manuscript package and submission checklist exist.

## Files

- `initial-user-brief.md`: the first message a user can paste after calling `$sci-paper-skills`.
- `complete-workflow.md`: the staged run showing which skill is called, what it consumes, what it produces, and how the next handoff is chosen.
- `final-package.md`: the final package produced by the run: title options, central claim, figure order, section plan, draft abstract, citation audit, and submission blockers.
- `../manuscript-state-example.yaml`: the final state snapshot for the same example.

## How To Use

1. Install the skill pack with `bash scripts/sync_codex_skills.sh`.
2. Start a new Codex chat and invoke `$sci-paper-skills`.
3. Paste the brief from `initial-user-brief.md`.
4. Compare the expected staged behavior in `complete-workflow.md`.
5. Use `final-package.md` as the shape of the output, replacing all demo content with verified project data.

This is not a factual plant biology case study. It is a workflow demonstration. All citations, exact statistics, journal instructions, and mechanistic interpretations must be verified in a real project.
