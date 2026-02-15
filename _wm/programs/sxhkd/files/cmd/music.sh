#!/bin/bash

case "$1" in
    previous) playerctl previous ;;
    next) playerctl next ;;
    play_pause) playerctl play-pause ;;
    stop) ;;
    *) echo "Comando no reconocido: $1";;
esac