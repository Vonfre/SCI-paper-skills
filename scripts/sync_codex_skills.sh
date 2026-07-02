#!/usr/bin/env bash
#
# sync_codex_skills.sh - install/update SCI-paper-skills for Codex or cc-switch.
#
# Codex commonly reads skills from ~/.codex/skills. cc-switch can store and
# expose skills from ~/.cc-switch/skills when skillStorageLocation=cc_switch.
# This script syncs every top-level directory under skills/ that contains a
# SKILL.md into the selected destination and verifies the copied files.
#
# Usage:
#   scripts/sync_codex_skills.sh                         # install to Codex
#   scripts/sync_codex_skills.sh --target ccswitch       # install to cc-switch
#   scripts/sync_codex_skills.sh --target both           # install to both
#   scripts/sync_codex_skills.sh --check --target both   # verify only
#   scripts/sync_codex_skills.sh --pull --target ccswitch
#   scripts/sync_codex_skills.sh --dest /path/to/skills  # custom destination
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/skills"
TARGET="${SCI_PAPER_SKILLS_TARGET:-codex}"
DEST_OVERRIDE=""
PULL="${PULL:-0}"
PRUNE="${PRUNE:-0}"
CHECK_ONLY="${CHECK_ONLY:-0}"
MANIFEST_NAME=".sci-paper-skills-install.txt"

usage() {
  cat <<'USAGE'
sync_codex_skills.sh - install/update SCI-paper-skills.

Usage:
  scripts/sync_codex_skills.sh
  scripts/sync_codex_skills.sh --target codex|ccswitch|both
  scripts/sync_codex_skills.sh --dest /path/to/skills
  scripts/sync_codex_skills.sh --pull
  scripts/sync_codex_skills.sh --check
  scripts/sync_codex_skills.sh --prune

Environment:
  SCI_PAPER_SKILLS_TARGET=codex|ccswitch|both
  CODEX_SKILLS_DIR=/path/to/codex/skills
  CCSWITCH_SKILLS_DIR=/path/to/cc-switch/skills
  PULL=1
  CHECK_ONLY=1
  PRUNE=1
USAGE
}

die() {
  echo "error: $*" >&2
  exit 1
}

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "$1 is required but not installed"
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      shift
      [ "$#" -gt 0 ] || die "--target requires codex, ccswitch, or both"
      TARGET="$1"
      ;;
    --dest)
      shift
      [ "$#" -gt 0 ] || die "--dest requires a directory"
      DEST_OVERRIDE="$1"
      ;;
    --pull)
      PULL=1
      ;;
    --check|--verify-only)
      CHECK_ONLY=1
      ;;
    --prune)
      PRUNE=1
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
  shift
done

[ -d "$SOURCE_DIR" ] || die "skills directory not found: $SOURCE_DIR"

case "$TARGET" in
  codex|ccswitch|both) ;;
  *) die "--target must be codex, ccswitch, or both" ;;
esac

if [ -n "$DEST_OVERRIDE" ] && [ "$TARGET" = "both" ]; then
  die "--dest can only be used with a single target"
fi

if [ "$PULL" = "1" ]; then
  if git -C "$ROOT_DIR" rev-parse --git-dir >/dev/null 2>&1; then
    echo "==> Pulling latest changes"
    git -C "$ROOT_DIR" pull --ff-only
  else
    echo "==> Skipping pull: $ROOT_DIR is not a git checkout"
  fi
fi

need_cmd diff
[ "$CHECK_ONLY" = "1" ] || need_cmd rsync

SKILL_LIST="$(mktemp "${TMPDIR:-/tmp}/sci-paper-skills-list.XXXXXX")"
DIFF_OUT="$(mktemp "${TMPDIR:-/tmp}/sci-paper-skills-diff.XXXXXX")"
trap 'rm -f "$SKILL_LIST" "$DIFF_OUT"' EXIT

for path in "$SOURCE_DIR"/*/; do
  [ -d "$path" ] || continue
  name="$(basename "$path")"
  if [ ! -f "$path/SKILL.md" ]; then
    die "unexpected skills/$name directory without SKILL.md"
  fi
  printf '%s\n' "$name" >> "$SKILL_LIST"
done

[ -s "$SKILL_LIST" ] || die "no skill directories found under $SOURCE_DIR"
sort -o "$SKILL_LIST" "$SKILL_LIST"

repo_commit="unknown"
if git -C "$ROOT_DIR" rev-parse --git-dir >/dev/null 2>&1; then
  repo_commit="$(git -C "$ROOT_DIR" rev-parse HEAD)"
fi

verify_target() {
  dest="$1"
  status=0
  while IFS= read -r name; do
    src_path="$SOURCE_DIR/$name"
    dst_path="$dest/$name"
    if [ ! -d "$dst_path" ]; then
      echo "MISSING  $name"
      status=1
    elif diff -qr "$src_path" "$dst_path" >"$DIFF_OUT"; then
      echo "MATCH    $name"
    else
      echo "DIFF     $name"
      sed 's/^/         /' "$DIFF_OUT"
      status=1
    fi
  done < "$SKILL_LIST"
  return "$status"
}

sync_target() {
  label="$1"
  dest="$2"

  if [ "$CHECK_ONLY" = "1" ]; then
    echo "==> Verifying $label skills in $dest"
    verify_target "$dest"
    echo "==> Verified against $repo_commit"
    return
  fi

  mkdir -p "$dest"
  echo "==> Syncing SCI-paper-skills into $label: $dest"
  while IFS= read -r name; do
    mkdir -p "$dest/$name"
    rsync -a --delete "$SOURCE_DIR/$name/" "$dest/$name/"
    echo "    synced $name"
  done < "$SKILL_LIST"

  manifest="$dest/$MANIFEST_NAME"
  if [ "$PRUNE" = "1" ]; then
    if [ -f "$manifest" ]; then
      echo "==> Pruning stale SCI-paper-skills entries in $dest"
      while IFS= read -r old_name; do
        case "$old_name" in
          ""|\#*) continue ;;
        esac
        if ! grep -Fxq "$old_name" "$SKILL_LIST" && [ -d "$dest/$old_name" ]; then
          rm -rf "$dest/$old_name"
          echo "    pruned $old_name"
        fi
      done < "$manifest"
    else
      echo "==> No previous $MANIFEST_NAME manifest; skipping prune"
    fi
  fi

  {
    echo "# Managed by SCI-paper-skills scripts/sync_codex_skills.sh"
    echo "# source=$ROOT_DIR"
    echo "# commit=$repo_commit"
    date '+# updated_at=%Y-%m-%dT%H:%M:%S%z'
    cat "$SKILL_LIST"
  } > "$manifest"

  echo "==> Verifying copied skills in $dest"
  verify_target "$dest"
  echo "==> Installed from $repo_commit"
}

if [ -n "$DEST_OVERRIDE" ]; then
  sync_target "custom" "$DEST_OVERRIDE"
else
  case "$TARGET" in
    codex)
      sync_target "Codex" "${CODEX_SKILLS_DIR:-$HOME/.codex/skills}"
      ;;
    ccswitch)
      sync_target "cc-switch" "${CCSWITCH_SKILLS_DIR:-$HOME/.cc-switch/skills}"
      ;;
    both)
      sync_target "Codex" "${CODEX_SKILLS_DIR:-$HOME/.codex/skills}"
      sync_target "cc-switch" "${CCSWITCH_SKILLS_DIR:-$HOME/.cc-switch/skills}"
      ;;
  esac
fi

echo "==> Done. Restart Codex or cc-switch if newly installed skills do not appear immediately."
