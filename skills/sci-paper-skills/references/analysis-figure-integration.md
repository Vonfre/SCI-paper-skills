# Analysis, Statistics, Figure, And Data Integration

Use this reference when a manuscript project includes raw data, analysis outputs, statistical tests, computational workflows, figures, source data, or data/code availability requirements. The goal is to connect analysis artifacts to manuscript claims without turning the writing workflow into ad hoc data analysis.

## Adjacent Skill Bridges

When the local environment has specialized skills, route the task to them rather than re-implementing their work inside `sci-paper-skills`:

| Need | Prefer Adjacent Skill | Return Artifact To SCI Workflow |
|---|---|---|
| File structure, format, quality, and preprocessing needs | `exploratory-data-analysis` | `analysis_registry.datasets` and quality risks |
| Test selection, assumptions, effect sizes, power, diagnostics | `statistical-analysis` or domain-specific modeling skill | `analysis_registry.statistical_plan` and `statistics_report` |
| Manuscript-grade plots, multi-panel figures, export QA | `scientific-visualization`, `matplotlib`, `plotly`, or `nature-figure` | `figure_registry.figures[].figure_contract` and export notes |
| Data Availability, repositories, accessions, FAIR checks | `nature-data` or journal-specific data policy check | `data_availability_plan` |
| Domain-specific analysis such as single-cell, bulk RNA-seq, imaging, metabolomics, phylogenetics | matching domain skill | verified analysis summary linked to claim IDs |

Do not require these adjacent skills when the user only needs writing advice. Use them when data, statistics, plotting, source data, or reproducibility affects claim strength.

## Analysis Evidence Gate

Before a result can support a manuscript claim, record:

- dataset or file provenance;
- preprocessing and exclusion rules;
- analysis script/software and version if known;
- comparison, endpoint, or metric;
- sample size and replicate unit;
- statistical test or model;
- assumption checks or diagnostic status;
- effect size or estimate with uncertainty when applicable;
- multiple-testing or post-hoc correction if applicable;
- whether the result is confirmatory, exploratory, or descriptive.

If any item is missing, the claim can still be drafted only with visible `[NEED: ...]` placeholders and bounded wording.

## Statistical Reporting Gate

Use the weakest honest statistical language:

- `trend` or `pattern`: exploratory, descriptive, or underpowered result.
- `difference` or `association`: test/model is appropriate, assumptions are acceptable or robust alternative used.
- `effect`: estimate, uncertainty, and effect size are reported.
- `predicts`, `regulates`, `drives`, or `causes`: requires design and evidence beyond statistical association.

Always prefer estimates, confidence/credible intervals, effect sizes, and replicate logic over p-values alone. Report non-significant and assumption-violating results honestly.

## Figure Contract

For each main figure, establish the contract before drafting Results text:

1. `Core conclusion`: one sentence the figure must defend.
2. `Evidence chain`: each panel has a unique role linked to a claim ID.
3. `Figure role`: discovery, mechanism, validation, comparison, robustness, method, resource, or clinical/biological relevance.
4. `Statistics and integrity`: n, replicate unit, error bars, tests/models, image handling, exclusions, and source data.
5. `Export and journal fit`: final size, editable text, readable fonts, color accessibility, vector/raster format, and target-journal callout style.

Cut or demote panels that do not support the figure's core conclusion.

## Data And Code Availability Gate

Before submission packaging, inventory every artifact needed to support the manuscript:

- raw data;
- processed data;
- figure source data;
- statistical-analysis tables;
- code/scripts/notebooks;
- models or weights;
- supplementary datasets;
- reused public datasets;
- restricted third-party or sensitive data.

For each artifact, record access route, repository or supplement location, identifier strategy, license/access restriction, and whether a formal dataset/software citation is needed. Do not invent DOIs, accession numbers, repository names, ethics approvals, or access conditions.

## Output Blocks

When analysis or figure quality matters, add compact blocks to the normal output:

```markdown
## Analysis Provenance
- Dataset/source:
- Analysis status:
- Statistical status:
- Reproducibility risks:

## Figure Contract
- Core conclusion:
- Linked claims:
- Panel roles:
- Missing source data/statistics:

## Data Availability Notes
- Supporting artifacts:
- Repository/accession status:
- Missing fields:
```
