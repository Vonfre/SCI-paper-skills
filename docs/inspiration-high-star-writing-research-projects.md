# High-Star Writing And Research Project Patterns

Research date: 2026-07-02.

This note records external patterns adapted for `SCI-paper-skills`. Star counts are approximate GitHub UI counts observed on the research date and will change over time.

## Projects Reviewed

| Project | Approx Stars | Relevant Pattern | Adapted Into This Repo |
|---|---:|---|---|
| [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | 165k | Large prompt catalog, simple browsing, model-agnostic prompt examples, contribution flow. | Prompt cards and reusable stage templates. |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 76.1k | Prompt elements, techniques, RAG, evaluation, and risk sections. | Explicit prompt anatomy and verification steps. |
| [stanford-oval/storm](https://github.com/stanford-oval/storm) | 29.7k | Research before writing; multi-perspective question asking; outline first; citations from collected references. | Literature search question matrix and outline-before-draft discipline. |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 28k | Planner/executor/publisher split; source tracking; multiple research questions before report synthesis. | Research-plan ledger and source role control. |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 14.1k | Template-driven paper generation, automated review, and explicit responsible-use warnings. | Multi-reviewer rubric and disclosure/safety checks for AI-assisted manuscripts. |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 8.8k | Scientific-document RAG with metadata awareness, re-ranking, contextual summaries, and page-grounded answers. | Source ledger, page/location fields, contradiction flags, and citation confidence levels. |

## Patterns To Keep

1. Treat every writing task as a reusable prompt card:
   - role,
   - task,
   - context,
   - constraints,
   - evidence,
   - output contract,
   - verification.
2. Separate research planning, evidence gathering, synthesis, and writing.
3. Generate questions from multiple perspectives before deciding the outline.
4. Maintain a source ledger that records exact claim support, source role, metadata status, and evidence limits.
5. Use reviewer simulation as a structured scoring pass, not a loose critique.
6. Keep responsible-use checks visible when AI contributes materially to a manuscript.

## Patterns Not Adopted Directly

- Fully autonomous experiment execution is out of scope. This repository should not generate or run scientific experiments on behalf of the user.
- Broad web report generation is not enough for SCI writing; the workflow must still check user data, claim strength, figure logic, and target-journal fit.
- Star count is a discovery heuristic, not a quality guarantee. Scientific evidence control remains the primary standard.
