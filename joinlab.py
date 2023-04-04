#!/usr/bin/env python3

import subprocess
from time import sleep
from datetime import datetime

url = ""


def main():
    while True:
        rn = datetime.now()
        print(f"Time is {rn.hour}:{rn.minute}")
        if (rn.hour, rn.minute) == (9, 59):
            break
        sleep(60)

    print("Joining Zoom...")
    subprocess.run(["/mnt/c/Program Files/Zoom/bin/Zoom.exe", f'--url="{url}"'])


if __name__ == "__main__":
    main()
