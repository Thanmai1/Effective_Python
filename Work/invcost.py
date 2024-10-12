import sys
import csv

def inventory_cost(filename):
    with open(filename) as FH:
        data = csv.reader(FH) # data is a generator object
        headers = next(data) # store the first line as headers

        total = 0
        for rno, row in enumerate(data, start=1): # iterating from the second line
            try:
                quant = int(row[1])
                price = float(row[2])
            except ValueError as e:
                print(f"Row {rno}: Couldn't convert: {row}")
                continue

            costfor1item = quant*price
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



