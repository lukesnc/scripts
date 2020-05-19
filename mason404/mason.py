# mason nigga
import requests
from progress.bar import Bar

FILE_PATH = "A_Long_List.txt"
OUT_FILE = "out.txt"
MAX = 100

in_file = open(FILE_PATH, 'r')
out_file = open(OUT_FILE, 'w')

bar = Bar("Checking links...")
i = 0
for line in in_file:
  try:
    r = requests.get(line, auth=('user', 'pass'))
    if 404 not in r.history:
      out_file.writelines(line)
  except:
    pass
  bar.next()

in_file.close()
out_file.close()
print("\nDone!")