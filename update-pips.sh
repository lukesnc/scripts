#!/bin/bash

python3 -m pip list | awk '{print $1}' | tail -n +3 > temp.lst
python3 -m pip install -r temp.lst --upgrade
rm temp.lst
echo "Done."
