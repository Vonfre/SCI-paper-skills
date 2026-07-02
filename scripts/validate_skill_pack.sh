#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

SKILLS=(
  sci-paper-skills
  sci-stage-diagnosis
  sci-intake-router
  sci-journal-landscape
  sci-literature-evidence
  sci-result-to-claim
  sci-core-story-finder
  sci-figure-story-builder
  sci-storyline-planner
  sci-reviewer-simulator
  sci-draft-mimic
  sci-paragraph-coach
  sci-language-polisher
  sci-citation-control
  sci-submission-revision
)

required_root_files=(
  LICENSE
  README.md
  README.zh-CN.md
  manifest.yaml
  docs/end-to-end-runbooks.md
  docs/design-principles.md
  docs/skill-index.md
  scripts/sync_codex_skills.sh
  skills/sci-paper-skills/references/manuscript-state-schema.md
  skills/sci-paper-skills/references/handoff-contracts.md
)

for file in "${required_root_files[@]}"; do
  if [[ ! -f "$ROOT_DIR/$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

for skill in "${SKILLS[@]}"; do
  skill_dir="$ROOT_DIR/skills/$skill"

  [[ -f "$skill_dir/SKILL.md" ]] || { echo "Missing $skill/SKILL.md" >&2; exit 1; }
  [[ -f "$skill_dir/agents/openai.yaml" ]] || { echo "Missing $skill/agents/openai.yaml" >&2; exit 1; }
  [[ -d "$skill_dir/references" ]] || { echo "Missing $skill/references/" >&2; exit 1; }

  if ! grep -q '^name: ' "$skill_dir/SKILL.md"; then
    echo "Missing frontmatter name in $skill/SKILL.md" >&2
    exit 1
  fi

  if ! grep -q '^description: ' "$skill_dir/SKILL.md"; then
    echo "Missing frontmatter description in $skill/SKILL.md" >&2
    exit 1
  fi

  if ! grep -q '^## State Coupling' "$skill_dir/SKILL.md"; then
    echo "Missing State Coupling section in $skill/SKILL.md" >&2
    exit 1
  fi
done

echo "Validated ${#SKILLS[@]} SCI-paper-skills modules."
