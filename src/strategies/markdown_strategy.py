from strategies import FormattingStrategy
from tabulate import tabulate

class MarkdownStrategy(FormattingStrategy):
    def format(self, message_content):
        if 'type' in message_content and message_content['type'] == 'alert':
            # Alert formatting
            icon = message_content.get('icon', '⚠️')
            return f"{icon} **Alert:** {message_content['message']}"
        elif 'rows' in message_content:
            # Table formatting
            title = f"{message_content['title']}\n" if message_content['title'] != "" else ""
            table = tabulate(message_content['rows'], headers=message_content.get('headers', []), tablefmt="rounded_outline")
            return title + table
        elif 'items' in message_content:
            # List formatting
            return "\n".join([f"- {item}" for item in message_content['items']])
        else:
            raise ValueError("Unsupported message content for Markdown formatting")