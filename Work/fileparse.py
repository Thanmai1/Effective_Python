import sys
import csv


def parse_csv(filename:str,
              select:list=None,
              types:list=None,
              has_headers:bool=True,
              delimiter:str=",",
              ) -> list:

    ''' Parse a csv file into a list of records'''
    if select and not has_headers:
        raise RuntimeError("Select argument requires col headers")

    with open(filename) as FH:
        rows = csv.reader(FH, delimiter = delimiter)

        if has_headers:
            #Read the file headers
            headers = next(rows)

        if select:
            indices = [headers.index(col) for col in select]
            headers = select
        else:
            indices = []

        records = []
        for rno, row in enumerate(rows, start=1):
            if not row:
                continue

            if indices:
                row = [row[idx] for idx in indices]

            if types:
                try:
                    row = [ func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    print(f"Row {rno}: Couldn't convert: {row}")
                    print(f"Row {rno}: Reason {e}")
                    continue

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)


    return records









