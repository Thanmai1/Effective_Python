
def create_formatter(name):
    if name == "txt":
        formatter = TextTableFormatter()
    elif name == "csv":
        formatter = CSVTableFormatter()
    else:
        raise RuntimeError(f"Unknown Format {name}")

    return formatter


class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    """
    Emit a table in Plain text format
    """
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))
