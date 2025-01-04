import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Validate required environment variables
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in the environment variables.")
if not TELEGRAM_CHAT_ID:
    raise ValueError("TELEGRAM_CHAT_ID is not set in the environment variables.")