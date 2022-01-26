#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Small script to mass rename files that
# begin with the same string(s).
# Perfect for track stems that have something
# dumb before the name of the instrument.
#
# Author: Luke Simone

import sys

if sys.version_info < (3, 6):
    sys.stdout.write("Requires Python 3.6 or newer\n")
    sys.exit(1)

import os
from pathlib import Path
from argparse import ArgumentParser


def main(args):
    dir_path = Path(args.dir).resolve()
    try:
        dir_ls = os.listdir(dir_path)
    except NotADirectoryError:
        sys.stderr.write("error - Provided path is not a directory\n")
        sys.exit(1)
    except FileNotFoundError:
        sys.stderr.write("error - Couldn't find that folder\n")
        sys.exit(1)

    file_parts = dir_ls[0].split(args.separator)

    # Display split file name and options
    print(dir_ls[0] + "\n\nParts:")
    print("  ", " | ".join(file_parts))

    print("   ", end='')
    for i in range(0, len(file_parts)):
        print(f"[{i+1}]" + ' ' * len(file_parts[i]), end='')
    print()

    try:
        choice = int(input("Keep file names starting at position: "))
        assert choice in range(1, len(file_parts)+1)
    except (ValueError, AssertionError):
        sys.stderr.write("error - Invalid choice, exiting\n")
        sys.exit(1)

    # Move files based on selection
    print("Renaming files...")
    for file in dir_ls:
        file_parts = [p.strip() for p in file.split(args.separator)]
        new_file_name = ''.join(file_parts[(choice-1):]).strip()

        old_path = Path(dir_path, file)
        new_path = Path(dir_path, new_file_name)
        old_path.rename(new_path)
        print(file, "-->", new_file_name)

    print("Done")


if __name__ == '__main__':
    try:
        parser = ArgumentParser(description="Rename track stems")
        parser.add_argument('dir', type=str,
                            help="Folder containing the track stems")
        parser.add_argument('-s', '--separator', type=str, default=' ',
                            help="Specify a different file name separator character, default is SPACE (Example: _)")
        args = parser.parse_args()
        main(args)
    except KeyboardInterrupt:
        sys.stdout.write("\nCancelled by user\n")
    sys.exit()
