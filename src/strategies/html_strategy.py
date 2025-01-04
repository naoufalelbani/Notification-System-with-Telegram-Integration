# src/strategies/html_strategy.py
from strategies.formatting_strategy import FormattingStrategy

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
        elif 'icon' in message_content and 'alert_label' in message_content and 'message' in message_content:
            # Alert formatting
            icon = message_content['icon']
            alert_label = f"<strong>{message_content['alert_label']}</strong>"
            message = message_content['message']
            return f"{icon} {alert_label} {message}"
        elif 'text' in message_content:
            # Quote formatting
            text = message_content['text']
            author = message_content.get('author')
            if author:
                return f'<blockquote>"{text}"</blockquote><p>— {author}</p>'
            return f'<blockquote>"{text}"</blockquote>'
        else:
            raise ValueError("Unsupported message content for HTML formatting")