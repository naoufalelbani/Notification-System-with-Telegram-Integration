from config.settings import TELEGRAM_BOT_TOKEN
from telegram import TelegramBot
from commands import NotificationCommand


class NotificationManager:
    def __init__(self):
        self.chats = set()

    def register_chat(self, chat_id):
        self.chats.add(chat_id)

    def unregister_chat(self, chat_id):
        self.chats.remove(chat_id)

    def notify_observers(self, message, parse_mode='plain'):
        bot = TelegramBot(TELEGRAM_BOT_TOKEN)
        for chat_id in self.chats:
            command = NotificationCommand(bot, chat_id, message, parse_mode)
            command.execute()