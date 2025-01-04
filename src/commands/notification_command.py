from telegram import TelegramBot

class NotificationCommand:
    def __init__(self, bot: TelegramBot, chat_id: str, message: str, parse_mode='Markdown'):
        """
        Initialize the NotificationCommand.

        Args:
            bot (TelegramBot): The TelegramBot instance to use for sending the message.
            chat_id (str): The chat ID to send the message to.
            message (str): The message content to send.
            parse_mode (str): The parse mode for the message (e.g., 'MarkdownV2', 'HTML', 'plain').
        """
        self.bot = bot
        self.chat_id = chat_id
        self.message = message
        self.parse_mode = parse_mode

    def execute(self):
        """
        Execute the command by sending the message using the TelegramBot.
        """
        try:
            self.bot.send_message(self.chat_id, self.message, self.parse_mode)
        except Exception as e:
            raise Exception(f"Failed to execute NotificationCommand: {e}")