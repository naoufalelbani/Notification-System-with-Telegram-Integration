import asyncio
from utils import get_logger
from notifier import TelegramNotifier,TableFormatter
from core import Notifier

logger = get_logger("Sniper")

async def main():
  print("Hello world!")
  logger.info("Hello")
  
  notifier = Notifier()
  telegram = TelegramNotifier()
  
  headers = ["Name", "Age", "Country", "Gender"]
  data = [
      ["Alice", 30, "USA", "Male"],
      ["Bob", 25, "Canada", "Male"],
      ["Charlie", 35, "UK", "Male"],
  ]
  
  # Initialize TelegramNotifier with TableFormatter
  table_formatter = TableFormatter(headers=headers, tablefmt="rounded_outline")
  telegram.formatter = table_formatter
  
  notifier.add_observer(telegram)
  
  notifier.notify_observers(data)
  
  
  
  pass

if __name__ == "__main__":
  asyncio.run(main())