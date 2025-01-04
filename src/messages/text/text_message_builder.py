from messages.text import TextMessage

class TextMessageBuilder:
    """
    Builder for creating TextMessage instances.
    """

    def __init__(self):
        self.text = ""

    def with_text(self, text):
        """
        Set the text content of the message.

        Args:
            text (str): The text content.

        Returns:
            TextMessageBuilder: The builder instance.
        """
        self.text = text
        return self

    def build(self):
        """
        Build the TextMessage.

        Returns:
            TextMessage: The constructed TextMessage.

        Raises:
            ValueError: If the text is empty.
        """
        if not self.text:
            raise ValueError("Text is required for TextMessage")
        return TextMessage(self.text)