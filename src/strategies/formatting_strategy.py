from abc import ABC, abstractmethod
from tabulate import tabulate

class FormattingStrategy(ABC):
    """
    Abstract base class for formatting strategies.
    Defines the template method and abstract methods for specific formatting steps.
    """

    def format(self, message_content):
        """
        Template method for formatting message content.

        Args:
            message_content (dict): The content of the message.

        Returns:
            str: The formatted message.

        Raises:
            ValueError: If the message content is unsupported.
        """
        if 'rows' in message_content:
            return self._format_table(message_content)
        elif 'items' in message_content:
            return self._format_list(message_content)
        elif 'type' in message_content and message_content['type'] == 'hyperlink':
            return self._format_hyperlink(message_content)
        elif 'type' in message_content and message_content['type'] == 'text':
            return self._format_text(message_content)
        elif 'icon' in message_content and 'alert_label' in message_content and 'message' in message_content:
            return self._format_alert(message_content)
        elif 'text' in message_content:
            return self._format_quote(message_content)
        else:
            raise ValueError("Unsupported message content for formatting")

    @abstractmethod
    def _format_table(self, message_content):
        """Format a table message."""
        pass

    @abstractmethod
    def _format_list(self, message_content):
        """Format a list message."""
        pass

    @abstractmethod
    def _format_alert(self, message_content):
        """Format an alert message."""
        pass

    @abstractmethod
    def _format_quote(self, message_content):
        """Format a quote message."""
        pass
    
    @abstractmethod
    def _format_hyperlink(self, message_content):
        """Format a hyperlink message."""
        pass
    
    @abstractmethod
    def _format_text(self, message_content):
        """Format a text message."""
        pass

    @abstractmethod
    def escape(self, text):
        """
        Escape reserved characters for the specific formatting syntax.

        Args:
            text (str): The text to escape.

        Returns:
            str: The escaped text.
        """
        pass