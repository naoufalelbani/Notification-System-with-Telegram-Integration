from messages.message import Message

class ListMessage(Message):
    def __init__(self, items):
        self.items = items

    def get_formatted_message(self, strategy):
        return strategy.format({'items': self.items})