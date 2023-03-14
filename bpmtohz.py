#!/usr/bin/env python3
# Author: lukesnc

import sys
import json


def main():
    if len(sys.argv) != 2:
        sys.stderr.write("error - please provide a BPM (beats per minute)\n")
        return 1

    try:
        bpm = int(sys.argv[1])
    except ValueError:
        sys.stderr.write("error - that's not a BPM (beats per minute)\n")
        return 1

    qtr_note_hz = bpm / 60
    table = {
        " WHL": qtr_note_hz / 4,
        " 1/2": qtr_note_hz / 2,
        " 1/4": qtr_note_hz,
        " 1/8": qtr_note_hz * 2,
        "1/16": qtr_note_hz * 4,
        "1/32": qtr_note_hz * 8
    }

    print(" BPM:", bpm)
    for key, val in table.items():
        print(f"{key}: {val:.3f} Hz")
    return 0


if __name__ == '__main__':
    sys.exit(main())
