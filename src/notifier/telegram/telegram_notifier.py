from core.formatter import Formatter
from core.notifier import Observer
from abc import abstractmethod
from utils import get_logger
from config import TELEGRAM_BOT_TOKEN,TELEGRAM_CHAT_ID
import requests # type: ignore

logger = get_logger(__name__)

class TelegramNotifier(Observer):
  """Notifier for sending formatted messages to Telegram."""
  def __init__(self, formatter: Formatter = None):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
      raise ValueError("Telegram bot token and chat ID must be set in the environment.")
    self.url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    self.formatter = formatter
  
  def update(self, message):
    
    if self.formatter != None:
      """Format the data and send it to Telegram."""
      formatted_message = self.formatter.format(message)
    else:
      formatted_message = message
    
    payload = {
      "chat_id": TELEGRAM_CHAT_ID,
      "text": f"```\n{formatted_message}\n```",
      "parse_mode": "MarkdownV2"
    }
    
    response = requests.post(self.url, json=payload)
    
    if response.status_code != 200:
      raise Exception(f"Failed to send message: {response.text}")
    return response.json()
    