import asyncio
from utils import get_logger
from notifier import TelegramNotifier, Notifier

logger = get_logger("Sniper")

async def main():
  print("Hello world!")
  logger.info("Hello")
  
  notifier = Notifier()
  telegram = TelegramNotifier()
  
  notifier.add_observer(telegram)
  
  notifier.notify_observers("*Starting* the bot...")
  
  
  
  pass

if __name__ == "__main__":
  asyncio.run(main())