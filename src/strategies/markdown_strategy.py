# src/strategies/markdown_strategy.py
from strategies.formatting_strategy import FormattingStrategy
from tabulate import tabulate

class MarkdownStrategy(FormattingStrategy):
    def format(self, message_content):
        if 'rows' in message_content:
            # Table formatting
            title = f"{message_content['title']}\n" if message_content['title'] != "" else ""
            table = tabulate(message_content['rows'], headers=message_content.get('headers', []), tablefmt="rounded_outline")
            return title + table
        elif 'items' in message_content:
            # List formatting
            return "\n".join([f"- {item}" for item in message_content['items']])
        elif 'icon' in message_content and 'alert_label' in message_content and 'message' in message_content:
            # Alert formatting
            icon = message_content['icon']
            alert_label = f"**{message_content['alert_label']}**"  # Bold the alert_label
            message = message_content['message']
            return f"{icon} {alert_label} {message}"
        elif 'text' in message_content:
            # Quote formatting
            text = message_content['text']
            author = message_content.get('author')
            if author:
                return f'> "{text}"\n> — {author}'
            return f'> "{text}"'
        else:
            raise ValueError("Unsupported message content for Markdown formatting")