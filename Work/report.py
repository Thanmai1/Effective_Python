import sys
import csv
from fileparse import parse_csv

def read_inventory(filename:str)-> list[dict]:
    inv = parse_csv(filename,
                    select = ["name", "quant", "price"],
                    types = [str, int, float])

    return inv

def read_prices(filename):
    prices_list = parse_csv(filename,
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

inventory_report("Data/inventory.csv", "Data/prices.csv")


