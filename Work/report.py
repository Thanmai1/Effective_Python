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

def read_prices(filename):
    prices = dict()
    with open(filename) as FH:
        data = csv.reader(FH)
        for row in data:
            try:
                prices[row[0]] = float(row[1])
            except IndexError as e:
                continue

    return prices

inventory = read_inventory("Data/inventory.csv")
prices = read_prices("Data/prices.csv")

old_total_cost = 0
for pr in inventory:
    old_total_cost += pr["quant"]* pr["price"]
print("total old cost", old_total_cost)

new_total_cost = 0
for pr in inventory:
    new_total_cost += pr["quant"]* prices[ pr["name"] ]
print("New old cost", new_total_cost)

print("Total gain/loss:", new_total_cost-old_total_cost)







