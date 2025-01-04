from strategies.formatting_strategy import FormattingStrategy
from tabulate import tabulate

class MarkdownV2Strategy(FormattingStrategy):
    def format(self, message_content):
        """
        Format the message content using MarkdownV2 syntax.

        Args:
            message_content (dict): The content of the message.

        Returns:
            str: The formatted message in MarkdownV2 syntax.
        """
        if 'rows' in message_content:
            # Table formatting for MarkdownV2
            title = f"*{self.escape_markdown_v2(message_content['title'])}*\n" if message_content.get('title') else ""
            headers = [self.escape_markdown_v2(header) for header in message_content.get('headers', [])]
            rows = [[self.escape_markdown_v2(str(cell)) for cell in row] for row in message_content['rows']]
            table = tabulate(rows, headers=headers, tablefmt="pipe")  # Use "pipe" for MarkdownV2 compatibility
            return title + self.escape_markdown_v2(table)
        elif 'items' in message_content:
            # List formatting for MarkdownV2
            items = [self.escape_markdown_v2(item) for item in message_content['items']]
            return "\n".join([f"• {item}" for item in items])
        elif 'icon' in message_content and 'alert_label' in message_content and 'message' in message_content:
            # Alert formatting for MarkdownV2
            icon = self.escape_markdown_v2(message_content['icon'])
            alert_label = self.escape_markdown_v2(message_content['alert_label'])
            message = self.escape_markdown_v2(message_content['message'])
            return f"{icon} **{alert_label}** {message}"
        elif 'text' in message_content:
            # Quote formatting for MarkdownV2
            text = self.escape_markdown_v2(message_content['text'])
            author = self.escape_markdown_v2(message_content.get('author', ''))
            if author:
                return f'> "{text}"\n> — {author}'
            return f'> "{text}"'
        else:
            raise ValueError("Unsupported message content for MarkdownV2 formatting")

    def escape_markdown_v2(self, text):
        """
        Escape reserved characters for MarkdownV2.

        Args:
            text (str): The text to escape.

        Returns:
            str: The escaped text.
        """
        if not text:
            return text
        # List of reserved characters in MarkdownV2
        reserved_chars = "_*[]()~`>#+-=|{}.!"
        return "".join(f"\\{char}" if char in reserved_chars else char for char in text)

    def __str__(self):
        return "MarkdownV2"