#!/bin/bash
set -euo pipefail

src="$HOME/.config/resources/config_files/bspwm/bspwm.desktop"
dst="/usr/share/xsessions/bspwm.desktop"

sudo install -Dm644 "$src" "$dst"
echo "Installed session file: $dst"
