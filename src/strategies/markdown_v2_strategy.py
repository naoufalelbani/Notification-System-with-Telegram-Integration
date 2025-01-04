from strategies.formatting_strategy import FormattingStrategy
from tabulate import tabulate

class MarkdownV2Strategy(FormattingStrategy):
    """
    A formatting strategy for MarkdownV2 syntax.
    """

    def _format_table(self, message_content):
        title = self._format_title(message_content.get('title', ''))
        headers = [self.escape(header) for header in message_content.get('headers', [])]
        rows = [[self.escape(str(cell)) for cell in row] for row in message_content['rows']]
        table = tabulate(rows, headers=headers, tablefmt="rounded_outline")
        return title + self.escape(table)
    
    def _format_hyperlink(self, message_content):
        """
        Format an inline URL message in MarkdownV2 syntax.

        Args:
            message_content (dict): The content of the inline URL message.

        Returns:
            str: The formatted inline URL message.
        """
        text = self.escape(message_content['text'])
        url = self.escape(message_content['url'])
        return f'[{text}]({url})'
    
    def _format_text(self, message_content):
        """
        Format a text message in MarkdownV2 syntax.

        Args:
            message_content (dict): The content of the text message.

        Returns:
            str: The formatted text message.
        """
        text = self.escape(message_content['text'])
        return text

    def _format_list(self, message_content):
        items = [self.escape(item) for item in message_content['items']]
        return "\n".join([f"• {item}" for item in items])

    def _format_alert(self, message_content):
        icon = self.escape(message_content['icon'])
        alert_label = self.escape(message_content['alert_label'])
        message = self.escape(message_content['message'])
        return f"{icon} *{alert_label}:* {message}"

    def _format_quote(self, message_content):
        text = self.escape(message_content['text'])
        author = self.escape(message_content.get('author', ''))
        if author:
            return f'> "{text}"\n> — {author}'
        return f'> "{text}"'

    def _format_title(self, title):
        if title:
            return f"*{self.escape(title)}*\n"
        return ""

    def escape(self, text):
        if not text:
            return text
        reserved_chars = "_*[]()~`>#+-=|{}.!"
        return "".join(f"\\{char}" if char in reserved_chars else char for char in text)

    def __str__(self):
        return "MarkdownV2"