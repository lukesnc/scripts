#!/usr/bin/env python3
# Author: lukesnc

from argparse import ArgumentParser
from fractions import Fraction


def main(args):
    bpm = args.bpm
    qtr_note_hz = bpm / 60
    print("BPM is", bpm)
    print("=" * 32)

    note = 4
    while note >= 1 / 32:
        hz = qtr_note_hz / (4 * note)
        ms = (60000 / bpm) * (note * 4)
        print(f"| {str(Fraction(note)):>4} | {hz:>6.3f} Hz | {ms:>6.0f} ms |")
        note /= 2


if __name__ == "__main__":
    parser = ArgumentParser(description="Convert BPM to Hz and ms")
    parser.add_argument("bpm", type=int, help="Beats per minute")
    args = parser.parse_args()
    main(args)
