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

case "$program" in
    thunar) target_dir="$HOME/.config/Thunar" ;;
    *) target_dir="$HOME/.config/$program" ;;
esac
files_dir="$PROGRAMS_DIR/$program/files"

for src in "$files_dir"/*; do
    [ -e "$src" ] || continue
    name="$(basename "$src")"
    dst="$target_dir/$name"

    if [ -L "$dst" ]; then
        target="$(readlink "$dst")"
        if [ "$target" = "$src" ]; then
            rm "$dst"
            echo "Unlinked: $dst"
        fi
    fi
done
