# Journal Format Profile

Use this profile whenever a target journal, article type, or benchmark-paper set is available. The goal is to make drafting and polishing obey the journal's concrete format rules, not a generic SCI style.

## Source Basis

Record each rule as one of:

- `official`: from current author instructions or publisher guidance.
- `benchmark`: observed in recent same-journal articles.
- `fallback`: inferred from peer-journal or publisher-family examples.
- `unknown`: not found; keep as `[NEED: ...]`.

Do not invent a rule. If official instructions and benchmark articles conflict, use the official rule and note the conflict.

## In-Text Figure And Table Callouts

Capture exact forms:

| Item | Journal Rule | Example From Source | Source Basis | Draft Rule |
|---|---|---|---|---|
| Main figure singular | | `Fig. 1` / `Figure 1` / `Fig 1` | | |
| Main figure panel | | `Fig. 1A` / `Fig. 1a` / `Figure 1A` | | |
| Multiple figures | | `Figs. 1 and 2` / `Figures 1, 2` | | |
| Table singular | | `Table 1` / `table 1` | | |
| Supplementary figure | | `Supplementary Fig. 1` / `Fig. S1` / `Supplemental Figure S1` | | |
| Supplementary table | | `Supplementary Table 1` / `Table S1` | | |
| Supplementary data/file | | `Supplementary Data 1` / `Data S1` | | |

Also capture:

- Whether callouts are usually parenthetical, narrative, or both.
- Whether there is a period after `Fig`.
- Whether there is a space between `Fig.` and the number.
- Whether panel letters are uppercase or lowercase.
- Whether panel ranges use `Fig. 1A-C`, `Fig. 1A, B`, or `Fig. 1A to C`.
- Whether a sentence may begin with `Fig.` or should use `Figure`.

## Section And Back-Matter Formatting

| Area | Journal Rule | Source Basis | Draft Rule |
|---|---|---|---|
| Article type | | | |
| Abstract | structured/unstructured, headings, word limit | | |
| Main headings | exact labels and order | | |
| Results subsection style | numbered/un-numbered, sentence case/title case | | |
| Methods placement | main text/end/supplement | | |
| Figure legends | `Figure 1.` vs `Fig. 1.`; title punctuation; statistics placement | | |
| Table titles/footnotes | | | |
| Reference style | numeric/name-year; bracket/parenthesis/superscript | | |
| Data/code statement | heading and placement | | |
| Ethics/funding/conflict statements | heading and placement | | |

## Format Rewrite Rules

Create a small replacement table before polishing:

| Wrong Or Mixed Form | Correct Journal Form | Scope |
|---|---|---|
| `Fig1` | | in-text only |
| `Figure 1A` | | in-text only |
| `Supplement Fig. 1` | | supplement callouts |
| `Table S1` | | supplement table callouts |

Rules:

- Normalize all figure/table/supplement callouts before final language polish.
- Do not change scientific meaning while changing format.
- Do not alter figure IDs (`F1`, `T1`) in state; only change manuscript-facing callout text.
- If a callout refers to a missing figure/table ID, flag it as a content problem, not only a format problem.

## Output Block

Return this block from `sci-journal-landscape` when format matters:

```markdown
## Journal Format Profile

### Source Basis
| Rule Area | Source | Date | Status |
|---|---|---|---|

### In-Text Callout Rules
- Main figure:
- Main figure panel:
- Main table:
- Supplementary figure:
- Supplementary table:
- Multiple items:
- Parenthetical/narrative behavior:

### Section And Back-Matter Rules
- Abstract:
- Heading order:
- Figure legends:
- References:
- Data/code/statements:

### Draft Rewrite Rules
| Mixed Form | Correct Form | Notes |
|---|---|---|

### Unknowns
- [NEED: ...]
```
