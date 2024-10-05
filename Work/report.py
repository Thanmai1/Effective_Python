import sys
import csv

def read_inventory(filename):
    inv = []
    with open(filename) as FH:
        data = csv.reader(FH) # data is a generator object
        headers = next(data) # store the first line as headers

        for row in data:
            items_in_row = {"name": str(row[0]),
                            "quant": int(row[1]),
                            "price": float(row[2]),
                            }
            inv.append(items_in_row)

        return inv




