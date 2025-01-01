from .composite_message import CompositeMessage
from message import Message

class CompositeMessage(Message):
    def __init__(self, components, separator="\n"):
        self.components = components
        self.separator = separator

    def get_formatted_message(self, strategy):
        formatted_components = [comp.get_formatted_message(strategy) for comp in self.components]
        return self.separator.join(formatted_components)