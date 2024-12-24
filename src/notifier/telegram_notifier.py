from notifier import Observer
from abc import abstractmethod
from utils import get_logger
from config import TELEGRAM_BOT_TOKEN,TELEGRAM_CHAT_ID
import requests # type: ignore

logger = get_logger(__name__)

class TelegramNotifier(Observer):
  
  def __init__(self):
    self.url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
  
  def update(self, message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
      raise ValueError("Telegram bot token and chat ID must be set in the environment.")
    
    payload = {
      "chat_id": TELEGRAM_CHAT_ID,
      "text": message,
      "parse_mode": "Markdown"
    }
    
    response = requests.post(self.url, json=payload)
    
    if response.status_code != 200:
      raise Exception(f"Failed to send message: {response.text}")
    return response.json()
    