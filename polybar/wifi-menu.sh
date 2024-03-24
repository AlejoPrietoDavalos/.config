#!/bin/bash

# Lista las redes WiFi disponibles
networks=$(nmcli --fields IN-USE,SSID,BARS dev wifi | awk 'NR>1 {print $2}')

# Usa rofi para seleccionar una red
selected=$(echo "$networks" | rofi -dmenu -p "Select a network: ")

# Si se seleccionó una red, pide la contraseña y conéctate
if [ -n "$selected" ]; then
    pass=$(rofi -dmenu -p "Password for $selected: " -lines 0)
    nmcli dev wifi connect "$selected" password "$pass"
fi
