# Citation Audit Schema

## Claim-Evidence-Citation Map

| Claim | Claim Type | Evidence Needed | Current Evidence | Citation Candidate | DOI/PMID/URL | Placement | Status |
|---|---|---|---|---|---|---|---|

Claim types:

- Background.
- Gap.
- Method precedent.
- Dataset/resource.
- Result from this manuscript.
- Mechanistic interpretation.
- Clinical/translational implication.
- Limitation.
- Novelty claim.

Evidence status:

- Verified.
- Needs primary source.
- Needs recent review.
- Needs user data.
- Unsupported.
- Too strong for evidence.
- Metadata unverified.

## Reference Triage

| Reference | Supports Which Claim | Source Type | Year | Strength | Concern | Action |
|---|---|---|---:|---|---|---|

## Source Ledger

| Source ID | Reference | DOI/PMID/URL | Year | Source Type | Metadata Verified? | Retraction/Status Checked? | Supports Claim IDs | Exact Evidence Location | Concern |
|---|---|---|---:|---|---|---|---|---|---|

## Evidence Match

| Claim | Source | Match Type | Citation Placement | Confidence | Needed Action |
|---|---|---|---|---|---|

Match types:

- Direct primary support.
- Indirect support.
- Background framing.
- Method precedent.
- Contradiction or alternative explanation.
- User-data support only.
- Weak or irrelevant.

## Citation Placement Rules

- Cite literature claims, not the user's own direct observations unless comparing to prior work.
- Cite methods, tools, databases, software, protocols, and reporting guidelines when expected.
- Avoid citing a review for a very specific experimental fact if a primary paper is available.
- Verify "first", "novel", "largest", "gold standard", and clinical-practice claims.
- Keep supplement citations consistent with target journal style.

## Final Citation Audit

- [ ] Every major background claim has support.
- [ ] Every novelty claim is verified or softened.
- [ ] Every method/tool/database has a citation if needed.
- [ ] Every reference exists and metadata are accurate.
- [ ] Exact evidence location is recorded where available.
- [ ] Retraction/status concerns are checked where possible.
- [ ] Reference style matches target journal.
- [ ] In-text citations and reference list agree.
- [ ] Supplement citations follow journal convention.
