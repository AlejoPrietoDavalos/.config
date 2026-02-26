#!/bin/bash

set -euo pipefail

print_util() {
  local value="$1"
  if [[ "$value" =~ ^[0-9]+$ ]]; then
    printf 'GPU %3s%%\n' "$value"
    exit 0
  fi
}

if command -v nvidia-smi >/dev/null 2>&1; then
  nvidia_util="$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits 2>/dev/null | head -n1 | tr -d '[:space:]' || true)"
  print_util "$nvidia_util"
fi

for path in /sys/class/drm/card*/device/gpu_busy_percent /sys/class/drm/card*/gt_busy_percent; do
  [ -r "$path" ] || continue
  util="$(tr -d '[:space:]' < "$path" 2>/dev/null || true)"
  print_util "$util"
done

printf 'GPU N/A\n'
