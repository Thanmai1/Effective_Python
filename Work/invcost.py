import sys
import csv
from report import read_inventory

def inventory_cost(filename):
    total = 0
    inv = read_inventory(filename)
    for pr in inv:
        costfor1item = pr["quant"]*pr["price"]
        # print(costfor1item)
        total = total + costfor1item

    return total

print(f'{sys.argv=}')
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/inventory.csv"

cost = inventory_cost(filename)
print("Total Cost:", cost)





