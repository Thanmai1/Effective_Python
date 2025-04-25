def filematch(lines, substr):
    # with open(filename) as f:
    for line in lines:
        if substr in line:
            yield line

from follow import follow
import csv

lines = follow("Data/marketlog.csv")
rows = csv.reader(lines)
for row in rows:
    print(row)

# mint = filematch(lines, "MINT")
# for line in mint:
#     print(line)

""">>> for line in filematch("Data/inventory.csv", "MINT"):
...     print(line, end = ' ')
...
"MINT",200,51.23
 "MINT",50,65.10
 >>>
"""