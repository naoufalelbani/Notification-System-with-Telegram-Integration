![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

# Notification System with Telegram Integration

This project is a Python-based notification system that allows you to send formatted messages (e.g., alerts, tables, lists, hyperlinks, quotes, and text) to Telegram chats. It supports multiple formatting strategies, including Markdown, MarkdownV2, HTML, and Plain Text.

## Features

- **Composite Messages**: Combine multiple message types (e.g., alerts, tables, lists) into a single message.
- **Multiple Formatting Strategies**: Supports Markdown, MarkdownV2, HTML, and Plain Text formatting.
- **Telegram Integration**: Send messages to Telegram chats using a Telegram bot.
- **Builder Pattern**: Use builder classes to easily construct complex messages.
- **Customizable Alerts**: Add icons, labels, and custom messages to alerts.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/notification-system.git
   cd notification-system

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory and add your Telegram bot token and chat ID:
   ```plaintext
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   TELEGRAM_CHAT_ID=your-telegram-chat-id
   ```

## Usage

### Sending a Composite Message

You can send a composite message that includes an alert, a table, a list, a hyperlink, a quote, and a text message. Here's an example:

```python
from messages.hyperlink.hyperlink_message_builder import HyperlinkMessageBuilder
from messages.quote import QuoteMessageBuilder
from messages.table import TableMessageBuilder
from messages.alert import AlertMessageBuilder, AlertIcon
from messages.list import ListMessageBuilder
from messages.composite import CompositeMessageBuilder
from messages.text.text_message_builder import TextMessageBuilder
from notification.notification_manager import NotificationManager
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from strategies import MarkdownV2Strategy, MarkdownStrategy, PlainTextStrategy, HTMLStrategy

def main():
    # Build a composite message
    builder = CompositeMessageBuilder()
    composite_message = (
        builder.add_component(
            AlertMessageBuilder()
            .with_message("This is a sample report.")
            .with_alert_label("Note")
            .with_icon(AlertIcon.INFO)
            .build()
        ).add_component(
            TableMessageBuilder()
            .with_title("Sales Report")
            .with_headers(["Product", "Quantity"])
            .with_rows([["Apple", 100], ["Banana", 200]])
            .build()
        ).add_component(
            ListMessageBuilder()
            .with_items(["Item 1", "Item 2", "Item 3"])
            .build()
        ).add_component(
            HyperlinkMessageBuilder()
            .with_text("Visit our website")
            .with_url("http://www.example.com")
            .build()
        ).add_component(
            QuoteMessageBuilder()
            .with_text("The only limit to our realization of tomorrow is our doubts of today.")
            .with_author("Franklin D. Roosevelt")
            .build()
        ).add_component(
            TextMessageBuilder()
            .with_text("This is a simple paragraph.")
            .build()
        )
        .with_default_strategy(PlainTextStrategy)
        .build()
    )

    # Send the message using MarkdownV2
    manager = NotificationManager()
    manager.register_chat(TELEGRAM_CHAT_ID)
    manager.notify_observers(composite_message)

if __name__ == "__main__":
    main()
```

### Message Types

- **AlertMessage**: Displays an alert with an optional icon and label.
- **TableMessage**: Displays a table with a title, headers, and rows.
- **ListMessage**: Displays a list of items.
- **HyperlinkMessage**: Displays a clickable hyperlink.
- **QuoteMessage**: Displays a quote with an optional author.
- **TextMessage**: Displays a simple text message.

### Formatting Strategies

- **MarkdownStrategy**: Formats messages using Markdown syntax.
- **MarkdownV2Strategy**: Formats messages using MarkdownV2 syntax (Telegram-specific).
- **HTMLStrategy**: Formats messages using HTML syntax.
- **PlainTextStrategy**: Formats messages as plain text.

## Configuration

The project uses environment variables for configuration. You need to set the following variables in a `.env` file:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `TELEGRAM_CHAT_ID`: The chat ID where messages will be sent.

## Running Tests

To run the tests, use the following command:

```bash
invoke test
```

## Clearing Cache

To clear the cache (e.g., `__pycache__` directories), use the following command:

```bash
invoke clear_cache
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


### Key Sections in the README:
1. **Features**: Highlights the main features of the project.
2. **Installation**: Steps to set up the project locally.
3. **Usage**: Examples of how to use the system, including sending a composite message.
4. **Message Types**: Describes the different types of messages that can be sent.
5. **Formatting Strategies**: Explains the different formatting strategies available.
6. **Configuration**: Details the required environment variables.
7. **Running Tests**: Instructions for running tests.
8. **Clearing Cache**: How to clear cache directories.
9. **Contributing**: Guidelines for contributing to the project.
10. **License**: Information about the project's license.

This README provides a comprehensive guide for users to understand, set up, and use the notification system.