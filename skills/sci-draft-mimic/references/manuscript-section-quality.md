# Manuscript Section Quality Standards

Use these standards before drafting or revising a full manuscript, Introduction, Results, Discussion, or Materials and Methods section.

## Introduction

Write the Introduction as a literature-backed funnel, not a generic opening.

Default paragraph budget:

- Use 4 natural paragraphs for concise Nature Communications/PNAS-like research articles unless comparable papers show a different norm.
- Expand to 5-6 only when the target journal or model papers use longer field framing.

Required sequence:

1. Research background and current field status, with sources grouped by role rather than pasted as a list.
2. The central problem, gap, or scientific question that follows from the current status.
3. The concrete difficulty, boundary, or technical/biological details that make the problem nontrivial.
4. This study's viewpoint, objective or hypothesis, design, and contribution, stated without inflated novelty.

Quality checks:

- Every paragraph should have a citation role: background, mechanism, gap, contradiction, method precedent, or target-journal framing.
- Use reviews for framing and primary papers for precise mechanisms.
- Do not let the gap appear only in the final sentence; build toward it.
- Avoid formulaic or conversational contribution openers such as `Here, we...`; use a gap-linked bridge such as `To address this challenge...` or `To address this need...` when introducing the study.
- Avoid textbook openings when the target field already has a mature literature.

## Results

Write Results around evidence, not only around claims.

Default paragraph budget:

- Use named Results subsections.
- Each ordinary Results subsection should contain 2-3 natural paragraphs.
- Use 4 only for complex multiomics, resource-building, or multi-assay subsections when model papers justify it.
- If a subsection needs more than 3 paragraphs without justification, merge adjacent same-job paragraphs, split the subsection into smaller result questions, or move detail to Methods/Supplementary Material.

Each result subsection should contain:

1. Purpose sentence explaining why this experiment was done.
2. Experimental comparison, control, or named result object.
3. Direct observation, output, artifact, or module definition with figure/table citation where available.
4. Quantification, sample size/replicate logic, statistical test, or inspectable artifact details when known.
5. A concise reliability or transition sentence that connects to the next result.

For algorithm, software, workflow, platform, or resource-building Results, make invisible operations visible by turning each major action into a named result object, such as an evidence graph, resolver, scoring layer, refinement module, online interface, agent-callable wrapper, output table, evidence report, or quality-control layer. Keep the claim at the artifact/module level unless benchmark or validation data support a stronger performance claim.

For benchmark or head-to-head Results, the subsection should not read as a neutral list of all comparisons. Establish the fair shared task, lead with the strongest direct result, show robustness across groups or conditions, add any orthogonal comparator that expands the claim space, and then explain the distinctive feature that competitors do not provide. Exceptions, deployment wrappers, and sanity checks should be concise unless they change the central result, but they still need a conclusion-level number, count, margin, rank, or dispersion value if mentioned.

For result subsection headings, name the core finding rather than the action performed. Prefer concise finding-led headings over generic process titles, and for DOCX outputs ensure heading text remains black like the rest of the manuscript.

Allowed micro-discussion in Results:

- One short sentence at the end of a subsection may state what the result enables next.
- One short clause may explain why a control matters.
- Do not use Results to speculate broadly, review the field, or claim mechanism beyond the data.

## Discussion

Write Discussion as result-anchored expansion.

Default paragraph budget:

- Use 3-4 paragraphs for concise Nature Communications/PNAS-like research articles.
- Expand to 5-7 only when comparable papers use a broader discussion pattern.

Recommended movement:

1. Principal finding in one paragraph.
2. How the result fits, extends, or differs from prior work.
3. Mechanistic model or conceptual implication.
4. Alternative explanations and why the current data do or do not address them.
5. Strengths and limitations.
6. Future experiments that directly follow from unresolved claims.
7. Closing conclusion with evidence-matched wording.

Quality checks:

- Every broad implication must point back to a result ID or source ID.
- Limitations should sharpen the paper's boundary, not apologize vaguely.
- Future work should resolve a named uncertainty, not be a generic wishlist.

## Materials And Methods

Write Methods so another lab could reproduce the work.

Minimum reproducibility fields:

- Organism/sample/cohort identity, source, genotype/background, growth or inclusion criteria.
- Reagent identity, concentration, supplier/catalog when available.
- Treatment dose, duration, temperature, timing, buffer/media composition, and handling.
- Instrument model or platform, acquisition settings, and calibration when relevant.
- Biological and technical replicate definitions.
- Randomization, blinding, exclusion criteria, and quality-control rules when relevant.
- Quantification workflow, software names and versions, normalization, and thresholds.
- Statistical model, test choice, multiple-comparison correction, exact n, and definition of error bars.
- Data/code availability and accession numbers when applicable.

If details are missing, mark them with `[NEED: ...]`; do not fill them by guessing.
