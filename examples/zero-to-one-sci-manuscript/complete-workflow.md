# Complete Zero-To-One Workflow

This is a compact run log for the demo brief. It shows the expected behavior of the orchestrator and the 14 stage skills. The text is synthetic; it demonstrates process, state coupling, and handoff discipline.

## Stage Map

| Stage | Skill | Consumes | Produces | Next |
|---:|---|---|---|---|
| 0 | `sci-stage-diagnosis` | rough user brief | stage diagnosis | `sci-intake-router` |
| 1 | `sci-intake-router` | target, topic, materials | intake brief | `sci-journal-landscape` |
| 2 | `sci-journal-landscape` | target journal and topic | journal fit and comparable-paper plan | `sci-literature-evidence` |
| 3 | `sci-literature-evidence` | questions and possible claims | source ledger and citation needs | `sci-result-to-claim` |
| 4 | `sci-result-to-claim` | result bullets | claim registry | `sci-core-story-finder` |
| 5 | `sci-core-story-finder` | claims and journal fit | central story | `sci-figure-story-builder` |
| 6 | `sci-figure-story-builder` | story and result inventory | figure story map | `sci-storyline-planner` |
| 7 | `sci-storyline-planner` | claims, figures, sources | section plan | `sci-reviewer-simulator` |
| 8 | `sci-reviewer-simulator` | storyline and claims | reviewer risk report | repair or `sci-draft-mimic` |
| 9 | `sci-draft-mimic` | model patterns, storyline, claims | draft package | `sci-paragraph-coach` |
| 10 | `sci-paragraph-coach` | section purpose and claim IDs | coached paragraph | `sci-language-polisher` |
| 11 | `sci-language-polisher` | draft paragraph | polished text and risk notes | `sci-citation-control` |
| 12 | `sci-citation-control` | claims, sources, draft | citation audit | `sci-submission-revision` |
| 13 | `sci-submission-revision` | draft, audit, journal needs | submission checklist | final repair |

## 0. Orchestrator And Stage Diagnosis

Call:

```text
$sci-paper-skills
```

User pastes `initial-user-brief.md`.

Expected output:

```markdown
Current manuscript stage: Claim unclear / journal fit unknown.
Best next skill: sci-intake-router.
Do not do yet: Do not draft an abstract before claim strength and figure order are controlled.
30-minute task: Convert each result bullet into one row with comparison, method, observation, statistics, and missing controls.

## Manuscript State Update
- Updated fields: project, current_stage, next_skill, global_blockers
- New IDs created: none
- Blockers: [NEED: exact sample sizes], [NEED: statistical tests], [CITE: ABA guard-cell pathway]
- Next skill: sci-intake-router
- User task: provide rough figure list and available statistics

## Handoff
- Consumed: initial user brief
- Produced: stage diagnosis
- Blockers: missing statistics and citation evidence
- Next: sci-intake-router
```

## 1. Intake

Call:

```text
$sci-intake-router
```

Expected output:

```markdown
Intake brief:
- Goal: build a target-journal-adaptive plant biology manuscript from rough result bullets.
- Target: The Plant Cell first; Plant Physiology as fallback if mechanistic depth is insufficient.
- Topic: DRK1 and ABA-induced stomatal closure in Arabidopsis guard cells.
- Available artifacts: result bullets, candidate figure list, target-journal preference.
- Missing inputs: [NEED: genotype details], [NEED: n values], [NEED: statistics], [NEED: raw figure panels], [NEED: verified DRK1 naming].

Route: sci-journal-landscape before drafting, because target-journal expectations determine evidence depth.
```

## 2. Journal Landscape

Call:

```text
$sci-journal-landscape
```

Expected output:

```markdown
Journal landscape:
- Fit verdict: Possible but risky.
- Why: The Plant Cell generally requires mechanistic depth, strong genetic evidence, and clear advance for plant biology readers.
- Fallback: Plant Physiology or a specialized plant stress/signaling journal if direct mechanism remains incomplete.
- Comparable-paper search plan:
  - same journal + guard cell + ABA signaling
  - same journal + kinase + stomatal closure
  - peer journal + ABA guard cell phenotype rescue
- Must prove:
  - Causal genetic link between DRK1 and ABA stomatal response.
  - Rescue or complementation is convincing.
  - ROS and qPCR results support pathway placement without overclaiming direct mechanism.

Blockers:
- [NEED: verify current author instructions, article type, figure limits, data policy, and APC/OA]
- [CITE: same-journal comparable paper]
```

Handoff route: `sci-literature-evidence`.

## 3. Literature Evidence

Call:

```text
$sci-literature-evidence
```

Expected output:

