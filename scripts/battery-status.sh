#!/bin/bash

set -euo pipefail

battery_path=""
for candidate in /sys/class/power_supply/BAT*; do
  if [ -e "$candidate" ]; then
    battery_path="$candidate"
    break
  fi
done

[ -z "$battery_path" ] && exit 0

capacity="$(cat "$battery_path/capacity" 2>/dev/null || echo "")"
status="$(cat "$battery_path/status" 2>/dev/null || echo "")"
[ -z "$capacity" ] && exit 0

if [ "$capacity" -ge 90 ]; then
  icon=''
elif [ "$capacity" -ge 65 ]; then
  icon=''
elif [ "$capacity" -ge 40 ]; then
  icon=''
elif [ "$capacity" -ge 20 ]; then
  icon=''
else
  icon=''
fi

case "$status" in
  Charging) prefix=' ' ;;
  *) prefix='' ;;
esac

printf '%s%s %s%%\n' "$prefix" "$icon" "$capacity"
