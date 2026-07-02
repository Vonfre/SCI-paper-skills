#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${CODEX_SKILLS_DIR:-$HOME/.codex/skills}"

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

mkdir -p "$TARGET_DIR"

for skill in "${SKILLS[@]}"; do
  source_dir="$ROOT_DIR/$skill"
  target_dir="$TARGET_DIR/$skill"

  if [[ ! -f "$source_dir/SKILL.md" ]]; then
    echo "Missing SKILL.md: $source_dir" >&2
    exit 1
  fi

  rm -rf "$target_dir"
  cp -R "$source_dir" "$target_dir"
  echo "Installed $skill -> $target_dir"
done

echo "Installed ${#SKILLS[@]} SCI-paper-skills modules into $TARGET_DIR"
