#!/bin/bash
set -euo pipefail

WM_ROOT="$HOME/.config/_wm"
PROGRAMS_DIR="$WM_ROOT/programs"
BACKUP_ROOT="$WM_ROOT/backups"

ensure_program() {
    local program="$1"
    local files_dir="$PROGRAMS_DIR/$program/files"
    if [ ! -d "$files_dir" ]; then
        echo "Program '$program' not found at $files_dir" >&2
        exit 1
    fi
}

backup_path() {
    date +"$BACKUP_ROOT/%Y%m%d-%H%M%S"
}

safe_link() {
    local src="$1"
    local dst="$2"
    local src_real
    src_real="$(readlink -f "$src")"

    mkdir -p "$(dirname "$dst")"

    if [ -L "$dst" ]; then
        local current_real
        current_real="$(readlink -f "$dst")"
        if [ "$current_real" = "$src_real" ]; then
            return 0
        fi
    fi

    if [ -e "$dst" ] || [ -L "$dst" ]; then
        local backup
        backup="$(backup_path)"
        mkdir -p "$backup/$(dirname "${dst#$HOME/.config/}")"
        mv "$dst" "$backup/${dst#$HOME/.config/}"
        echo "Backed up: $dst -> $backup/${dst#$HOME/.config/}"
    fi

    ln -s "$src" "$dst"
    echo "Linked: $dst -> $src"
}
