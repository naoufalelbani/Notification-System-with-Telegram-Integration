from messages.message import Message

class TableMessage(Message):
    def __init__(self, title, headers, rows):
        self.title = title
        self.headers = headers
        self.rows = rows

    def get_formatted_message(self, strategy):
        return strategy.format({
            'title': self.title,
            'headers': self.headers,
            'rows': self.rows
        })