import sys
import csv


def parse_csv(filename:str) -> list:
    ''' Parse a csv file into a list of records'''
    with open(filename) as FH:
        rows = csv.reader(FH)

        #Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue

            record = dict(zip(headers, row))
            records.append(record)

    return records









