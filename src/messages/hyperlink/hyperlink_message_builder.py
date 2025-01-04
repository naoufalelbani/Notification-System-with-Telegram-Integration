from messages.hyperlink.hyperlink_message import HyperlinkMessage


class HyperlinkMessageBuilder:
    """
    Builder for creating HyperlinkMessage instances.
    """

    def __init__(self):
        self.text = ""
        self.url = ""

    def with_text(self, text):
        """
        Set the display text for the URL.

        Args:
            text (str): The display text.

        Returns:
            HyperlinkMessageBuilder: The builder instance.
        """
        self.text = text
        return self

    def with_url(self, url):
        """
        Set the URL to link to.

        Args:
            url (str): The URL.

        Returns:
            HyperlinkMessageBuilder: The builder instance.
        """
        self.url = url
        return self

    def build(self):
        """
        Build the HyperlinkMessage.

        Returns:
            HyperlinkMessage: The constructed HyperlinkMessage.

        Raises:
            ValueError: If the text or URL is empty.
        """
        if not self.text or not self.url:
            raise ValueError("Text and URL are required for HyperlinkMessage")
        return HyperlinkMessage(self.text, self.url)