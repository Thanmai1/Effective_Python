import sys
import csv
from fileparse import parse_csv

#this function is used to read a csv file with headers
def read_inventory(filename:str)-> list[dict]:
    with open(filename) as FH:
        inv = parse_csv(FH,
                        select = ["name", "quant", "price"],
                        types = [str, int, float])

    return inv

#this function is used to read a csv file WITHOUT headers
def read_prices(filename):
    with open(filename) as FH:
        prices_list = parse_csv(FH,
                                types = [str, float],
                                has_headers= False)
        prices = dict(prices_list)

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

def print_report(report):
    headers = ("Name", "Quantity", "Price", "Change")
    dash = ("-"*10,)*4

    print("%10s %10s %10s %10s" % headers)
    print("%10s %10s %10s %10s" % dash)
    for r in report:
        print("%10s %10d %10.2f %10.2f" % r)

def inventory_report(inv_filename, prices_filename):
    inv = read_inventory(inv_filename)
    prices = read_prices(prices_filename)
    report = make_report(inv, prices)
    print_report(report)


def main(argv):
    print(f"{argv= }")
    if len(argv)!=3:
        raise SystemExit(f"Usage: {argv[0]} invfile pricefile")

    invfile = argv[1]
    pricefile = argv[2]
    inventory_report(invfile, pricefile)

if __name__ == "__main__":
    import sys
    main(sys.argv)




