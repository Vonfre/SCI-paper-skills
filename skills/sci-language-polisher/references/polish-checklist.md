# Scientific Polishing Checklist

## Checkpoints

- Meaning unchanged.
- No new data or citations added unless the user explicitly asks for evidence or citation repair.
- Claim strength matches evidence.
- Causality is supported or softened.
- Novelty language is verified or softened.
- Paragraphs have clear topic and transition sentences.
- Results report evidence before interpretation.
- Discussion does not overstate findings.
- Terms are consistent.
- Journal style and word limits are respected.
- In-text figure/table/supplement callouts match `journal_format_profile`.
- Figure legend labels, table titles, headings, reference style, and declaration labels match target-journal rules or are marked unknown.

## Common Rewrites

| Problem | Fix |
|---|---|
| "plays an important role" | State the specific function or evidence |
| "significantly" without statistics | Remove or provide statistical result |
| "proved" | Use showed, demonstrated, suggested, or supported depending on evidence |
| Overbroad conclusion | Narrow to tested system and conditions |
| Blunt non-ideal result, such as "method A was worse in some datasets" | Keep the number, define the affected boundary, give an evidence-supported reason or condition, and return to the central result |
| Stiff transition such as "Accuracy was only one part of the result" | Replace with a finding-linked bridge that names the added evidence layer, such as inspectability, robustness, mechanism, validation, or biological interpretation |
| Literal Chinese-English phrasing | Rewrite in idiomatic scientific English |
| Formulaic or conversational contribution opener such as "Here, we present..." | Replace with a specific bridge, such as "To address this challenge...", "To address this need...", or another gap-linked transition that preserves continuity |
| `Fig1` or `Fig 1` when the journal requires `Fig. 1` | Normalize the figure callout and apply the same form throughout |
| `Figure 1A` when the journal requires abbreviated panel callouts | Rewrite as the required form, such as `Fig. 1A` |
| Mixed `Supplementary Fig. 1`, `Fig. S1`, and `Supplemental Figure S1` | Choose the target-journal supplementary form and apply it consistently |
| `Table S1` when the journal requires `Supplementary Table 1` | Rewrite the supplementary table callout and update the supplement inventory |
| Result subsection opens as a transition, such as "Next, we asked..." | Make the subsection self-contained by opening with the produced resource, evidence object, or analytical question |
| Main-figure prose lists panels without a through-line | Build a panel ladder: resource/source, representative case, grouping structure, functional interpretation, and real-data example; merge panels that serve one evidence layer |
| Secondary evidence becomes a mini-methods explanation | Keep only the result, key number/range, and supported conclusion; avoid explaining the metric or panel if it is not central to the paragraph |
| Interface or browser panel is described like an independent result | State which downstream data panel or case it lets readers inspect, then move quickly to the biological evidence |
| Re-clustering/refinement comparison reports counts before explaining logic | First contrast the decision rules, such as expression-neighbourhood partitioning versus graph-guided candidate identity scoring |
| Weak rare-state refinement is overstated | Use candidate or weakly marked rare-state wording and pair it with cell counts, purity/agreement, GO gene counts and FDR |
| GO or enrichment terms are used to support biology without wet-lab validation but lack citations | Add a concise literature-backed interpretation sentence and state the enrichment as a biological consistency check, not experimental validation or mechanistic proof |

## Output Notes

When helpful, include:

- `Before -> After` examples for recurring problems.
- A list of claims that still need data/citation.
- A list of figure/table/supplement callouts or headings that still need target-journal format verification.
- A concise note explaining tone changes.