```markdown
Evidence map:
- Research question Q1: What pathways are established for ABA-induced stomatal closure?
- Research question Q2: What evidence is normally required to place a kinase in this pathway?
- Research question Q3: Are DRK-family kinases known in guard-cell signaling?

Source ledger:
- S1: [CITE: verified ABA guard-cell signaling review], supports background only.
- S2: [CITE: primary paper on ABA-induced ROS in guard cells], supports pathway context.
- S3: [CITE: comparable kinase/stomatal closure paper], supports expected evidence pattern.
- S4: [CITE: target-journal comparable article], supports structure and claim strength.

Evidence boundary:
- Current data can support "DRK1 is required for full ABA-induced stomatal closure under tested conditions."
- Current data cannot support "DRK1 directly regulates ABA signaling" unless direct pathway or substrate evidence is added.
```

Handoff route: `sci-result-to-claim`.

## 4. Result To Claim

Call:

```text
$sci-result-to-claim
```

Expected output:

```markdown
Result-to-claim matrix:

| Result | Direct observation | Safe claim | Stronger claim only if fixed |
|---|---|---|---|
| F1 stomatal aperture | drk1 remains more open after ABA | C1: DRK1 is required for full ABA-induced stomatal closure under tested conditions | DRK1 directly regulates ABA response |
| F2 complementation | DRK1 complementation partially restores closure | C2: the phenotype is linked to DRK1 disruption | DRK1 is sufficient for pathway restoration |
| F3 ROS imaging | drk1 shows weaker ABA-induced ROS signal | C3: DRK1 is associated with ABA-triggered ROS accumulation | DRK1 acts upstream of ROS production |
| F4 qPCR | ABA-responsive genes shift in drk1 | C4: DRK1 perturbation changes selected ABA-responsive transcripts | DRK1 controls ABA transcriptional program |

Evidence gaps:
- [NEED: sample size and statistical test for F1-F4]
- [NEED: independent mutant allele or complementation details]
- [NEED: pathway control to place DRK1 upstream/downstream of ROS]
- [CITE: literature establishing ABA-ROS-stomatal closure pathway]
```

Handoff route: `sci-core-story-finder`.

## 5. Core Story

Call:

```text
$sci-core-story-finder
```

Expected output:

```markdown
Recommended story ST1:
DRK1 supports ABA-induced stomatal closure in Arabidopsis guard cells, likely by contributing to the ROS-linked ABA response, but direct mechanism remains unresolved.

Why this story:
- It uses all four results without overclaiming.
- It fits a phenotype -> rescue -> pathway-associated signal -> transcript support arc.
- It leaves a clear repair path for a higher-impact journal.

Backup story:
DRK1 as a physiological modulator of guard-cell ABA sensitivity for a lower-risk plant physiology venue.

Manuscript boundary:
Do not use "directly regulates", "master regulator", or "novel mechanism" until direct pathway evidence is added.
```

Handoff route: `sci-figure-story-builder`.

## 6. Figure Story

Call:

```text
$sci-figure-story-builder
```

Expected output:

```markdown
Figure story map:
- F1 main: ABA stomatal aperture phenotype. Opens the story.
- F2 main: DRK1 complementation/rescue. Protects specificity.
- F3 main: ABA-induced ROS imaging. Adds pathway-associated signal.
- F4 supplement or main depending on quality: qPCR of ABA-responsive genes.
- F5 optional supplement: DRK1 expression/localization if available.

Reader path:
1. Is there a phenotype?
2. Is the phenotype linked to DRK1?
3. Is the phenotype connected to known ABA response biology?
4. How far can the pathway claim go?

Missing figure controls:
- [NEED: mock treatment controls]
- [NEED: exact ABA concentration and time course]
- [NEED: independent biological replicates]
```

Handoff route: `sci-storyline-planner`.

## 7. Storyline Planner

Call:

```text
$sci-storyline-planner
```

Expected output:

```markdown
Manuscript structure:
- Title: DRK1 supports ABA-induced stomatal closure in Arabidopsis guard cells.
- Abstract move order: background -> gap -> phenotype -> rescue -> ROS/transcript evidence -> bounded implication.
- Introduction: ABA guard-cell response -> kinase signaling gap -> DRK1 candidate -> study aim.
- Results:
  - SEC1/F1: drk1 shows impaired ABA-induced stomatal closure.
  - SEC2/F2: complementation partially restores ABA responsiveness.
  - SEC3/F3: DRK1 disruption attenuates ABA-induced ROS accumulation.
  - SEC4/F4: ABA-responsive marker genes are altered in drk1.
- Discussion: DRK1 as a contributor to ABA response, limits of pathway placement, next experiments.

Draft readiness: skeleton only until statistics and citations are verified.
```

Handoff route: `sci-reviewer-simulator`.

## 8. Reviewer Simulator

Call:

```text
$sci-reviewer-simulator
```

Expected output:

