from .composite_message import CompositeMessage

class CompositeMessageBuilder:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        if not isinstance(component, Message):
            raise TypeError("Component must be an instance of Message")
        self.components.append(component)
        return self

    def build(self):
        return CompositeMessage(self.components)