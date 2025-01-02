from messages.message import Message
from strategies import PlainTextStrategy

class CompositeMessage(Message):
    def __init__(self, components, separator="\n"):
        self.components = components
        self.separator = separator

    def get_formatted_message(self, strategy):
        formatted_components = []
        for comp in self.components:
            formatted_message = comp.get_formatted_message(strategy)
            # Wrap only table messages in triple backticks
            if hasattr(comp, 'rows'):  # Check if the component is a table
                formatted_message = f"```\n{formatted_message}\n```"
            formatted_components.append(formatted_message)
        return self.separator.join(formatted_components)

    def __str__(self):
        return self.get_formatted_message(PlainTextStrategy())  # Default to plain text