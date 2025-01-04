# src/messages/composite/composite_message.py
from typing import List, Type
from messages.message import Message
from strategies import FormattingStrategy, MarkdownV2Strategy, MarkdownStrategy

class CompositeMessage(Message):
    def __init__(self, components: List[Message], separator="\n", default_strategy: Type[FormattingStrategy] = MarkdownV2Strategy):
        """
        Initialize a CompositeMessage.

        Args:
            components (List[Message]): A list of message components.
            separator (str, optional): The separator to use between components. Defaults to "\n".
            default_strategy (Type[FormattingStrategy], optional): The default strategy to use for formatting.
                                                                 Defaults to MarkdownV2Strategy.
        """
        self.components = components
        self.separator = separator
        self.default_strategy = default_strategy  # Store the default strategy

    def get_formatted_message(self):
        """
        Format the composite message using the default strategy.

        Returns:
            str: The formatted composite message.
        """
        strategy_instance = self.default_strategy()  # Use the default strategy
        formatted_components = []
        for comp in self.components:
            formatted_message = comp.get_formatted_message(strategy_instance)
            # Wrap only table messages in triple backticks for Markdown/MarkdownV2
            if hasattr(comp, 'rows') and isinstance(strategy_instance, (MarkdownStrategy, MarkdownV2Strategy)):
                formatted_message = f"```\n{formatted_message}\n```"
            formatted_components.append(formatted_message)
        return self.separator.join(formatted_components)

    def __str__(self):
        """
        Convert the composite message to a string using the default strategy.

        Returns:
            str: The formatted composite message using the default strategy.
        """
        return self.get_formatted_message()