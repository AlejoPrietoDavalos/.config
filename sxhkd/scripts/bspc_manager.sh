#!/bin/bash

function current_state_win {
    echo $(bspc query -T -n | jq -r '.client.state')

}

case "$1" in
    toggle_fullscreen) ;;
    *) echo "Comando no reconocido: $1";;
esac
my_var=$(current_state_win)
echo $my_var