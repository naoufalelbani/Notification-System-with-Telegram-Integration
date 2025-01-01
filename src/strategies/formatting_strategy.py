from abc import ABC, abstractmethod

class FormattingStrategy(ABC):
    """
    Abstract base class for formatting strategies.
    Defines the interface for formatting message content.
    """

    @abstractmethod
    def format(self, message_content):
        """
        Format the message content.

        Args:
            message_content (dict): The content of the message.

        Returns:
            str: The formatted message.
        """
        pass