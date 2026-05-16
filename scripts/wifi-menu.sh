#!/bin/bash

set -euo pipefail

if ! command -v nmcli >/dev/null 2>&1; then
  rofi -e "nmcli no esta instalado"
  exit 1
fi

if ! command -v rofi >/dev/null 2>&1; then
  notify-send "WiFi" "Instala rofi para abrir el menu"
  exit 1
fi

list="$(nmcli -t -f IN-USE,SSID,SECURITY,SIGNAL dev wifi list | sed '/^$/d')"
[ -z "$list" ] && { rofi -e "No se encontraron redes"; exit 0; }

menu="$(printf '%s\n' "$list" | awk -F: '
{
  mark=$1; ssid=$2; sec=$3; signal=$4;
  if (ssid == "") next;
  lock=(sec == "--" ? "" : " [lock]");
  active=(mark == "*" ? "* " : "  ");
  printf "%s%s%s (%s%%)\n", active, ssid, lock, signal;
}')"

choice="$(printf '%s\n' "$menu" | rofi -dmenu -i -p "WiFi")"
[ -z "$choice" ] && exit 0

ssid="$(printf '%s\n' "$choice" | sed -E 's/^[* ]+//; s/ \[lock\] \([0-9]+%\)$//; s/ \([0-9]+%\)$//')"
security="$(printf '%s\n' "$list" | awk -F: -v s="$ssid" '$2==s{print $3; exit}')"

if [ "${security:-}" = "--" ] || [ -z "${security:-}" ]; then
  nmcli dev wifi connect "$ssid" >/dev/null 2>&1 && notify-send "WiFi" "Conectado a $ssid"
  exit 0
fi

pass="$(rofi -dmenu -password -p "Clave de $ssid")"
[ -z "$pass" ] && exit 0

if nmcli dev wifi connect "$ssid" password "$pass" >/dev/null 2>&1; then
  notify-send "WiFi" "Conectado a $ssid"
else
  rofi -e "No se pudo conectar a $ssid"
  exit 1
fi
