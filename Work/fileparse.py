import sys
import csv


def parse_csv(filename:str,
              select:list=None,
              types:list=None,
              ) -> list:
    ''' Parse a csv file into a list of records'''
    with open(filename) as FH:
        rows = csv.reader(FH)

        #Read the file headers
        headers = next(rows)
        if select:
            indices = [headers.index(col) for col in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:
                continue

            if indices:
                row = [row[idx] for idx in indices]

            if types:
                row = [ func(val) for func, val in zip(types, row)]

            record = dict(zip(headers, row))
            records.append(record)

    return records









