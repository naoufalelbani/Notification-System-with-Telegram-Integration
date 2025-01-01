from abc import ABC, abstractmethod
from strategies import FormattingStrategy

class Message(ABC):
    """
    Abstract base class for all message types.
    Defines the interface for formatting messages using a strategy.
    """

    @abstractmethod
    def get_formatted_message(self, strategy: FormattingStrategy):
        """
        Format the message using the provided strategy.

        Args:
            strategy: A formatting strategy (e.g., MarkdownStrategy, HTMLStrategy).

        Returns:
            str: The formatted message.
        """
        pass