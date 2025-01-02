from strategies import FormattingStrategy
from tabulate import tabulate

class PlainTextStrategy(FormattingStrategy):
    def format(self, message_content):
        if 'title' in message_content:
            # Table formatting
            title = f"{message_content['title']}\n"
            table = tabulate(message_content['rows'], headers=message_content['headers'], tablefmt="rounded_outline")
            return title + table
        elif 'items' in message_content:
            # List formatting
            return "\n".join([f"- {item}" for item in message_content['items']])
        elif 'message' in message_content:
            # Alert formatting
            return f"Alert: {message_content['message']}"
        else:
            raise ValueError("Unsupported message content for Plain Text formatting")