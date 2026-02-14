#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

rm -rf "$SCRIPT_DIR/env/"
python3 -m venv "$SCRIPT_DIR/env"
source "$SCRIPT_DIR/env/bin/activate"
pip install -r "$SCRIPT_DIR/requirements_wm.txt"
