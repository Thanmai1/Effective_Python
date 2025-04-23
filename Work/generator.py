def filematch(filename, substr):
    with open(filename) as f:
        for line in f:
            if substr in line:
                yield line


""">>> for line in filematch("Data/inventory.csv", "MINT"):
...     print(line, end = ' ')
...
"MINT",200,51.23
 "MINT",50,65.10
 >>>
"""