# Citation Source Ledger Schema

Use this schema to connect manuscript claims, reference metadata, and exact evidence support.

## Claim Inventory

| Claim ID | Claim Text | Claim Type | Strength | Needs Citation? | Evidence Needed | Current Support |
|---|---|---|---|---|---|---|

Claim strength:

- Background.
- Observation.
- Association.
- Regulation.
- Mechanism.
- Causality.
- Validation.
- Application.
- Novelty.

## Source Ledger

| Source ID | Reference | DOI/PMID/URL | Year | Source Type | Metadata Verified? | Retraction/Status Checked? | Supports Claim IDs | Exact Evidence Location | Concern |
|---|---|---|---:|---|---|---|---|---|---|

Exact evidence location should be as specific as possible: page, figure, table, abstract sentence, methods section, result subsection, or supplement location.

## Evidence Match

| Claim ID | Source ID | Match Type | Citation Placement | Confidence | Needed Action |
|---|---|---|---|---|---|

Match type:

- Direct primary support.
- Indirect support.
- Background framing.
- Method precedent.
- Contradiction or alternative explanation.
- User-data support only.
- Weak or irrelevant.

Confidence:

- Verified.
- Plausible but metadata unverified.
- Needs primary source.
- Needs newer source.
- Too strong for source.
- Unsupported.

## Final Citation Health Checks

- Every precise mechanism or causal claim has primary support or is softened.
- Every novelty claim has negative-search evidence or is softened.
- Reviews are not used as sole support for precise experimental facts.
- Preprints are labeled appropriately when journal context requires caution.
- Retractions, expressions of concern, and metadata mismatches are checked when possible.
- Citation placement is adjacent to the claim it supports.
