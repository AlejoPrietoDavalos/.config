#!/bin/bash

DELTA_VOLUME=5

case "$1" in
    mute) pamixer --toggle-mute;;
    decrease) pamixer --decrease "$DELTA_VOLUME";;
    increase) pamixer --increase "$DELTA_VOLUME";;
    *) echo "Comando no reconocido: $1";;
esac