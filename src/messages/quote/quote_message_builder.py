# src/messages/quote/quote_message_builder.py
from messages.quote.quote_message import QuoteMessage

class QuoteMessageBuilder:
    def __init__(self):
        self.text = ""
        self.author = None

    def with_text(self, text):
        """
        Set the text of the quote.

        Args:
            text (str): The text of the quote.

        Returns:
            QuoteMessageBuilder: The builder instance.
        """
        self.text = text
        return self

    def with_author(self, author):
        """
        Set the author of the quote.

        Args:
            author (str): The author of the quote.

        Returns:
            QuoteMessageBuilder: The builder instance.
        """
        self.author = author
        return self

    def build(self):
        """
        Build the QuoteMessage.

        Returns:
            QuoteMessage: The constructed QuoteMessage.

        Raises:
            ValueError: If the text is empty.
        """
        if not self.text:
            raise ValueError("Text is required for QuoteMessage")
        return QuoteMessage(self.text, self.author)