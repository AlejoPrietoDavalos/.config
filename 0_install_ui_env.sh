#!/bin/bash

rm -rf env/
python3 -m venv env
source env/bin/activate
pip install -r requirements_wm.txt
