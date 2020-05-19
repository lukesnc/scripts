#!/usr/bin/python3.8

# Author: Luke Simone

import random
import sys
import time
import string
import os
from pathlib import Path
from progress.bar import Bar

max_files = 20
max_file_size = 200.0 # in mb
files_dir = Path('./files/')
write_speed = 5 # creates data faster ( EXPONENTIAL )

# Gets size of files/
def get_dir_size():
    return sum(f.stat().st_size for f in files_dir.glob('**/*') if f.is_file())

def make_files(num_of_files, size_of_file):
    # Clear files dir
    try:
        for f in files_dir.glob('**/*'):
            if f.is_file(): os.remove(f)
        print("Cleared contents of 'files/'")
    except:
        pass

    # Starts timer and creates progress bar
    start_time = time.time()
    print("Making", num_of_files, size_of_file, "MB sized file(s)...")
    progress_bar = Bar('Progress', max=num_of_files)

    # Makes the files
    for i in range(1, num_of_files + 1):
        file_name = 'files/file_' + str(i) + '.txt'
        f = open(file_name, 'w+')
        # create file size specified by user
        while get_dir_size() < (size_of_file * 1024 * 1024 * i):
            f.write(random.choice(string.digits) * pow(10, write_speed))
            f.write(random.choice(string.ascii_lowercase) * pow(10, write_speed))
        f.close()
        progress_bar.next()

    # Finished
    progress_bar.finish()
    print("Done!")
    elapsed_time = round(time.time() - start_time, 2)
    print("Took", elapsed_time, "seconds.")

    bytes = get_dir_size()
    gb = round(bytes / 1024 / 1024 / 1024, 1)
    mb = round(bytes / 1024 / 1024, 1)
    kb = round(bytes / 1024, 1)
    if gb > 0:
        print("Created", gb, "GB of data.")
    elif mb > 0:
        print("Created", mb, "MB of data.")
    elif kb > 0:
        print("Created", kb, "KB of data.")
    else:
        print("Created", bytes, "bytes of data.")


# Get args and run program
try:
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        s = float(sys.argv[2])

        if n > max_files or s > max_file_size:
            if s > max_files and not s > max_file_size:
                make_files(max_files, s)
            elif not s > max_files and s > max_file_size:
                make_files(n, max_file_size)
            else:
                make_files(max_files, max_file_size)
        else:
            make_files(n, s)

    elif len(sys.argv) == 2 and sys.argv[1] == '--help':
        print("Simple file creation script.")
        print("Author: Luke Simone")
        print("Usage: python3.8 make_files.py [NUMBER OF FILES] [SIZE OF EACH FILE IN MB]")
        print("  or:  python3.8 make_files.py --help")
        print("\nFiles are written to 'files/'")
        print("Maximum number of files:", max_files)
        print("Maximum size of each file:", max_file_size, "MB")

    else:
        raise Exception

except:
    print("Something went wrong. See --help for more info.")
    sys.exit(1)
