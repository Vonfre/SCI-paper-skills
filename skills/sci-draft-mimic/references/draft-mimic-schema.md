# Draft Mimic Schema

## Style Brief

| Model Pattern | Observed In | Use In Draft | Adaptation |
|---|---|---|---|
| Title pattern | | | |
| Abstract moves | | | |
| Introduction opening | | | |
| Paragraph counts | | | |
| Result transition | | | |
| Figure citation behavior | | | |
| Discussion limitation style | | | |

## Journal Format Profile

| Element | Required Journal Form | Source Basis | Applied In Draft | Unresolved Need |
|---|---|---|---|---|
| Main figure | | official / benchmark / fallback / unknown | | |
| Main figure panel | | official / benchmark / fallback / unknown | | |
| Multiple figures | | official / benchmark / fallback / unknown | | |
| Main table | | official / benchmark / fallback / unknown | | |
| Supplementary figure/table/data | | official / benchmark / fallback / unknown | | |
| Figure legends/table titles | | official / benchmark / fallback / unknown | | |

## Draft Output

```markdown
## Title Options

## Abstract
- Target paragraphs: 1

## Introduction
- Target paragraphs: 4 unless model papers justify another count
- Background paragraph with citations:
- Known mechanisms paragraph:
- Gap/question paragraph:
- Objective/contribution paragraph:

## Results
- Result subsection 1: target 2-3 natural paragraphs
- Result subsection 2: target 2-3 natural paragraphs
- Result subsection 3: target 2-3 natural paragraphs

## Discussion
- Target paragraphs: 3-4 for concise Nature Communications/PNAS-like papers unless model papers justify another count
- Principal findings:
- Relation to prior literature:
- Mechanistic interpretation:
- Alternative explanations:
- Limitations and future work:

## Materials and Methods
- Biological material/samples:
- Experimental conditions:
- Controls and replicates:
- Assay protocol:
- Quantification:
- Statistics:
- Software/equipment:
- Data availability:

## Placeholders
- [NEED: ...]
- [CITE: ...]
```

## Paragraph Plan

| Section/Subsection | Target Paragraphs | Drafted Paragraphs | Status | Basis |
|---|---:|---:|---|---|
| Abstract | 1 | | pass / needs repair | official / model / local baseline / fallback |
| Introduction | 4 | | pass / needs repair | official / model / local baseline / fallback |
| Result subsection | 2-3 | | pass / needs repair | official / model / local baseline / fallback |
| Discussion | 3-4 | | pass / needs repair | official / model / local baseline / fallback |

## Format Normalization Notes

| Mixed Or Provisional Form | Draft Form Used | Source Basis | Location | Follow-Up |
|---|---|---|---|---|
| `Fig1` / `Figure 1A` / `Fig. S1` | | official / benchmark / fallback / unknown | | |

## Word/DOCX Format Notes

| Element | Required | Applied | Status | Follow-Up |
|---|---|---|---|---|
| Line numbering | continuous | | pass / not checked / needs repair | |
| Font family | Times New Roman | | pass / not checked / needs repair | |
| Text color | black `000000` | | pass / not checked / needs repair | |
| Font size | 12 pt | | pass / not checked / needs repair | |
| Body alignment | justified | | pass / not checked / needs repair | |
| Title/heading alignment | left | | pass / not checked / needs repair | |
| Line spacing | 1.5 | | pass / not checked / needs repair | |

## Mimic Rules

- Imitate organization and rhetorical function, not exact language.
- Do not quote model papers unless the user specifically asks for short excerpts.
- Keep scientific claims tied to evidence.
- Preserve the user's data and meaning over superficial style matching.
- Do not write a full manuscript until each major section has its evidence role: Introduction uses source roles, Results uses data packages, Discussion uses result-anchored expansion, and Methods is reproducible.
- Do not write full major sections until paragraph counts and paragraph jobs are planned.
- Keep ordinary Results subsections to 2-3 natural paragraphs unless the paragraph plan records a justified exception.
- Do not mix figure/table/supplement callout styles; use the target journal profile or mark the rule as unresolved.
- Do not call a DOCX final until Word formatting, including Times New Roman font family, is applied and checked.
