import os
import time

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue

        yield line

if __name__ == "__main__":
    import report
    inv = report.read_inventory("Data/inventory.csv")

    for line in follow("Data/marketlog.csv"):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in inv:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
