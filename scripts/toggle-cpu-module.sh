#!/bin/bash

set -euo pipefail

polybar-msg action "#cpu.module_toggle" >/dev/null
polybar-msg action "#gpu.module_toggle" >/dev/null
polybar-msg action "#ram.module_toggle" >/dev/null
polybar-msg action "#linux_sep.module_toggle" >/dev/null
