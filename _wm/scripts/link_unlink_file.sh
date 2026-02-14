#!/bin/bash
set -euo pipefail

# Linkea o deslinkea archivos de un programa en ~/.config.
# Uso:
#   ./_wm/scripts/link_unlink_file.sh install bspwm
#   ./_wm/scripts/link_unlink_file.sh install thunar "$HOME/.config/Thunar"
#   WM_REMOVE_PACKAGES=1 ./_wm/scripts/link_unlink_file.sh remove bspwm

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$SCRIPT_DIR/common.sh"

action=""
program=""
target_dir=""
files_dir=""

parse_args() {
    action="${1:-}"
    program="${2:-}"
    target_dir="${3:-$HOME/.config/$program}"
}

validate_args() {
    if [ -z "$action" ] || [ -z "$program" ]; then
        echo "Uso: $0 <install|remove> <program>" >&2
        exit 1
    fi

    if [ "$action" != "install" ] && [ "$action" != "remove" ]; then
        echo "Accion invalida: '$action'. Usar: install | remove" >&2
        exit 1
    fi
}

set_program_context() {
    ensure_program "$program"
    files_dir="$PROGRAMS_DIR/$program/files"
}

install_program() {
    ensure_program_packages "$program"
    ensure_cmd_executables "$program"
    mkdir -p "$target_dir"

    for src in "$files_dir"/*; do
        [ -e "$src" ] || continue
        name="$(basename "$src")"
        dst="$target_dir/$name"
        safe_link "$src" "$dst"
    done
}

remove_program() {
    for src in "$files_dir"/*; do
        [ -e "$src" ] || continue
        name="$(basename "$src")"
        dst="$target_dir/$name"

        if [ -L "$dst" ]; then
            target_real="$(readlink -f "$dst")"
            src_real="$(readlink -f "$src")"
            if [ "$target_real" = "$src_real" ]; then
                rm "$dst"
                echo "Unlinked: $dst"
            fi
        fi
    done

    remove_program_packages "$program"
}

main() {
    parse_args "$@"
    validate_args
    set_program_context

    if [ "$action" = "install" ]; then
        install_program
    else
        remove_program
    fi
}

main "$@"
