
import csv
from report import read_inventory

def inventory_cost(filename):
    total = 0
    inv = read_inventory(filename)
    for pr in inv:
        costfor1item = pr.quant * pr.price
        # print(costfor1item)
        total = total + costfor1item

    return total

def main(argv):
    print(f'{argv=}')
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "Data/inventory.csv"

    cost = inventory_cost(filename)
    print("Total Cost:", cost)

if __name__ == "__main__":
    import sys
    main(sys.argv)





