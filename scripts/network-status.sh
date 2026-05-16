#!/bin/bash

set -euo pipefail

if ! command -v nmcli >/dev/null 2>&1; then
  printf 'ERR\n'
  exit 0
fi

if nmcli -t -f TYPE,STATE dev status | grep -q '^ethernet:connected$'; then
  printf 'LAN\n'
  exit 0
fi

if nmcli -t -f TYPE,STATE dev status | grep -q '^wifi:connected$'; then
  signal="$(nmcli -t -f IN-USE,SIGNAL dev wifi list | awk -F: '$1=="*"{print $2; exit}')"
  signal="${signal:-0}"

  if [ "$signal" -ge 75 ]; then
    bars='▂▄▆█'
  elif [ "$signal" -ge 50 ]; then
    bars='▂▄▆_'
  elif [ "$signal" -ge 25 ]; then
    bars='▂▄__'
  else
    bars='▂___'
  fi

  printf '%s\n' "$bars"
  exit 0
fi

printf 'OFF\n'
