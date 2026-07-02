# SCI-paper-skills

`SCI-paper-skills` is a target-journal-adaptive skill suite for turning real research results into a coherent SCI/SCIE manuscript.

It is designed for graduate students and researchers who already have data, figures, conclusions, or a rough idea, but do not yet know how to organize the logic, support claims with literature, imitate the target journal's writing pattern, and prepare a submission-ready paper.

## Entry Point

Use the orchestrator:

```text
$sci-paper-skills
```

The first response should ask only the next useful questions:

1. What journal do you want to submit to? If undecided, list candidate journals or target level.
2. What is your research topic, field, organism/material/system, and article type if known?
3. What do you already have: scientific question, conclusions, figures/data, outline, draft, PDFs/model papers, or reviewer comments?

If enough context is already provided, the skill should proceed directly and mark missing information with `[NEED: ...]`.

## Core Workflow

| Stage | Skill | Job | Main Artifact |
|---:|---|---|---|
| 0 | `sci-stage-diagnosis` | Diagnose where the paper project is stuck. | Stage diagnosis |
| 1 | `sci-intake-router` | Collect journal, topic, system, materials, and route. | Intake brief |
| 2 | `sci-journal-landscape` | Profile target journal and find comparable papers. | Journal landscape |
| 3 | `sci-literature-evidence` | Check whether questions/conclusions are supported or contradicted. | Evidence map |
| 4 | `sci-result-to-claim` | Convert results and figures into defensible claims. | Result-to-claim matrix |
| 5 | `sci-core-story-finder` | Choose the central scientific story. | Story decision memo |
| 6 | `sci-figure-story-builder` | Arrange figures, tables, and cases into reader logic. | Figure story map |
| 7 | `sci-storyline-planner` | Design manuscript structure and alternative logics. | Storyline plan |
| 8 | `sci-reviewer-simulator` | Predict editor/reviewer objections before submission. | Reviewer risk report |
| 9 | `sci-draft-mimic` | Draft by imitating model-paper structure and rhetoric, not wording. | Draft package |
| 10 | `sci-paragraph-coach` | Teach and write section-level paragraphs. | Paragraph coaching block |
| 11 | `sci-language-polisher` | Polish expression while preserving meaning and evidence boundaries. | Polish report |
| 12 | `sci-citation-control` | Verify claim-evidence-reference alignment and style. | Citation audit |
| 13 | `sci-submission-revision` | Prepare submission files or reviewer-response materials. | Submission/revision package |

## How The Suite Adapts

- If the user has a target journal, it first builds a journal portrait and searches same-journal similar papers.
- If the target journal has no close matches, it searches same-level or peer-journal papers and explains why they are comparable.
- If the user has conclusions, it searches literature to support, challenge, or soften those conclusions.
- If the user has no conclusions, it proposes possible research directions grounded in recent literature.
- If the user has a writing logic, it improves that logic.
- If the user has no writing logic, it derives several possible manuscript structures from comparable literature and the user's evidence.
- If the user provides PDFs or model papers, it extracts structure, rhetorical moves, figure citation behavior, supplement style, and claim strength, then drafts by imitation without copying language.
- If the user has no writing experience, it gives one concrete next task instead of a long abstract checklist.

## Active Skills

- `sci-paper-skills`: main orchestrator and full workflow controller.
- `sci-stage-diagnosis`: stage diagnosis and next-action selection.
- `sci-intake-router`: first-step questions and routing.
- `sci-journal-landscape`: journal profile and comparable-paper scan.
- `sci-literature-evidence`: literature support, conflict, and direction mapping.
- `sci-result-to-claim`: result-to-claim conversion and evidence-gap control.
- `sci-core-story-finder`: central story selection.
- `sci-figure-story-builder`: figure and case narrative construction.
- `sci-storyline-planner`: manuscript logic planning.
- `sci-reviewer-simulator`: pre-submission reviewer-risk simulation.
- `sci-draft-mimic`: model-paper guided first drafting.
- `sci-paragraph-coach`: paragraph-level writing coaching.
- `sci-language-polisher`: final scientific-language polishing.
- `sci-citation-control`: citation and evidence control.
- `sci-submission-revision`: submission and revision support.

## Project Scaffold

The orchestrator includes a helper script:

```bash
python sci-paper-skills/scripts/init_journal_project.py   --journal "The Plant Cell"   --topic "ABA stomatal closure"   --out ./journal-projects
```

Generated project folders are working artifacts and are ignored by Git.

## Quality Rules

- Do not invent data, references, statistics, approvals, accession numbers, methods, findings, or journal requirements.
- Use current web research for journal facts, article lists, metrics, OA/APC, policies, and recent literature.
- Distinguish user data, literature support, interpretation, speculation, and unsupported claims.
- Match claim strength to evidence: observation, association, regulation, mechanism, causality, validation, and application are different.
- Draft only after journal fit, literature support, result-to-claim mapping, central story, figure logic, and citation needs are sufficiently clear.
- Keep every stage traceable by producing a handoff artifact for the next stage.

## Packaging Notes

- Generated `journal-projects/` folders are local working artifacts and are ignored by git.
- The final workflow uses the active 14-stage module set; removed legacy modules should not be reintroduced as working stages.
- Each active module keeps `SKILL.md` short and links to one-level `references/` files for templates and quality rules.

## Validation

Each skill is a standard Codex skill folder with:

```text
SKILL.md
agents/openai.yaml
references/
```

Validate each skill with the skill creator `quick_validate.py` tool before publishing changes. If the bundled runtime lacks PyYAML, use the system `python3` that has `yaml` installed.
