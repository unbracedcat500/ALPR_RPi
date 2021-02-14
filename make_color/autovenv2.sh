#!/bin/bash
source "/home/pi/venv/bin/activate"
export LC_ALL=C
export PYTHONPATH=/home/pi/openalpr/src/bindings/python/openalpr
python --version
python /home/pi/Github/ALPR_RPi/make_color/main2.py
