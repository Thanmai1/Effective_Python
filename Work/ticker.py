
from follow import follow
import csv
def filter_names(rows, names):
    for row in rows:
        if row["Name"] in names:
            yield row

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def convert_types(rows, types):
    for row in rows:
        yield [ func(val)  for func, val in zip(types, row)]

def select_cols(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parse_product_data(lines):
    rows = csv.reader(lines)
    # rows = select_cols(rows, [0, 1, 4])
    rows = ( [row[index] for index in [0,1,4]] for row in rows)
    rows = convert_types(rows, [ str, float, float])
    # rows = make_dicts(rows, ["Name", "Price", "Change"])
    headers = ["Name", "Price", "Change"]
    rows = (dict(zip(headers, row)) for row in rows )
    return rows

def make_report(row):
    ''' This function takes inv list and prices dict as inputs and returns list fo tuples'''
    for prod in row:
        info = prod.values()
        yield info

def print_report(reportdata, formatter):
    headers = ("Name", "Price", "Change")
    formatter.headings(headers)

    for name,  price, change in reportdata:
        rowdata = [name,  f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def ticker(inv_file, log_file, fmt):
    from tableformat import create_formatter
    from report import read_inventory
    inv = read_inventory("Data/inventory.csv")
    lines = follow("Data/marketlog.csv")
    rows = parse_product_data(lines)
    # rows = filter_names(rows, inv)
    rows = (row for row in rows if row["Name"] in inv)

    report = make_report(rows)
    formatter = create_formatter(fmt)
    print_report(report, formatter)

if __name__ == "__main__":

    inv = ticker("Data/inventory.csv", "Data/marketlog.csv", "txt")

