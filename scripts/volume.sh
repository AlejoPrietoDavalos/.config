#!/bin/bash

DELTA_VOLUME=5

run_with_pamixer() {
    case "$1" in
        mute) pamixer --toggle-mute ;;
        decrease) pamixer --decrease "$DELTA_VOLUME" ;;
        increase) pamixer --increase "$DELTA_VOLUME" ;;
        *) echo "Comando no reconocido: $1"; return 1 ;;
    esac
}

run_with_wpctl() {
    case "$1" in
        mute) wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle ;;
        decrease) wpctl set-volume @DEFAULT_AUDIO_SINK@ "${DELTA_VOLUME}%-" ;;
        increase) wpctl set-volume @DEFAULT_AUDIO_SINK@ "${DELTA_VOLUME}%+" ;;
        *) echo "Comando no reconocido: $1"; return 1 ;;
    esac
}

if command -v pamixer >/dev/null 2>&1; then
    run_with_pamixer "$1"
elif command -v wpctl >/dev/null 2>&1; then
    run_with_wpctl "$1"
else
    echo "No se encontro ni 'pamixer' ni 'wpctl' para controlar volumen."
    exit 1
fi
