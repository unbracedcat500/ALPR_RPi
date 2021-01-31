#!/bin/bash
source "/home/pi/venv/bin/activate"
export PYTHONPATH=/home/pi/openalpr/src/bindings/python/openalpr
python --version
python /home/pi/Github/ALPR_RPi/make_color/main.py
