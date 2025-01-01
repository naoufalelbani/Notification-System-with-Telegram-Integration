from strategies import FormattingStrategy

class PlainTextStrategy(FormattingStrategy):
    def format(self, message_content):
        if 'title' in message_content:
            # Table formatting
            title = f"{message_content['title']}\n"
            headers = " | ".join(message_content['headers']) + "\n"
            separator = "-" * len(headers) + "\n"
            rows = "\n".join([" | ".join(row) for row in message_content['rows']])
            return title + headers + separator + rows
        elif 'items' in message_content:
            # List formatting
            return "\n".join([f"- {item}" for item in message_content['items']])
        elif 'message' in message_content:
            # Alert formatting
            return f"Alert: {message_content['message']}"
        else:
            raise ValueError("Unsupported message content for Plain Text formatting")