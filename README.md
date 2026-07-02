# SCI-paper-skills

[English](README.md) | [简体中文](README.zh-CN.md)

`SCI-paper-skills` is a target-journal-adaptive Codex skill suite for turning real research results into a coherent SCI/SCIE manuscript.

It is designed for graduate students and researchers who already have data, figures, conclusions, a rough idea, a draft, model papers, or reviewer comments, but need help organizing logic, controlling claim strength, finding evidence, imitating target-journal structure, polishing language, and preparing submission or revision materials.

## Quick Install

Clone the repository, then sync all skill folders into your local Codex skills directory:

```bash
git clone https://github.com/Vonfre/SCI-paper-skills.git
cd SCI-paper-skills
bash scripts/sync_codex_skills.sh
```

By default, the script installs to `~/.codex/skills`. To install elsewhere:

```bash
CODEX_SKILLS_DIR=/path/to/skills bash scripts/sync_codex_skills.sh
```

After installation, invoke the orchestrator:

```text
$sci-paper-skills
```

The first response should ask only the next useful questions:

1. What journal do you want to submit to? If undecided, list candidate journals or target level.
2. What is your research topic, field, organism/material/system, and article type if known?
3. What do you already have: scientific question, conclusions, figures/data, outline, draft, PDFs/model papers, or reviewer comments?

If enough context is already provided, the skill proceeds directly and marks missing information with `[NEED: ...]`.

## Skill Index

| Status | Stage | Skill | Trigger | Main Artifact |
|---|---:|---|---|---|
| Stable | 0 | `sci-stage-diagnosis` | Unsure where the manuscript is stuck | Stage diagnosis |
| Stable | 1 | `sci-intake-router` | New project or incomplete context | Intake brief |
| Stable | 2 | `sci-journal-landscape` | Target journal, candidate journal, or journal-fit question | Journal landscape |
| Stable | 3 | `sci-literature-evidence` | Need support, conflict, gap, novelty, or direction evidence | Evidence map |
| Stable | 4 | `sci-result-to-claim` | Results/figures exist but claims are unclear | Result-to-claim matrix |
| Stable | 5 | `sci-core-story-finder` | Several possible conclusions or weak central message | Story decision memo |
| Stable | 6 | `sci-figure-story-builder` | Figures/tables/cases need ordering and main-vs-supplement decisions | Figure story map |
| Stable | 7 | `sci-storyline-planner` | Need manuscript structure or alternative logic plans | Storyline plan |
| Stable | 8 | `sci-reviewer-simulator` | Want editor/reviewer risk before submission | Reviewer risk report |
| Stable | 9 | `sci-draft-mimic` | Draft from model papers without copying wording | Draft package |
| Stable | 10 | `sci-paragraph-coach` | Need paragraph-level writing help | Paragraph coaching block |
| Stable | 11 | `sci-language-polisher` | Meaning is stable and expression needs polishing | Polish report |
| Stable | 12 | `sci-citation-control` | Need reference placement, evidence audit, or citation style | Citation audit |
| Stable | 13 | `sci-submission-revision` | Submission files, cover letter, reviewer response, or revision plan | Submission/revision package |

For a more detailed trigger and handoff map, see [docs/skill-index.md](docs/skill-index.md).

## Workflow

```text
diagnose -> intake -> journal landscape -> literature evidence -> result-to-claim
-> core story -> figure story -> storyline -> reviewer simulation
-> draft mimic -> paragraph coach -> language polish -> citation control
-> submission or revision
```

The orchestrator uses the stages in order unless the user explicitly asks for a specific module.

## Tight Workflow

The tight workflow layer adds stateful handoff rules so the skills work as a connected manuscript pipeline rather than isolated prompts.

- Shared state: [manuscript-state-schema.md](skills/sci-paper-skills/references/manuscript-state-schema.md)
- Stage contracts: [handoff-contracts.md](skills/sci-paper-skills/references/handoff-contracts.md)
- End-to-end routes: [end-to-end-runbooks.md](docs/end-to-end-runbooks.md)
- Complete example paper: [complete-manuscript.md](examples/zero-to-one-sci-manuscript/complete-manuscript.md)
- Example run notes: [zero-to-one-sci-manuscript](examples/zero-to-one-sci-manuscript/README.md)
- Final example state: [manuscript-state-example.yaml](examples/manuscript-state-example.yaml)

Every stage now consumes upstream state, updates its owned fields, preserves IDs such as `C#`, `F#`, `S#`, `SEC#`, and ends with `Manuscript State Update` plus `Handoff` blocks.

## Design Principles

- Diagnose before drafting.
- Treat journal fit, literature evidence, claim strength, and figure logic as separate gates.
- Produce a named handoff artifact at every stage.
- Use reusable prompt cards and source-backed outlines for complex writing tasks.
- Maintain source ledgers for literature, citation, novelty, and contradiction checks.
- Keep missing facts visible with `[NEED: ...]`.
- Keep unverified citations visible with `[CITE: ...]`.
- Imitate model-paper structure and rhetorical function, not distinctive wording.
- Use current web research for journal facts, policies, metrics, APC/OA, and recent literature.
- Never invent data, references, approvals, accession numbers, methods, findings, statistics, or journal requirements.

See [docs/design-principles.md](docs/design-principles.md) for the shared operating standards.
See [docs/inspiration-high-star-writing-research-projects.md](docs/inspiration-high-star-writing-research-projects.md) for external project patterns adapted into this suite.

## Repository Layout

```text
README.md
README.zh-CN.md
CHANGELOG.md
manifest.yaml
docs/
examples/
  zero-to-one-sci-manuscript/
scripts/
skills/
  sci-paper-skills/
  sci-stage-diagnosis/
  sci-intake-router/
...
```

Each skill folder follows the Codex skill shape:

```text
SKILL.md
agents/openai.yaml
references/
```

The installable skill folders live under `skills/`. Copy or sync the complete skill folders, not just individual `SKILL.md` files.

## Project Scaffold

The orchestrator includes a helper script:

```bash
python skills/sci-paper-skills/scripts/init_journal_project.py \
  --journal "The Plant Cell" \
  --topic "ABA stomatal closure" \
  --out ./journal-projects
```

Generated `journal-projects/` folders are local working artifacts and are ignored by Git.

## Validation

Run the local pack check:

```bash
bash scripts/validate_skill_pack.sh
```

The same check runs in GitHub Actions on pushes and pull requests. See [CHANGELOG.md](CHANGELOG.md) for release history and upgrade notes.

Before publishing larger skill changes, also validate each skill with the skill creator `quick_validate.py` tool. If the bundled runtime lacks PyYAML, use a system `python3` that has `yaml` installed.

## License

This project is released under the [MIT License](LICENSE).

## Adding A Skill

New modules should include:

- `SKILL.md` with `name` and `description` frontmatter.
- `agents/openai.yaml`.
- At least one focused file under `references/` when templates or quality rules are needed.
- One row in `manifest.yaml`.
- One row in [docs/skill-index.md](docs/skill-index.md).
- A clear handoff artifact that can feed another stage.
