from messages.alert import AlertMessage

class AlertMessageBuilder:
    def __init__(self):
        self.message = ""

    def with_message(self, message):
        self.message = message
        return self

    def build(self):
        if not self.message:
            raise ValueError("Message is required for AlertMessage")
        return AlertMessage(self.message)