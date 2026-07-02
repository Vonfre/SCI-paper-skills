#!/usr/bin/env python3
"""Create a local scaffold for the final SCI manuscript coaching workflow."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "journal-project"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create templates for the final SCI manuscript workflow."
    )
    parser.add_argument("--journal", required=True, help="Target journal name")
    parser.add_argument("--topic", default="", help="Research topic or short project label")
    parser.add_argument("--out", default=".", help="Output directory")
    args = parser.parse_args()

    journal = args.journal.strip()
    topic = args.topic.strip()
    today = date.today().isoformat()
    root = Path(args.out).expanduser().resolve() / slugify(
        f"{journal}-{topic}" if topic else journal
    )

    folders = [
        "00-stage-diagnosis",
        "01-intake",
        "02-journal-landscape",
        "03-literature-evidence",
        "04-result-to-claim",
        "05-core-story",
        "06-figure-story",
        "07-storyline-planning",
        "08-reviewer-simulation",
        "09-draft-mimic",
        "10-paragraph-coach",
        "11-language-polish",
        "12-citation-control",
        "13-submission-revision",
        "14-deconstruction-archive",
    ]
    for folder in folders:
        (root / folder).mkdir(parents=True, exist_ok=True)

    write_file(
        root / "PROJECT.md",
        f"""# SCI-paper-skills Project

Journal: {journal}
Topic: {topic or "[NEED: research topic]"}
Created: {today}

## Current Status
- Stage:
- Next skill:
- Blocking gaps:
- Next 30-minute task:

## Handoff Artifacts
- 00-stage-diagnosis/stage-diagnosis.md
- 01-intake/intake-brief.md
- 02-journal-landscape/journal-landscape.md
- 03-literature-evidence/evidence-map.md
- 04-result-to-claim/result-to-claim-matrix.md
- 05-core-story/story-decision-memo.md
- 06-figure-story/figure-story-map.md
- 07-storyline-planning/storyline-plan.md
- 08-reviewer-simulation/reviewer-risk-report.md
- 09-draft-mimic/draft-package.md
- 10-paragraph-coach/paragraph-coach.md
- 11-language-polish/polish-report.md
- 12-citation-control/citation-map.md
- 13-submission-revision/submission-checklist.md
""",
    )

    write_file(
        root / "00-stage-diagnosis" / "stage-diagnosis.md",
        f"""# Manuscript Stage Diagnosis

Journal: {journal}
Topic: {topic or "[NEED: research topic]"}
Created: {today}

## Current Stage

## Why

## Do Not Do Yet

## Next Best Action

## Route
- Next skill:
- Input needed:
- Expected output:

## 30-Minute Task For User

## Missing Information
""",
    )

    write_file(
        root / "01-intake" / "intake-brief.md",
        f"""# SCI Workflow Intake Brief

## User Goal
- Target journal or journal level: {journal}
- Research field/topic: {topic or "[NEED: research topic]"}
- Model system/material:
- Article type:
- Manuscript stage:
- User experience level:
- Desired output:

## Available Inputs
- Scientific question:
- Main conclusions:
- Key figures/cases:
- Result-to-claim clarity:
- Storyline clarity:
- Existing outline/draft:
- Uploaded papers/PDFs:
- Deadline:

## Missing Inputs
- Required before journal landscape:
- Required before literature evidence:
- Required before result-to-claim:
- Required before core story:
- Required before figure story:
- Required before storyline planning:
- Required before reviewer simulation:
- Required before drafting:
- Required before final polish:

## Route
- Next skill:
- Reason:
- First action:
""",
    )

    write_file(
        root / "02-journal-landscape" / "journal-landscape.md",
        f"""# Journal Landscape

## Target Journal Portrait
- Journal: {journal}
- Publisher:
- Official site:
- Author instructions:
- Scope:
- Article types:
- Metrics/indexing:
- OA/APC:
- Novelty/evidence threshold:
- Desk-rejection risks:

## Same-Journal Similar Papers
| Paper | Year | DOI/URL | Similarity | What It Did | Structure/Style Notes | Relevance |
|---|---:|---|---|---|---|---|

## Peer-Journal Fallback Papers
| Journal | Why Comparable | Paper | Year | What It Did | Usefulness |
|---|---|---|---:|---|---|

## Landscape Opinion
- Field saturation:
- Open gap:
- Target-journal fit:
- Needed evidence:
- Recommended next step:

## Search Log
| Query | Source | Date | Result |
|---|---|---|---|
""",
    )

    write_file(
        root / "03-literature-evidence" / "evidence-map.md",
        """# Literature Evidence Map

| User Conclusion/Question | Claim Type | Supporting Literature | Conflicting/Alternative Literature | Support Level | Missing Evidence | Writing Recommendation |
|---|---|---|---|---|---|---|

## Possible Directions
| Direction | Prior Literature Did | Remaining Gap | Required Experiments/Data | Target-Journal Fit | Risk |
|---|---|---|---|---|---|
""",
    )

    write_file(
        root / "04-result-to-claim" / "result-to-claim-matrix.md",
        """# Result-To-Claim Matrix

| Result/Figure | What It Directly Shows | Defensible Claim | Claims It Does Not Yet Support | Evidence Gap | Safe Wording | Stronger Wording If Fixed |
|---|---|---|---|---|---|---|