```markdown
Reviewer risk report:
- R1 major: Mechanistic claim exceeds evidence.
  - Minimum fix: soften mechanism language.
  - Stronger fix: add pathway ordering or substrate evidence.
- R2 major: Single mutant/rescue may not rule out background effects.
  - Minimum fix: detail complementation and segregation.
  - Stronger fix: independent allele or CRISPR line.
- R3 major: Statistics and replicate reporting are incomplete.
  - Minimum fix: add n, tests, exact P values, biological replicates.
- R4 moderate: Target-journal fit may be too ambitious without mechanistic novelty.
  - Minimum fix: position as physiological response with clear limits.

Decision: revise before submission.
```

Handoff route: repair blockers or proceed to `sci-draft-mimic` with visible placeholders.

## 9. Draft Mimic

Call:

```text
$sci-draft-mimic
```

Expected output:

```markdown
Style brief:
- Use phenotype-first Results headings.
- Keep claim verbs bounded: supports, contributes to, is required for full response under tested conditions.
- Place citations in background and boundary-setting locations, not as fake proof of DRK1.

Draft package:
- 3 title options.
- Abstract skeleton with [NEED] and [CITE] markers.
- Result subsection headings.
- One Results subsection scaffold for SEC1.
- Discussion paragraph plan.

High-risk claims:
- C1, C3, C4 require citation and statistics checks before strengthening.
```

Handoff route: `sci-paragraph-coach`.

## 10. Paragraph Coach

Call:

```text
$sci-paragraph-coach
```

Input paragraph:

```text
DRK1 directly regulates ABA signaling and controls stomatal closure. The mutant did not close stomata after ABA, and ROS was lower.
```

Expected output:

```markdown
Problem:
- "directly regulates" is too strong for current evidence.
- "did not close" is absolute and may overstate the phenotype.
- ROS result needs method, timing, statistics, and linkage to F3.

Coached paragraph:
ABA treatment reduced stomatal aperture in wild-type plants, whereas drk1 mutants retained a larger aperture under the same conditions ([NEED: ABA concentration, time point, n, statistical test]; Fig. 1). This phenotype was partially restored in the DRK1 complementation line (Fig. 2), supporting a role for DRK1 in the full ABA-induced closure response. Because ABA-induced ROS accumulation was also reduced in drk1 guard cells (Fig. 3), DRK1 may contribute to a ROS-linked branch of the guard-cell ABA response, although direct pathway placement requires additional evidence [CITE: ABA-ROS guard-cell pathway].
```

Handoff route: `sci-language-polisher`.

## 11. Language Polisher

Call:

```text
$sci-language-polisher
```

Expected output:

```markdown
Polished paragraph:
ABA treatment decreased stomatal aperture in wild-type plants, whereas drk1 mutants maintained a significantly larger aperture under the same treatment conditions ([NEED: ABA concentration, time point, n, statistical test]; Fig. 1). The partial restoration of this response in DRK1-complemented plants further links the phenotype to DRK1 disruption (Fig. 2). Together with the reduced ABA-induced ROS signal observed in drk1 guard cells (Fig. 3), these results support a role for DRK1 in the full guard-cell response to ABA, while leaving the precise pathway position to be resolved [CITE: ABA-ROS guard-cell pathway].

Meaning-change note:
- The claim was softened from direct regulation to evidence-bounded contribution.
```

Handoff route: `sci-citation-control`.

## 12. Citation Control

Call:

```text
$sci-citation-control
```

Expected output:

```markdown
Citation audit:
- C1 needs background citations for ABA-induced stomatal closure and a verified link to user data, not a literature citation as direct proof.
- C2 is supported by user complementation data; cite method/details if previously described.
- C3 needs ABA-ROS guard-cell pathway citations and careful wording.
- C4 needs citations for chosen marker genes if used as ABA-responsive genes.

Unsupported or risky:
- "DRK1 directly regulates ABA signaling" remains unsupported.
- "novel mechanism" remains unsupported.

Citation placement plan:
- Introduction: S1-S3 for ABA/guard-cell background.
- Results SEC3: S2 for interpreting ROS as ABA-response context.
- Discussion: S3-S4 for comparing expected evidence standards and limitations.
```

Handoff route: `sci-submission-revision`.

## 13. Submission Revision And Complete Manuscript Assembly

Call:

```text
$sci-submission-revision
```

Expected output:

```markdown
Complete manuscript assembly:
- Manuscript file: complete-manuscript.md.
- Included sections: title, authors, abstract, significance statement, keywords, Introduction, Results, Discussion, Materials and Methods, Data Availability, Funding, Author Contributions, Conflict Of Interest, Acknowledgements, Figure Legends, Supplementary Table, and References.
- Citation status: background references included and DOI redirects checked for the demo.
- Final readiness: complete synthetic demo manuscript.

Real-project caution:
1. Replace all synthetic DRK1 data before real submission.
2. Re-check every citation and journal instruction.
3. Add real raw data, figures, author details, funding, and policy statements.
```

The complete paper is shown in `complete-manuscript.md`. The final package metadata is shown in `final-package.md`. The final state snapshot is `../manuscript-state-example.yaml`.
