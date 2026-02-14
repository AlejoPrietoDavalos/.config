#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$SCRIPT_DIR/common.sh"

program="${1:-}"
if [ -z "$program" ]; then
    echo "Usage: $0 <program>" >&2
    exit 1
fi

ensure_program "$program"
ensure_program_packages "$program"

files_dir="$PROGRAMS_DIR/$program/files"
case "$program" in
    thunar) target_dir="$HOME/.config/Thunar" ;;
    *) target_dir="$HOME/.config/$program" ;;
esac
mkdir -p "$target_dir"

for src in "$files_dir"/*; do
    [ -e "$src" ] || continue
    name="$(basename "$src")"
    dst="$target_dir/$name"
    safe_link "$src" "$dst"
done
