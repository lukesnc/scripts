#!/bin/bash

python3 -m pip list | awk '{print $1}' | tail -n +3 > temp.lst
python3 -m pip install --upgrade -r temp.lst
rm temp.lst
echo "Done."
