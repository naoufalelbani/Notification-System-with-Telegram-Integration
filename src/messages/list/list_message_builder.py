from .list_message import ListMessage

class ListMessageBuilder:
    def __init__(self):
        self.items = []

    def with_items(self, items):
        self.items = items
        return self

    def build(self):
        if not self.items:
            raise ValueError("Items are required for ListMessage")
        return ListMessage(self.items)