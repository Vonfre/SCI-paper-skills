#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

fail() {
  echo "ERROR: $*" >&2
  exit 1
}

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
  CHANGELOG.md
  docs/end-to-end-runbooks.md
  docs/design-principles.md
  docs/skill-index.md
  examples/README.md
  examples/manuscript-state-example.yaml
  .github/workflows/validate.yml
  scripts/sync_codex_skills.sh
  skills/sci-paper-skills/references/manuscript-state-schema.md
  skills/sci-paper-skills/references/handoff-contracts.md
)

for file in "${required_root_files[@]}"; do
  if [[ ! -f "$ROOT_DIR/$file" ]]; then
    fail "Missing required file: $file"
  fi
done

manifest_version="$(awk -F': *' '$1 == "version" {print $2; exit}' "$ROOT_DIR/manifest.yaml" | tr -d '"')"
if [[ ! "$manifest_version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  fail "manifest.yaml version must use semantic versioning, got: ${manifest_version:-missing}"
fi

if ! grep -q "^## $manifest_version " "$ROOT_DIR/CHANGELOG.md"; then
  fail "CHANGELOG.md is missing an entry for manifest version $manifest_version"
fi

root_skill_dirs=()
for dir in "$ROOT_DIR"/sci-*; do
  [[ -e "$dir" ]] || continue
  [[ -d "$dir" ]] && root_skill_dirs+=("$(basename "$dir")")
done

if (( ${#root_skill_dirs[@]} > 0 )); then
  fail "Unexpected root-level skill folder(s): ${root_skill_dirs[*]}. Installable skills must live under skills/."
fi

manifest_skill_names="$(awk '/^  - name: / {print $3}' "$ROOT_DIR/manifest.yaml")"
expected_skill_names="$(printf '%s\n' "${SKILLS[@]}")"

if [[ "$manifest_skill_names" != "$expected_skill_names" ]]; then
  echo "Expected skills from validation script:" >&2
  echo "$expected_skill_names" >&2
  echo "Skills listed in manifest.yaml:" >&2
  echo "$manifest_skill_names" >&2
  fail "manifest.yaml skill list does not match packaged skills"
fi

for skill in "${SKILLS[@]}"; do
  skill_dir="$ROOT_DIR/skills/$skill"
  manifest_path="$(awk -v skill="$skill" '
    /^  - name: / {in_block = ($3 == skill)}
    in_block && /^    path: / {print $2; exit}
  ' "$ROOT_DIR/manifest.yaml")"

  if [[ "$manifest_path" != "skills/$skill" ]]; then
    fail "manifest.yaml path for $skill must be skills/$skill, got: ${manifest_path:-missing}"
  fi

  [[ -d "$skill_dir" ]] || fail "Missing skill directory: skills/$skill"
  [[ -f "$skill_dir/SKILL.md" ]] || fail "Missing $skill/SKILL.md"
  [[ -f "$skill_dir/agents/openai.yaml" ]] || fail "Missing $skill/agents/openai.yaml"
  [[ -d "$skill_dir/references" ]] || fail "Missing $skill/references/"

  reference_file_count="$(find "$skill_dir/references" -maxdepth 1 -type f | wc -l | tr -d ' ')"
  if [[ "$reference_file_count" == "0" ]]; then
    fail "Missing reference file under $skill/references/"
  fi

  if [[ "$(sed -n '1p' "$skill_dir/SKILL.md")" != "---" ]]; then
    fail "$skill/SKILL.md must start with YAML frontmatter"
  fi

  declared_name="$(awk -F': *' '$1 == "name" {print $2; exit}' "$skill_dir/SKILL.md" | tr -d '"')"
  if [[ "$declared_name" != "$skill" ]]; then
    fail "$skill/SKILL.md frontmatter name must be $skill, got: ${declared_name:-missing}"
  fi

  if ! grep -q '^description: ' "$skill_dir/SKILL.md"; then
    fail "Missing frontmatter description in $skill/SKILL.md"
  fi

  if ! grep -q '^## State Coupling' "$skill_dir/SKILL.md"; then
    fail "Missing State Coupling section in $skill/SKILL.md"
  fi

  if ! grep -q '^interface:' "$skill_dir/agents/openai.yaml"; then
    fail "Missing interface block in $skill/agents/openai.yaml"
  fi

  if ! grep -q '^  display_name:' "$skill_dir/agents/openai.yaml"; then
    fail "Missing display_name in $skill/agents/openai.yaml"
  fi

  if ! grep -q '^  short_description:' "$skill_dir/agents/openai.yaml"; then
    fail "Missing short_description in $skill/agents/openai.yaml"
  fi

  if ! grep -q '^  default_prompt:' "$skill_dir/agents/openai.yaml"; then
    fail "Missing default_prompt in $skill/agents/openai.yaml"
  fi
done

echo "Validated SCI-paper-skills $manifest_version with ${#SKILLS[@]} modules."
