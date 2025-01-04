from telegram import TelegramBot

class NotificationCommand:
    def __init__(self, bot: TelegramBot, chat_id: str, message: str, parse_mode='Markdown'):
        self.bot = bot
        self.chat_id = chat_id
        self.message = message
        self.parse_mode = parse_mode

    def execute(self):
        self.bot.send_message(self.chat_id, self.message, self.parse_mode)