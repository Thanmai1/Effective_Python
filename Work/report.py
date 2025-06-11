import sys
import csv
from fileparse import parse_csv
from tableformat import create_formatter
from inventory import Inventory


#this function is used to read a csv file with headers
def read_inventory(filename:str, **opts)-> list[dict]:
    print(opts)
    with open(filename) as FH:
        inv = Inventory.from_csv(FH)

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
        name = prod.name
        quant = prod.quant
        old_price = prod.price
        new_price = prices[name]
        change = new_price - old_price
        info = (name, quant, new_price, change)
        report.append(info)

    return report  # report is a list

def print_report(reportdata, formatter):
    headers = ("Name", "Quantity", "Price", "Change")
    #dash = ("-"*10,)*4
    formatter.headings(headers)

    # print("%10s %10s %10s %10s" % headers)
    # print("%10s %10s %10s %10s" % dash)
    for name,quant,price,change in reportdata:
        # print("%10s %10d %10.2f %10.2f" % r)
        rowdata = [name, str(quant), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

def inventory_report(inv_filename, prices_filename, fmt = "txt"):
    inv = read_inventory(inv_filename)
    prices = read_prices(prices_filename)
    report = make_report(inv, prices)
    formatter = create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    print(f"{argv= }")
    if len(argv)!=4:
        raise SystemExit(f"Usage: {argv[0]} invfile pricefile fmt")

    invfile = argv[1]
    pricefile = argv[2]
    fmt = argv[3]
    inventory_report(invfile, pricefile, fmt)

if __name__ == "__main__":
    import sys
    main(sys.argv)




