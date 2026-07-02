# SCI Paper Skills

A novice-adaptive SCI/SCIE manuscript coaching skill suite for researchers who have scientific results but need help turning them into a coherent, target-journal paper.

The suite is designed as a manuscript mentor, not just a text generator. It helps users diagnose where a paper project is stuck, evaluate target-journal fit, connect conclusions to literature, convert results into defensible claims, build the central story, arrange figures, anticipate reviewer objections, draft by imitating model-paper structure, coach paragraph writing, polish expression, manage citations, and prepare submission or revision materials.

## Entry Point

Use:

```text
$sci-journal-paper
```

Main orchestrator:

```text
sci-journal-paper/
```

The orchestrator first asks:

1. What journal do you want to submit to? If undecided, what target level or candidate journals?
2. What is your research content and direction, including organism/material/system?
3. What do you already have: scientific question, conclusions, figures/data, outline, draft, or reviewer comments?

## Final Workflow

| Stage | Skill | Purpose |
|---:|---|---|
| 0 | `sci-stage-diagnosis` | Diagnose where the manuscript project is stuck and choose the next action. |
| 1 | `sci-intake-router` | Collect target journal, field, materials, and route the workflow. |
| 2 | `sci-journal-landscape` | Build target-journal portrait and find same-journal or peer-journal similar papers. |
| 3 | `sci-literature-evidence` | Search literature around scientific questions, conclusions, support, conflict, and gaps. |
| 4 | `sci-result-to-claim` | Convert results/figures into defensible manuscript claims and evidence gaps. |
| 5 | `sci-core-story-finder` | Identify the paper's central story and best angle for the target journal. |
| 6 | `sci-figure-story-builder` | Arrange figures, tables, and cases into a results narrative. |
| 7 | `sci-storyline-planner` | Plan manuscript logic, result order, and alternative structures. |
| 8 | `sci-reviewer-simulator` | Predict editor/reviewer objections and prioritize fixes. |
| 9 | `sci-draft-mimic` | Draft by imitating target-journal or user-provided model-paper structure without copying wording. |
| 10 | `sci-paragraph-coach` | Coach paragraph-level writing for Introduction, Results, Discussion, Abstract, figure legends, and cover letters. |
| 11 | `sci-language-polisher` | Polish scientific expression while preserving meaning and evidence boundaries. |
| 12 | `sci-citation-control` | Align claims, evidence, citation placement, and reference verification. |
| 13 | `sci-submission-revision` | Prepare submission materials, cover letters, checklists, reviewer responses, and revision plans. |

## Included Skills

- `sci-journal-paper`: final orchestrator.
- `sci-stage-diagnosis`: stage diagnosis and next-action selection.
- `sci-intake-router`: first-step questions and routing.
- `sci-journal-landscape`: journal profile and comparable-paper scan.
- `sci-literature-evidence`: literature support and research-direction mapping.
- `sci-result-to-claim`: result-to-claim conversion.
- `sci-core-story-finder`: central story selection.
- `sci-figure-story-builder`: figure/case narrative construction.
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
python sci-journal-paper/scripts/init_journal_project.py --journal "The Plant Cell" --topic "ABA stomatal closure" --out ./journal-projects
```

It creates a working folder with:

```text
00-stage-diagnosis/
01-intake/
02-journal-landscape/
03-literature-evidence/
04-result-to-claim/
05-core-story/
06-figure-story/
07-storyline-planning/
08-reviewer-simulation/
09-draft-mimic/
10-paragraph-coach/
11-language-polish/
12-citation-control/
13-submission-revision/
14-deconstruction-archive/
```

## Design Principles

- Ask only the next useful questions.
- Adapt to the user's actual stage and experience level.
- Never invent data, references, statistics, approvals, accession numbers, or findings.
- Separate user data, literature support, interpretation, and unsupported claims.
- Prefer evidence-backed specificity over generic writing advice.
- Treat drafting as the result of journal landscape, literature evidence, result-to-claim mapping, story selection, and figure narrative.
- Make every stage leave a handoff artifact for the next stage.

## Validation

Each skill is a standard Codex skill folder with:

```text
SKILL.md
agents/openai.yaml
references/
```

The final suite was validated with the skill creator `quick_validate.py` tool.
