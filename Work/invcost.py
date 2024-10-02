
import csv
with open("Data/inventory.csv") as FH:
    data = csv.reader(FH) # data is a generator object
    count = 0
    total = 0
    for row in data:
        count = count+1
        if count == 1: # skip first row(headers)
            continue #skip the calculations and goto the iterator again

        quant = int(row[1])
        price = float(row[2])
        costfor1item = quant*price
        # print(costfor1item)
        total = total + costfor1item

    print(total)

