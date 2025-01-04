# src/strategies/plain_text_strategy.py
from strategies.formatting_strategy import FormattingStrategy
from tabulate import tabulate

class PlainTextStrategy(FormattingStrategy):
    def format(self, message_content):
        if 'rows' in message_content:
            # Table formatting
            title = f"{message_content['title']}\n" if message_content['title'] != "" else ""
            table = tabulate(message_content['rows'], headers=message_content['headers'], tablefmt="rounded_outline")
            return title + table
        elif 'items' in message_content:
            # List formatting
            return "\n".join([f"- {item}" for item in message_content['items']])
        elif 'icon' in message_content and 'alert_label' in message_content and 'message' in message_content:
            # Alert formatting
            icon = message_content['icon']
            alert_label = message_content['alert_label']
            message = message_content['message']
            return f"{icon} {alert_label} {message}"
        else:
            raise ValueError("Unsupported message content for Plain Text formatting")