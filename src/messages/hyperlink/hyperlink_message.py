from messages.message import Message

class HyperlinkMessage(Message):
    """
    Represents a message containing an Hyperlink.
    """

    def __init__(self, text, url):
        """
        Initialize an HyperlinkMessage.

        Args:
            text (str): The display text for the URL.
            url (str): The URL to link to.
        """
        self.text = text
        self.url = url

    def get_formatted_message(self, strategy):
        """
        Format the Hyperlink message using the provided strategy.

        Args:
            strategy: The formatting strategy to use.

        Returns:
            str: The formatted Hyperlink message.
        """
        return strategy.format({
            'type': 'hyperlink',
            'text': self.text,
            'url': self.url
        })