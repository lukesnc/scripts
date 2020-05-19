# Filters through a large list of links and strips out the ones that 404

import requests  # pip3 install requests
from progress.bar import Bar  # pip3 install progress

IN_FILE = "A_Long_List.txt"
OUT_FILE = "out.txt"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36'}

bar = Bar("Checking links...", max=20000)
broken_links_found = 0
with open(IN_FILE, 'r') as in_f, open(OUT_FILE, 'w') as out_f:
    for line in in_f: # each line has a url
        status_code = requests.get(line, headers=headers).status_code
        if status_code != 404:
            out_f.writelines(line)
        else:
            broken_links_found += 1
        bar.next()

bar.finish()
print("\nDone! Broken links found:", broken_links_found)
