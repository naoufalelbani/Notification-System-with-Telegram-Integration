from typing import List
from messages.message import Message
from strategies import MarkdownStrategy, MarkdownV2Strategy

class CompositeMessage(Message):
    def __init__(self, components: List[Message], separator="\n"):
        self.components = components
        self.separator = separator

    def get_formatted_message(self, strategy):
        formatted_components = []
        for comp in self.components:
            formatted_message = comp.get_formatted_message(strategy)
            # Wrap only table messages in triple backticks for Markdown/MarkdownV2
            if hasattr(comp, 'rows') and isinstance(strategy, (MarkdownStrategy, MarkdownV2Strategy)):
                formatted_message = f"```\n{formatted_message}\n```"
            formatted_components.append(formatted_message)
        return self.separator.join(formatted_components)

    def __str__(self):
        # Default to MarkdownV2 formatting when converting to string
        return self.get_formatted_message(MarkdownV2Strategy())