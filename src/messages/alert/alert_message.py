from message import Message

class AlertMessage(Message):
    def __init__(self, message):
        self.message = message

    def get_formatted_message(self, strategy):
        return strategy.format({'message': self.message})