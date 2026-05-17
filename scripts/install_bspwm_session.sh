#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
src="$REPO_DIR/resources/config_files/bspwm/bspwm.desktop"
dst="/usr/share/xsessions/bspwm.desktop"

sudo install -Dm644 "$src" "$dst"
echo "Installed session file: $dst"
