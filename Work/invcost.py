
import csv
with open("Data/inventory.csv") as FH:
    data = csv.reader(FH) # data is a generator object
    headers = next(data) # store the first line as headers

    total = 0
    for row in data: # iterating from the second line
        quant = int(row[1])
        price = float(row[2])
        costfor1item = quant*price
        # print(costfor1item)
        total = total + costfor1item

    print(total)