## Evidence Gap Advisor
| Desired Claim | Current Evidence | Minimum Fix | Stronger Fix | Priority |
|---|---|---|---|---|
""",
    )

    write_file(
        root / "05-core-story" / "story-decision-memo.md",
        """# Core Story Decision Memo

## Candidate Stories
| Story | Type | One-Sentence Takeaway | Evidence Strength | Journal Fit | Risk | Recommendation |
|---|---|---|---|---|---|---|

## Recommended Core Story
- Core message:
- Why this is the best story:
- Target audience:
- What to emphasize:
- What to avoid:

## Manuscript Boundary
- Main text:
- Supplement:
- Cut/defer:
""",
    )

    write_file(
        root / "06-figure-story" / "figure-story-map.md",
        """# Figure Story Map

## Recommended Figure Order
| Order | Figure/Case | Question Answered | Evidence Type | Direct Claim | Main/Supplement/Cut | Missing Panel/Control | Transition |
|---:|---|---|---|---|---|---|---|

## Results Section Skeleton
1. Section title:
   - Figure:
   - Purpose:
   - Claim:
   - Transition:
""",
    )

    write_file(
        root / "07-storyline-planning" / "storyline-plan.md",
        """# Storyline Plan

## Storyline Options
| Plan | Logic Type | Order | Strengths | Risks | Best Use |
|---|---|---|---|---|---|

## Recommended Plan

## Drafting Brief
- Title direction:
- Abstract logic:
- Introduction logic:
- Results logic:
- Discussion logic:
""",
    )

    write_file(
        root / "08-reviewer-simulation" / "reviewer-risk-report.md",
        """# Reviewer Risk Report

## Desk-Rejection Risk
- Verdict:
- Main reason:
- Fast fixes:

## Reviewer Objection Matrix
| Priority | Likely Objection | Reviewer Type | Why It Matters | Minimum Fix | Stronger Fix | Writing Fix Possible? |
|---:|---|---|---|---|---|---|

## Overclaim Audit
| Current Claim | Problem | Safer Claim | Evidence Needed For Strong Claim |
|---|---|---|---|
""",
    )

    write_file(
        root / "09-draft-mimic" / "draft-package.md",
        f"""# Draft Mimic Package

Target journal: {journal}
Topic: {topic or "[NEED: research topic]"}

## Style Brief
| Model Pattern | Observed In | Use In Draft | Adaptation |
|---|---|---|---|

## Title Options

## Abstract

## Section Drafts

## Placeholders
- [NEED: ]
- [CITE: ]
""",
    )

    write_file(
        root / "10-paragraph-coach" / "paragraph-coach.md",
        """# Paragraph Coaching

## Paragraph Type

## Purpose

## Required Inputs
- Data:
- Citation:
- Figure/table:
- Claim:

## Sentence Scaffold
1. Context/topic sentence:
2. Specific gap or question:
3. Evidence/result:
4. Interpretation:
5. Transition:

## Example Paragraph

## User Draft Feedback
| Issue | Why It Hurts | Fix |
|---|---|---|
""",
    )

    write_file(
        root / "11-language-polish" / "polish-report.md",
        """# Language Polish Report

## Polished Text

## Meaning Preservation
- Status:
- Caveats:

## Claim-Strength Changes
| Original | Polished | Reason |
|---|---|---|

## Remaining Placeholders
- [NEED: ]
- [CITE: ]
""",
    )

    write_file(
        root / "12-citation-control" / "citation-map.md",
        """# Claim-Evidence-Citation Map

| Manuscript Claim | Evidence Type | Citation Candidate | DOI/PMID | Placement | Style Status | Verification |
|---|---|---|---|---|---|---|

## Reference Risks
- Unsupported claim:
- Outdated citation:
- Missing primary source:
- Style issue:
""",
    )

    write_file(
        root / "13-submission-revision" / "submission-checklist.md",
        """# Submission Checklist

## Required Files
- [ ] Main manuscript
- [ ] Title page
- [ ] Figures
- [ ] Tables
- [ ] Supplementary files
- [ ] Cover letter
- [ ] Highlights/significance statement if required
- [ ] Graphical abstract if required
- [ ] Reporting checklist if required

## Compliance
- [ ] Article type and scope fit confirmed
- [ ] Word limits checked
- [ ] Abstract format checked
- [ ] Reference style checked
- [ ] Figure/table limits checked
- [ ] Supplement naming checked
- [ ] Data/code availability statement included
- [ ] Ethics/consent/animal approval statements included if relevant
- [ ] Funding/conflict/author contribution statements included
- [ ] All placeholders resolved
""",
    )

    write_file(
        root / "13-submission-revision" / "rebuttal-matrix.md",
        """# Rebuttal Matrix

| Reviewer | Comment | Issue Type | Response Strategy | Manuscript Change | Location | Evidence | Status |
|---|---|---|---|---|---|---|---|
""",
    )

    write_file(
        root / "14-deconstruction-archive" / "accepted-paper-card.md",
        """# Accepted Paper Deconstruction

## Final Identity
- Title:
- Journal:
- Article type:
- DOI:
- Publication date:

## What Worked
- Positioning:
- Structure:
- Figures:
- Citations:
- Supplement:
- Review response:

## Reusable Patterns
- Title/abstract:
- Introduction:
- Results:
- Discussion:
- Submission:
""",
    )

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
