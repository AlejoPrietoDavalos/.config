#!/bin/bash
set -euo pipefail

WM_ROOT="$HOME/.config/_wm"
PROGRAMS_DIR="$WM_ROOT/programs"
BACKUP_ROOT="$WM_ROOT/backups"
PACKAGES_DIR="$WM_ROOT/packages"

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

ensure_cmd_executables() {
    local program="$1"
    local cmd_dir="$PROGRAMS_DIR/$program/files/cmd"
    if [ ! -d "$cmd_dir" ]; then
        return 0
    fi
    find "$cmd_dir" -maxdepth 1 -type f -exec chmod +x {} +
}

packages_file_for_program() {
    local program="$1"
    echo "$PACKAGES_DIR/$program.txt"
}

read_program_packages() {
    local program="$1"
    local packages_file
    packages_file="$(packages_file_for_program "$program")"

    if [ ! -f "$packages_file" ]; then
        return 0
    fi

    # shellcheck disable=SC2016
    awk '!/^[[:space:]]*#/ && NF {print $1}' "$packages_file"
}

ensure_program_packages() {
    local program="$1"

    if ! command -v pacman >/dev/null 2>&1; then
        echo "Skip deps for '$program': pacman not found."
        return 0
    fi

    mapfile -t packages < <(read_program_packages "$program")
    if [ "${#packages[@]}" -eq 0 ]; then
        return 0
    fi

    local missing=()
    local pkg
    for pkg in "${packages[@]}"; do
        if ! pacman -Q "$pkg" >/dev/null 2>&1; then
            missing+=("$pkg")
        fi
    done

    if [ "${#missing[@]}" -eq 0 ]; then
        return 0
    fi

    echo "Installing deps for '$program': ${missing[*]}"
    sudo pacman -S --needed --noconfirm "${missing[@]}"
}

remove_program_packages() {
    local program="$1"

    if [ "${WM_REMOVE_PACKAGES:-0}" != "1" ]; then
        return 0
    fi

    if ! command -v pacman >/dev/null 2>&1; then
        return 0
    fi

    mapfile -t packages < <(read_program_packages "$program")
    if [ "${#packages[@]}" -eq 0 ]; then
        return 0
    fi

    local installed=()
    local pkg
    for pkg in "${packages[@]}"; do
        if pacman -Q "$pkg" >/dev/null 2>&1; then
            installed+=("$pkg")
        fi
    done

    if [ "${#installed[@]}" -eq 0 ]; then
        return 0
    fi

    echo "Removing deps for '$program': ${installed[*]}"
    sudo pacman -Rns --noconfirm "${installed[@]}"
}
