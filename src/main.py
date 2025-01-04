from messages.table import TableMessageBuilder
from messages.alert import AlertMessageBuilder,AlertIcon
from messages.list import ListMessageBuilder
from messages.composite import CompositeMessageBuilder
from notification.notification_manager import NotificationManager
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def main():
    # Build a composite message
    builder = CompositeMessageBuilder()
    composite_message = builder.add_component(
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
    ).build()

    # Send the message using MarkdownV2
    manager = NotificationManager()
    manager.register_chat(TELEGRAM_CHAT_ID)
    manager.notify_observers(composite_message, parse_mode='Markdown')

if __name__ == "__main__":
    main()