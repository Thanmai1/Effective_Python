import sys
import csv

def read_inventory(filename:str)-> list[dict]:
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



def make_report(inventory, prices):
    ''' This function takes inv list and prices dict as inputs and returns list fo tuples'''
    report = []
    for prod in inventory:
        name = prod["name"]
        quant = prod["quant"]
        old_price = prod["price"]
        new_price = prices[name]
        change = new_price - old_price
        info = (name, quant, new_price, change)
        report.append(info)

    return report  # report is a list

inv = read_inventory("Data/inventory.csv")
prices = read_prices("Data/prices.csv")
report = make_report(inv, prices)
headers = ("Name", "Quantity", "Price", "Change")
dash = ("-"*10,)*4

print("%10s %10s %10s %10s" % headers)
print("%10s %10s %10s %10s" % dash)
for r in report:
    print("%10s %10d %10.2f %10.2f" % r)


