import sys
import csv


def parse_csv(filename:str,
              select:list=None,
              types:list=None,
              has_headers:bool=True,
              ) -> list:
    ''' Parse a csv file into a list of records'''
    with open(filename) as FH:
        rows = csv.reader(FH)

        if has_headers:
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

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)


    return records









