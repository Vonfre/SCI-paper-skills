# Word Manuscript Format And Paragraph Plan

Use this reference when the user asks for a Word/DOCX manuscript, a full manuscript draft, section planning, model-paper imitation, or final submission formatting.

## Required DOCX Format

For Word manuscript outputs, enforce these defaults unless the target journal requires a different file format:

| Element | Required Setting |
|---|---|
| Line numbering | Continuous line numbers, count every line |
| Font family | Times New Roman for all manuscript text, including headings, hyperlinks, tables, legends, declarations, Chinese text, and complex-script runs |
| Text color | Black (`000000`) for all manuscript text, including headings, hyperlinks, tables, legends, and declarations |
| Font size | 12 pt for all manuscript text, headings, legends, tables, and references |
| Body alignment | Justified |
| Title and headings | Left aligned |
| Line spacing | 1.5 lines |

Do not call a Word manuscript final if line numbers, Times New Roman font, all-black text, 12 pt size, 1.5 spacing, justified body paragraphs, and left-aligned headings have not been checked.

## DOCX Implementation

When creating a new `.docx`, apply the formatting during document generation and then run the post-processor:

```bash
# Run from the sci-paper-skills skill folder, or resolve scripts/ relative to this reference.
python scripts/enforce_manuscript_docx_format.py input.docx output.docx
python scripts/enforce_manuscript_docx_format.py output.docx --check
```

Use the same script after converting Markdown, LaTeX, or another source into DOCX. The script enforces the OOXML equivalents:

- Section line numbering: `<w:lnNumType w:countBy="1" w:restart="continuous"/>`.
- Times New Roman font family: `<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>`.
- 12 pt font size: `<w:sz w:val="24"/>` and `<w:szCs w:val="24"/>`.
- Black text: `<w:color w:val="000000"/>`.
- 1.5 line spacing: `<w:spacing w:line="360" w:lineRule="auto"/>`.
- Justified body paragraphs: `<w:jc w:val="both"/>`.
- Left-aligned headings/title paragraphs: `<w:jc w:val="left"/>`.

If a target journal gives contradictory Word requirements, follow the journal and record the deviation in `document_output.word_format_profile`.

## Paragraph Plan Gate

Before drafting a full manuscript or a major section, create a paragraph plan. The plan should be based on, in priority order:

1. The target journal's official instructions if they specify section structure.
2. Same-journal or user-provided model papers.
3. The local bamboo-reference baseline below.
4. A clearly labeled fallback based on article type.

The paragraph plan must list each section or subsection, target paragraph count, paragraph job, linked claim/figure/source IDs, and the basis for the count.

## Local Bamboo-Reference Baseline

The local reference folder contained two bamboo research articles used as calibration papers: a Nature Communications haplotype pangenome paper and a PNAS single-nucleus/spatial transcriptomics paper. Their reusable pattern is:

| Section | Paragraph Budget | Planning Rule |
|---|---:|---|
| Abstract | 1 | One compact paragraph moving from context/gap to approach, main findings, and implication. |
| Introduction | 4 | Research background and current status; central problem/question; concrete difficulty, boundary, or technical/biological details; study viewpoint, objective, design, and main contribution. |
| Results overview | Named subsections | Do not write Results as one long block; each subsection should answer one scientific question. |
| Result subsection | 2-3 | Purpose/setup, direct evidence with statistics/figures, and short interpretation or bridge. Use 4 only for unusually complex multiomics or resource-building subsections. |
| Discussion | 3-4 | Principal findings; method/resource or mechanism significance; limitations/boundaries; conservation/application/future direction and closing. |
| Methods | Subheaded | Use reproducible method blocks. One concise paragraph per method block is acceptable; protocol-heavy work may use more subheaded paragraphs. |

For the user's stated preference, Results should default to 2-3 natural paragraphs per result subsection. If a draft exceeds this, split by figure/claim or move supporting detail into Methods/Supplementary Material.

## Paragraph Roles By Section

Use these roles when planning:

- Abstract: context/gap; approach; primary result sequence; interpretation and implication.
- Introduction: background/current status; problem/question; specific difficulty/details; viewpoint/objective/design/contribution.
- Result subsection: why tested; what was compared; what was observed; quantitative/statistical support; bridge to the next question.
- Discussion: main answer; relation to literature; mechanism/model or resource value; limitations/alternative explanations; future/application/conclusion.
- Methods: sample/material; protocol or computational workflow; quantification/statistics; software/data availability.

## State Updates

Record these fields when the workflow reaches planning, drafting, or Word output:

```yaml
storyline:
  paragraph_plan:
    basis: "official | model papers | local bamboo-reference baseline | fallback"
    reference_papers:
      - paper_id: "P1"
        paragraph_pattern: ""
    sections:
      - section_id: "SEC1"
        section_type: "results"
        target_paragraphs: "2-3"
        paragraph_roles: []
        linked_claim_ids: []
        linked_figure_ids: []
        basis_note: ""

document_output:
  requested_formats: ["docx"]
  word_format_profile:
    line_numbering: "continuous"
    font_family: "Times New Roman"
    text_color: "000000"
    font_size_pt: 12
    line_spacing: 1.5
    body_alignment: "justified"
    heading_alignment: "left"
    enforcement_script: "scripts/enforce_manuscript_docx_format.py"
    validation_status: "not checked | pass | needs repair"
```
