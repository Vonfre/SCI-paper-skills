# Journal Intelligence And Benchmarking

## Contents

- Research Sequence
- Search Tactics
- Benchmark Paper Selection
- Dossier Template
- Quality Bar

Use this reference when researching the target SCI journal and comparable papers.

## Research Sequence

1. Resolve identity
   - Exact journal title.
   - Publisher or society.
   - ISSN/eISSN.
   - Official website and author guidelines URL.
   - Submission system URL.
   - Warning signs: copied titles, unrelated publisher domain, fake impact factor claims, inconsistent ISSN, or no editorial board.

2. Capture journal profile
   - Aims and scope.
   - Article types accepted.
   - Audience and disciplinary positioning.
   - Editorial priorities and stated novelty requirements.
   - Review model and publication timeline if available.
   - Indexing claims: SCIE, MEDLINE/PubMed, Scopus, DOAJ, PMC, etc.
   - Metrics: Journal Impact Factor, CiteScore, SJR/quartile, h-index, or official alternatives. Record source and year.

3. Verify publication model
   - Fully open access, hybrid, delayed OA, or subscription.
   - APC amount, currency, taxes, waivers, discounts, society/member rates.
   - License options: CC BY, CC BY-NC, etc.
   - Whether accepted manuscripts, preprints, or data deposits are allowed.

4. Extract author requirements
   - Article type definitions and limits.
   - Abstract format: structured/unstructured, headings, word count.
   - Main-text word count and section order.
   - Figure/table count, image resolution, color policy, file formats.
   - Reference style, maximum references, citation format.
   - Title length, running title, keywords, highlights, graphical abstract.
   - Supplementary-material naming, in-text citation pattern, and separate file requirements.
   - Data/code availability, ethics, consent, animal approvals, clinical trial registration.
   - Reporting guidelines: CONSORT, PRISMA, STROBE, ARRIVE, MIAME, MDAR, CHEERS, etc.
   - AI-use, conflict-of-interest, funding, author contribution, and acknowledgments policies.

5. Build a journal format profile
   - Exact in-text main figure form: `Fig. 1`, `Figure 1`, `Fig 1`, or another required form.
   - Exact panel form: `Fig. 1A`, `Fig. 1a`, `Figure 1A`, panel ranges, and multi-panel punctuation.
   - Exact table, supplementary figure, supplementary table, supplementary data, and source-data callouts.
   - Whether callouts are parenthetical, narrative, or both; whether a sentence may start with abbreviated `Fig.`.
   - Figure legend and table title style.
   - Abstract/headings, Methods placement, declaration headings, reference style, and supplement file naming.
   - Rule source for each item: official instruction, same-journal benchmark, peer-journal fallback, or unknown.

## Search Tactics

Use several independent searches rather than one broad query:

- Official site: `<journal name> aims scope author guidelines`.
- OA/APC: `<journal name> article processing charge open access license`.
- Indexing/metrics: `<journal name> impact factor`, `<journal name> Journal Citation Reports`, `<journal name> CiteScore`, `<journal name> DOAJ`.
- Same-journal papers: `site:<journal-domain> <topic keywords> <article type>`.
- Database searches: PubMed, Crossref, Europe PMC, Google Scholar, publisher search, and journal issue archive.

Prefer newest papers first, but do not sacrifice topical similarity. If the user's topic is rare, broaden in this order:

1. Same journal + same article type + same topic.
2. Same journal + same article type + adjacent topic.
3. Same journal + same broad field + similar method or claim.
4. Same publisher family + same journal section or sister journal only when same-journal material is unavailable.

## Benchmark Paper Selection

Select 3-8 papers. For each, record:

- Full citation and DOI.
- Article URL and PDF/full-text availability.
- Publication date.
- Article type.
- Why it is relevant to the user's manuscript.
- Sections/headings.
- Abstract structure and approximate length.
- Figure/table count and story sequence.
- Supplementary files and in-text citation pattern.
- Figure/table/supplement callout behavior, including capitalization, periods, spacing, panel letters, and parenthetical versus narrative placement.
- Reference count and citation style.
- Data/code/ethics statements.
- Language features: novelty framing, hedging, transition phrases, claim strength.

## Dossier Template

Use this structure in the output or local files:

```markdown
## Target Journal Dossier

## Identity
- Journal:
- Publisher:
- ISSN/eISSN:
- Official website:
- Author guidelines:
- Submission system:
- Retrieval date:

## Positioning
- Aims and scope:
- Audience:
- Preferred article types:
- Editorial fit signals:
- Desk-rejection risks:

## Metrics And Indexing
- Impact factor / year / source:
- CiteScore / year / source:
- Quartile or ranking / source:
- Indexing:
- Verification notes:

## Publication Model
- OA/hybrid/subscription:
- APC:
- License options:
- Waiver/discount notes:

## Author Requirements
- Article type:
- Word limits:
- Abstract:
- Sections:
- Figures/tables:
- References:
- Supplementary materials:
- Data/code availability:
- Ethics/reporting:
- Required declarations:

## Journal Format Profile
| Rule Area | Required Form | Source Basis | Unknowns |
|---|---|---|---|
| Main figure callout | | official / benchmark / fallback / unknown | |
| Main figure panel | | official / benchmark / fallback / unknown | |
| Multiple figures | | official / benchmark / fallback / unknown | |
| Main table callout | | official / benchmark / fallback / unknown | |
| Supplementary figure/table/data | | official / benchmark / fallback / unknown | |
| Figure legends and table titles | | official / benchmark / fallback / unknown | |
| Abstract, headings, Methods, declarations | | official / benchmark / fallback / unknown | |
| Reference style | | official / benchmark / fallback / unknown | |

## Benchmark Papers
| Paper | Year | Article Type | Why Included | Structure | Figures | Supplement Pattern | Voice Notes |
|---|---:|---|---|---|---|---|---|

## Journal Voice Model
- Title patterns:
- Abstract logic:
- Introduction moves:
- Results narrative:
- Discussion moves:
- Claim style:
- Citation behavior:
- Figure/table callout behavior:
- Supplement behavior:

## Implications For This Manuscript
- Fit verdict:
- Recommended article type:
- Story spine:
- Required changes:
- Missing information:
```

## Quality Bar

Do not output a generic journal summary. The dossier must explain how the journal facts change the user's manuscript strategy.

Good analysis says: "Because the benchmark papers introduce the disease burden in one paragraph and move quickly to the mechanistic gap, this manuscript should avoid a broad textbook opening and use the first page to establish the unresolved mechanism."

Weak analysis says: "The journal publishes high-quality papers and the manuscript should be well written."
