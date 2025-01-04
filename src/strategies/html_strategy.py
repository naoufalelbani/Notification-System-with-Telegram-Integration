from tabulate import tabulate

from strategies.formatting_strategy import FormattingStrategy

class HTMLStrategy(FormattingStrategy):
    """
    A formatting strategy for HTML syntax.
    Supports only the HTML tags allowed by Telegram's parse_mode="HTML".
    """
    def _format_text(self, message_content):
        """
        Format a text message in HTML syntax.

        Args:
            message_content (dict): The content of the text message.

        Returns:
            str: The formatted text message.
        """
        text = self.escape(message_content['text'])
        return f"<p>{text}</p>"
    
    def _format_table(self, message_content):
        """
        Format a table message in HTML syntax using <pre> tags.

        Args:
            message_content (dict): The content of the table message.

        Returns:
            str: The formatted table message.
        """
        title = self._format_title(message_content.get('title', ''))
        headers = [self.escape(header) for header in message_content.get('headers', [])]
        rows = [[self.escape(str(cell)) for cell in row] for row in message_content['rows']]
        # Use tabulate to format the table as plain text
        table = tabulate(rows, headers=headers, tablefmt="rounded_outline")
        # Wrap the table in <pre> tags for pre-formatted fixed-width text
        return f"{title}<pre>{table}</pre>"
    
    def _format_hyperlink(self, message_content):
        """
        Format an inline URL message in HTML syntax.

        Args:
            message_content (dict): The content of the inline URL message.

        Returns:
            str: The formatted inline URL message.
        """
        text = self.escape(message_content['text'])
        url = self.escape(message_content['url'])
        return f'<a href="{url}">{text}</a>'

    def _format_list(self, message_content):
        """
        Format a list message in HTML syntax.

        Args:
            message_content (dict): The content of the list message.

        Returns:
            str: The formatted list message.
        """
        items = [self.escape(item) for item in message_content['items']]
        return "\n".join([f"• {item}" for item in items])  # Use plain text for lists

    def _format_alert(self, message_content):
        """
        Format an alert message in HTML syntax.

        Args:
            message_content (dict): The content of the alert message.

        Returns:
            str: The formatted alert message.
        """
        icon = self.escape(message_content['icon'])
        alert_label = f"<b>{self.escape(message_content['alert_label'])}</b>"
        message = self.escape(message_content['message'])
        return f"{icon} <b>{alert_label}:</b> {message}"

    def _format_quote(self, message_content):
        """
        Format a quote message in HTML syntax.

        Args:
            message_content (dict): The content of the quote message.

        Returns:
            str: The formatted quote message.
        """
        text = self.escape(message_content['text'])
        author = self.escape(message_content.get('author', ''))
        if author:
            return f'<blockquote>"{text}"</blockquote>\n— {author}'
        return f'<blockquote>"{text}"</blockquote>'

    def _format_title(self, title):
        """
        Format a title for HTML.

        Args:
            title (str): The title to format.

        Returns:
            str: The formatted title.
        """
        if title:
            return f"<b>{self.escape(title)}</b>\n"
        return ""

    def escape(self, text):
        """
        Escape reserved HTML characters.

        Args:
            text (str): The text to escape.

        Returns:
            str: The escaped text.
        """
        if not text:
            return text
        # Escape <, >, &, ", and '
        return (
            text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#39;")
        )

    def __str__(self):
        return "HTML"