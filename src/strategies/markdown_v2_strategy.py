# src/strategies/markdown_v2_strategy.py
from strategies.formatting_strategy import FormattingStrategy
from tabulate import tabulate

class MarkdownV2Strategy(FormattingStrategy):
    def format(self, message_content):
        if 'rows' in message_content:
            # Table formatting for MarkdownV2
            title = f"*{self.escape_markdown_v2(message_content['title'])}*\n" if message_content['title'] != "" else ""
            headers = [self.escape_markdown_v2(header) for header in message_content.get('headers', [])]
            rows = [[self.escape_markdown_v2(str(cell)) for cell in row] for row in message_content['rows']]
            table = tabulate(rows, headers=headers, tablefmt="rounded_outline")
            return title + table
        elif 'items' in message_content:
            # List formatting for MarkdownV2
            items = [self.escape_markdown_v2(item) for item in message_content['items']]
            return "\n".join([f"• {item}" for item in items])
        elif 'icon' in message_content and 'alert_label' in message_content and 'message' in message_content:
            # Alert formatting for MarkdownV2
            icon = self.escape_markdown_v2(message_content['icon'])
            alert_label = f"**{self.escape_markdown_v2(message_content['alert_label'])}**"  # Bold the alert_label
            message = self.escape_markdown_v2(message_content['message'])
            return f"{icon} *{alert_label}:* {message}"
        else:
            raise ValueError("Unsupported message content for MarkdownV2 formatting")

    def escape_markdown_v2(self, text):
        """
        Escape special characters for MarkdownV2.

        Args:
            text (str): The text to escape.

        Returns:
            str: The escaped text.
        """
        if not text:
            return text
        escape_chars = "_*[]()~`>#+-=|{}.!"
        return "".join(f"\\{char}" if char in escape_chars else char for char in text)