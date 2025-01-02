from messages.table import TableMessage

class TableMessageBuilder:
    def __init__(self):
        self.title = ""
        self.headers = []
        self.rows = []

    def with_title(self, title):
        self.title = title
        return self

    def with_headers(self, headers):
        self.headers = headers
        return self

    def with_rows(self, rows):
        self.rows = rows
        return self

    def build(self):
        if not self.title or not self.headers or not self.rows:
            raise ValueError("Title, headers, and rows are required for TableMessage")
        return TableMessage(self.title, self.headers, self.rows)