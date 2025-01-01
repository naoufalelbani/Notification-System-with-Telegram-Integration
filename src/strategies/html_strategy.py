from strategies import FormattingStrategy

class HTMLStrategy(FormattingStrategy):
    def format(self, message_content):
        if 'title' in message_content:
            # Table formatting
            title = f"<h3>{message_content['title']}</h3>"
            headers = "<tr><th>" + "</th><th>".join(message_content['headers']) + "</th></tr>"
            rows = "".join(["<tr><td>" + "</td><td>".join(row) + "</td></tr>" for row in message_content['rows']])
            return f"{title}<table>{headers}{rows}</table>"
        elif 'items' in message_content:
            # List formatting
            return "<ul>" + "".join([f"<li>{item}</li>" for item in message_content['items']]) + "</ul>"
        elif 'message' in message_content:
            # Alert formatting
            return f"<strong>⚠️ Alert:</strong> {message_content['message']}"
        else:
            raise ValueError("Unsupported message content for HTML formatting")