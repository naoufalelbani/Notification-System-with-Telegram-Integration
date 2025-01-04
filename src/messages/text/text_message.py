from messages.message import Message

class TextMessage(Message):
    """
    Represents a simple text message.
    """

    def __init__(self, text):
        """
        Initialize a TextMessage.

        Args:
            text (str): The text content of the message.
        """
        self.text = text

    def get_formatted_message(self, strategy):
        """
        Format the text message using the provided strategy.

        Args:
            strategy: The formatting strategy to use.

        Returns:
            str: The formatted text message.
        """
        return strategy.format({
            'type': 'text',
            'text': self.text
        })