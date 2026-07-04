# Changelog

All notable changes to `SCI-paper-skills` are documented here.

## Unreleased

## 0.6.9 - Regenerated DOCX Example And Skill Cleanup

- Regenerated the bilingual zero-to-one example with paragraph-plan discipline: 4-paragraph Introduction, 2-paragraph Results subsections, and 4-paragraph Discussion.
- Added checked English and Chinese DOCX manuscript examples produced from the regenerated manuscript and verified against the Word format profile.
- Updated manifest, README files, example package notes, and validation checks so DOCX examples are part of the published package.
- Removed the unused `init_journal_project.py` skill script and generated Python cache clutter from the skills tree.

## 0.6.8 - Word Manuscript Formatting And Paragraph Planning

- Added Word/DOCX manuscript formatting rules and an OOXML enforcement/check script for continuous line numbers, black 12 pt text, 1.5 spacing, justified body paragraphs, and left-aligned headings.
- Added paragraph-count planning across storyline, drafting, paragraph coaching, polishing, and submission checks, with Results subsections defaulting to 2-3 natural paragraphs.
- Calibrated default paragraph budgets from the two local bamboo reference papers: 1-paragraph abstract, 4-paragraph introduction, 2-3 paragraphs per Results subsection, 3-4-paragraph discussion, and subheaded Methods.
- Added analysis/statistics/figure/data-availability integration guidance inspired by local scientific analysis, visualization, and Nature-style skills.
- Extended manuscript state, handoff contracts, and downstream skills with analysis provenance, figure contracts, source-data checks, and data/code availability gates.
- Removed internal high-star project inspiration notes from the published documentation set.

## 0.6.7 - Target Journal Format Profile Gate

- Added a target-journal format profile for in-text figure/table/supplement callouts, legends, table titles, headings, references, and back-matter labels.
- Wired the format profile through journal landscape, drafting, polishing, citation audit, submission checks, shared state, handoff contracts, templates, and examples.
- Updated the complete demo state/package to show provisional `Fig. 1A`, `Figure 1.`, and `Supplementary Table 1` handling.

## 0.6.6 - Chinese GitHub README

- Made `README.md` the Chinese-first GitHub landing page.
- Removed the duplicate Chinese README file and simplified the root README around project purpose, skill modules, workflow, examples, and design principles.
- Moved away from README-level implementation details so the homepage focuses on what the skill suite does.

## 0.6.5 - cc-switch Install Discovery

- Updated the sync script to support `--target codex`, `--target ccswitch`, `--target both`, `--check`, `--pull`, `--prune`, and verified `rsync`-based installs.
- Documented the cc-switch storage mismatch that can make a GitHub skill repo appear registered while `sci-*` skills are not visible.
- Added cc-switch install and verification commands to both English and Chinese READMEs.

## 0.6.4 - Manuscript Quality Gates

- Strengthened writing skills with explicit quality gates for literature-backed Introductions, evidence-dense Results, result-anchored Discussions, and reproducible Methods.
- Added manuscript section quality standards to `sci-draft-mimic` and expanded evidence, paragraph, result-to-claim, and manuscript-output templates.
- Regenerated the bilingual complete manuscript example with a deeper Introduction, stronger result evidence packages, broader Discussion, and more reproducible Materials and Methods.

## 0.6.3 - Bilingual Paper-Format Example

- Reworked the zero-to-one example into true paper-format Markdown outputs instead of workflow-style prose.
- Added complete English and Chinese manuscript versions with Abstract/摘要, Introduction/引言, Results/结果, Discussion/讨论, Materials and Methods/材料与方法, declarations, figure legends, supplementary table, and references.
- Updated README files, manifest metadata, package validation, and final package metadata for the bilingual manuscript example.

## 0.6.2 - Complete Manuscript Example

- Added `complete-manuscript.md`, a full synthetic SCI-style paper generated from the example workflow.
- Updated the zero-to-one example so the complete manuscript is the primary artifact, with workflow trace and state as supporting files.
- Updated manifest metadata and validation checks to require the complete manuscript example.

## 0.6.1 - Complete Zero-To-One Example

- Reworked `examples/` around a complete synthetic zero-to-one SCI manuscript workflow.
- Added an initial user brief, staged skill-call run log, final manuscript package, and final `manuscript_state` snapshot.
- Updated README files, manifest metadata, and validation checks so the complete example is part of the published package.

## 0.6.0 - Release-Ready Project Polish

- Added `examples/` with a compact manuscript-state example.
- Added GitHub Actions validation workflow.
- Strengthened `scripts/validate_skill_pack.sh` to check packaged layout, manifest paths, skill names, required docs, examples, and accidental root-level skill folders.
- Removed version-specific wording from the skill index.

## 0.5.0 - Packaged Skills Layout

- Moved all installable skill folders under `skills/`.
- Updated README, Chinese README, manifest, validation script, and sync script for the packaged layout.
- Preserved file history as 100% renames.

## 0.4.0 - Stateful Tight Workflow

- Added `manuscript_state` schema.
- Added handoff contracts for every stage.
- Added end-to-end runbooks for common manuscript workflows.
- Added `State Coupling` sections to all skills.

## 0.3.1 - License Metadata

- Added MIT License.
- Added license sections to README files.
- Added `license: MIT` to `manifest.yaml`.

## 0.3.0 - Research And Evidence Patterns

- Added high-star project inspiration notes.
- Added prompt/research patterns, source ledger templates, citation source ledger schema, and multi-reviewer rubric.

## 0.2.0 - Productized Skill Pack

- Added install and validation scripts.
- Added docs, manifest, bilingual README, and packaged workflow descriptions.

## 0.1.0 - Initial Skill Suite

- Added the core SCI manuscript workflow and active skill modules.
