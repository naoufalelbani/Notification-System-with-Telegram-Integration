import asyncio
from notifier.telegram.formatters.alert import AlertFormatter
from utils import get_logger
from notifier import TelegramNotifier, TableFormatter
from core import Notifier

# Initialize the logger
logger = get_logger("Sniper")

# Function to send a startup notification
def send_startup_notification():
    telegram_starting = TelegramNotifier(formatter=AlertFormatter(alert_symbol="⚙️"))
    startup_message = {'title': 'Bot (Production)', 'message': 'Starting up...'}
    telegram_starting.update(startup_message)

# Function to send a table notification
def send_table_notification(notifier, headers, data):
    table_formatter = TableFormatter(headers=headers, tablefmt="rounded_outline")
    telegram = TelegramNotifier(formatter=table_formatter)
    notifier.add_observer(telegram)
    notifier.notify_observers(data)

# Main function to orchestrate the notifications
async def main():
    notifier_starting = Notifier()
    telegram_starting = TelegramNotifier(formatter=AlertFormatter(alert_symbol="⚙️"))
    notifier_starting.add_observer(telegram_starting)
    notifier_starting.notify_observers({'title': 'Bot (Production)', 'message': 'Starting up...'})
    logger.info("Application starting")
    
    # Send startup notification
    # send_startup_notification()
    
    # Prepare headers and data for table notification
    headers = ["Name", "Age", "Country", "Gender"]
    data = [
        ["Alice", 30, "USA", "Female"],
        ["Bob", 25, "Canada", "Male"],
        ["Charlie", 35, "UK", "Male"]
    ]
    
    # Create a notifier and send the table notification
    notifier = Notifier()
    send_table_notification(notifier, headers, data)

if __name__ == "__main__":
  asyncio.run(main())