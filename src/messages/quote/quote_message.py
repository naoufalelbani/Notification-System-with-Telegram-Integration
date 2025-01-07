from messages.message import Message

class QuoteMessage(Message):
    def __init__(self, text, author=None):
        """
        Initialize a QuoteMessage.

        Args:
            text (str): The text of the quote.
            author (str, optional): The author of the quote. Defaults to None.
        """
        self.text = text
        self.author = author

    def get_formatted_message(self, strategy):
        """
        Format the quote message using the provided strategy.

        Args:
            strategy: The formatting strategy to use.

        Returns:
            str: The formatted quote message.
        """
        return strategy.format({
            'text': self.text,
            'author': self.author
        })