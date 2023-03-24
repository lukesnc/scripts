#!/usr/bin/env python3
# Author: lukesnc

import sys
from fractions import Fraction


def main() -> int:
    if len(sys.argv) != 2:
        sys.stderr.write("error - please provide a BPM (beats per minute)\n")
        return 1

    try:
        bpm = int(sys.argv[1])
    except ValueError:
        sys.stderr.write("error - that's not a BPM (beats per minute)\n")
        return 1

    qtr_note_hz = bpm / 60
    print("BPM is", bpm)
    print("=" * 15)

    note = 4
    while note >= 1 / 32:
        print(f"{str(Fraction(note)):>4}: {qtr_note_hz / (4 * note):.3f} Hz")
        note /= 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
