# Zero-To-One SCI Manuscript Example

This example shows the final output of a full synthetic run of `SCI-paper-skills`: a user starts with rough results and no writing plan, then the orchestrator routes through the skill suite until complete English and Chinese manuscripts exist.

## Files

- `complete-manuscript.md`: the complete English SCI-style manuscript produced by the example run.
- `complete-manuscript.zh-CN.md`: the complete Chinese SCI-style manuscript produced by the same example run.
- `complete-manuscript.docx`: the checked English Word manuscript produced from the example run.
- `complete-manuscript.zh-CN.docx`: the checked Chinese Word manuscript produced from the same example run.
- `initial-user-brief.md`: the first message a user can paste after calling `$sci-paper-skills`.
- `complete-workflow.md`: the staged run showing which skill is called, what it consumes, what it produces, and how the next handoff is chosen.
- `final-package.md`: the manuscript package metadata behind the final manuscript: title decision, figure order, section map, citation audit, and readiness status.
- `../manuscript-state-example.yaml`: the final state snapshot for the same example.

## How To Use

1. Install the skill pack with `bash scripts/sync_codex_skills.sh`.
2. Read `complete-manuscript.md` and `complete-manuscript.zh-CN.md` first to see the actual bilingual paper output; open the DOCX files when you want to inspect Word line numbering and formatting.
3. Start a new Codex chat and invoke `$sci-paper-skills`.
4. Paste the brief from `initial-user-brief.md`.
5. Use `complete-workflow.md`, `final-package.md`, and `../manuscript-state-example.yaml` to inspect how the paper was built.

This is not a factual plant biology case study. It is a complete synthetic manuscript demonstration. All data, statistics, figures, journal instructions, and mechanistic interpretations must be replaced or verified in a real project.
