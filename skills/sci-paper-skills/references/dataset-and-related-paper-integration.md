# Dataset And Related-Paper Integration

Use this reference when a manuscript project depends on public datasets, benchmark datasets, repositories, database records, accession numbers, source data, software/model releases, or related-paper landscapes. The goal is to turn dataset and paper discovery into controlled manuscript evidence, not a loose list of URLs.

## When To Trigger

Trigger this bridge when the user asks to:

- find public datasets, source data, benchmark cohorts, single-cell atlases, expression resources, clinical cohorts, image sets, sequencing records, or repository accessions;
- decide whether a dataset is suitable for validation, comparison, reuse, or discussion;
- find related papers around a dataset, method, topic, organism, journal, or claim;
- cite datasets, software, models, databases, or code releases correctly;
- check whether a manuscript has enough external evidence, comparable-paper precedent, or data/code availability detail for submission.

If the user only needs prose polishing and no dataset or citation decision is involved, do not expand the workflow unnecessarily.

## Dataset Discovery Ladder

Use the most authoritative source available for the field. Prefer official repository or database records over secondary web pages.

1. Define the dataset need: discovery, independent validation, benchmark comparison, method demonstration, background context, or source-data deposit.
2. Search the official repository or domain database first, then broader scholarly indexes if needed.
3. Resolve stable identifiers: accession, DOI, repository ID, dataset version, release date, organism/system, assay/platform, license/access route, and restrictions.
4. Record sample or observation units, inclusion/exclusion logic, preprocessing state, and whether raw and processed data are both available.
5. Identify the dataset's companion paper or data descriptor when one exists.
6. Decide the manuscript role: primary user data, reused public data, validation dataset, benchmark, comparator, background resource, or citation-only source.
7. Mark gaps as `[NEED: ...]`; never invent accessions, dataset sizes, licenses, ethics approvals, or repository locations.

## Dataset Evidence Card

For every dataset that may affect a claim, create a compact card before using it in writing:

```yaml
- dataset_id: "D1"
  name_or_accession: ""
  repository: ""
  url_or_doi: ""
  companion_paper_source_id: "S# | [NEED: companion paper]"
  organism_material_system: ""
  data_type_platform: ""
  sample_size_and_unit: ""
  raw_processed_available: "raw | processed | both | unknown"
  preprocessing_or_qc_status: "verified | user-provided | needs check"
  license_access_restriction: ""
  manuscript_role: "primary | validation | benchmark | comparator | background | citation-only"
  linked_claim_ids: []
  linked_figure_ids: []
  suitability_verdict: "suitable | limited | unsuitable | unknown"
  main_limitations: []
  citation_requirement: "dataset citation | companion paper | repository URL | software/model citation | unknown"
```

## Related-Paper Search Ladder

Related-paper work should use retrieval before synthesis. Do not rely on remembered citations for DOI, PMID, journal, year, retraction status, or exact claim support.

1. Start with the user's exact topic, organism/system, method, dataset, and target journal.
2. Retrieve primary papers for precise findings, benchmark papers for methods or datasets, and reviews only for field framing.
3. For the top relevant papers, inspect both directions of the citation graph when available: references reveal foundations; citing papers reveal extensions, contradictions, and recent uptake.
4. Separate same-journal comparable papers, peer-journal comparable papers, method/dataset papers, and background reviews.
5. For every source, record its role: background, gap, direct claim support, conflicting evidence, method precedent, dataset descriptor, benchmark comparator, journal-style model, or discussion boundary.
6. Synthesize by theme and evidence relationship, not by listing papers one after another.

## Dataset-Paper Triangulation

Before a dataset or related paper becomes manuscript evidence, cross-check these relationships:

| Question | Required Record |
|---|---|
| Does the dataset have a companion paper or data descriptor? | Link `dataset_id` to `source_id`. |
| Does a related paper actually use the same organism, system, assay, or endpoint? | Record comparable basis and limits. |
| Does the paper support the exact claim or only a nearby premise? | Mark direct, indirect, conflicting, or framing. |
| Is the dataset suitable for the intended analysis? | Record sample unit, platform, preprocessing, access, and limitations. |
| Does the target journal require data/code availability or dataset citations? | Update `data_availability_plan` and `citation_audit`. |

If triangulation fails, the manuscript may still discuss the source, but it should not use it as strong evidence for a claim.

## Manuscript-State Updates

When this bridge is used, update or create these fields:

- `analysis_registry.datasets[]` for dataset provenance, type, preprocessing, and quality risks.
- `source_ledger.sources[]` for companion papers, related primary papers, reviews, methods papers, dataset descriptors, and official repository pages.
- `journal_landscape.comparable_papers[]` when related papers inform target-journal fit or structure.
- `claim_registry.claims[].citation_needs` and `linked_result_or_figure_ids` when datasets or related papers affect claim strength.
- `figure_registry.figures[].figure_contract` when a dataset supports a figure panel or benchmark.
- `data_availability_plan` for source-data, repository, code, model, and accession actions.
- `citation_audit.dataset_software_citation_issues` when dataset, software, database, model, or code citations are missing.

## Output Blocks

Add these compact blocks to the normal skill output when relevant:

```markdown
## Dataset Evidence Cards
| Dataset ID | Repository/Accession | Role | Linked Claims/Figures | Suitability | Missing Fields |
|---|---|---|---|---|---|

## Related-Paper Map
| Source ID | Paper/DOI/PMID | Role | Directness | Linked Claims | Notes |
|---|---|---|---|---|---|

## Dataset-Paper Triangulation
- Strong links:
- Weak or indirect links:
- Citation or data-availability actions:
- Claims that must remain provisional:
```

## Routing

- Dataset discovery or provenance unclear -> domain repository connector or adjacent data-analysis skill, then `sci-result-to-claim`.
- Related-paper search, novelty boundary, conflict, or background synthesis -> `sci-literature-evidence`.
- Dataset/software citation, metadata verification, or unsupported claim audit -> `sci-citation-control`.
- Target-journal comparable-paper patterns -> `sci-journal-landscape` and then `sci-storyline-planner`.
- Submission-facing repository, accession, code, source-data, or statement issues -> `sci-submission-revision`.
