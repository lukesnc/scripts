#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Small script to mass rename files that
# begin with the same string(s).
# Perfect for track stems that have something
# dumb before the name of the instrument.
#
# Author: Luke Simone

import os
import sys
from pathlib import Path

if sys.version_info < (3, 6):
    sys.stdout.write("Requires Python 3.6 or newer\n")
    sys.exit(1)

if len(sys.argv) != 2:
    sys.stderr.write("error - Provide a folder path\n")
    sys.exit(1)


def main():
    folder_path = Path(sys.argv[1]).resolve()
    try:
        dir_listing = os.listdir(folder_path)
    except FileNotFoundError:
        print("error - couldn't find that folder, exiting\n")
        sys.exit(1)

    file_parts = dir_listing[0].split(' ')

    # Display first file
    print(dir_listing[0], end='\n\n')
    print("Parts:")

    # Show file name parts
    print("  ", " | ".join(file_parts))

    # Show selector options
    print("   ", end='')
    for i in range(0, len(file_parts)):
        print(f"[{i+1}]" +
              ' ' * len(file_parts[i]),
              end='')
    print()

    # Get selection
    try:
        choice = int(input("Keep file names starting at position: "))
        if choice not in range(1, len(file_parts)+1):
            raise Exception
    except:
        print("error - invalid choice, exiting\n")
        sys.exit(1)

    # Rename files
    print("Renaming files...")
    for file in dir_listing:
        # Build paths
        file_parts = [p.strip() for p in file.split(' ')]
        new_path = ''.join(file_parts[(choice-1):]).strip()

        # Rename files
        old = Path(folder_path, file)
        new = Path(folder_path, new_path)
        old.rename(new)
        print(file, "-->", new_path)

    print("Done")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled by user\n")
    sys.exit()
