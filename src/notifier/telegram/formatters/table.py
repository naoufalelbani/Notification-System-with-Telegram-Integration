from tabulate import tabulate
from core.formatter import Formatter

class TableFormatter(Formatter):
    """Formatter for preparing tabular messages."""
    def __init__(self, headers, tablefmt="pretty"):
        self.headers = headers
        self.tablefmt = tablefmt

    def format(self, data):
        return tabulate(data, headers=self.headers, tablefmt=self.tablefmt)
