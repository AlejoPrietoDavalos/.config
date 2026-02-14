#!/bin/bash

# Estado actual de la ventana. (tiled, fullscreen, floating)
function get_current_state {
    echo $(bspc query -T -n | jq -r '.client.state')
}


function toggle {
    state=$1
    bspc node -t $state
}

function toggle_tiled {
    toggle tiled
}

function toggle_fullscreen {
    toggle fullscreen
}

function toggle_floating {
    toggle floating
}


function toggle_fullscreen_tiled {
    current_state=$(get_current_state)

    if [[ "$current_state" == "fullscreen" ]]; then
        $(toggle_tiled)
    else
        $(toggle_fullscreen)
    fi
}

function toggle_floating_tiled {
    current_state=$(get_current_state)

    if [[ "$current_state" == "floating" ]]; then
        $(toggle_tiled)
    else
        $(toggle_floating)
    fi
}


case "$1" in
    fullscreen_tiled) $(toggle_fullscreen_tiled);;
    floating_tiled) $(toggle_floating_tiled);;
    *) echo "Comando no reconocido: $1";;
esac
