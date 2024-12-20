import asyncio
from utils import get_logger

logger = get_logger("Sniper")

async def main():
  print("Hello world!")
  logger.info("Hello")
  pass

if __name__ == "__main__":
  asyncio.run(main())