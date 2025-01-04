from config.settings import TELEGRAM_BOT_TOKEN
from telegram import TelegramBot
from commands import NotificationCommand
import logging

class NotificationManager:
    # Class-level default strategy
    _default_strategy = None

    def __init__(self):
        """
        Initialize the NotificationManager with an empty set of chat IDs.
        """
        self.chats = set()
        self.bot = TelegramBot(TELEGRAM_BOT_TOKEN)
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    @classmethod
    def with_default_strategy(cls, strategy):
        """
        Set the default strategy for all instances of NotificationManager.

        Args:
            strategy: The default formatting strategy (e.g., MarkdownV2Strategy).
        """
        cls._default_strategy = strategy
        logging.info(f"Default strategy set to {strategy.__name__}.")
        return cls

    def register_chat(self, chat_id):
        """
        Register a chat ID to receive notifications.

        Args:
            chat_id (str): The chat ID to register.
        """
        if chat_id not in self.chats:
            self.chats.add(chat_id)
            logging.info(f"Chat {chat_id} registered for notifications.")
        else:
            logging.warning(f"Chat {chat_id} is already registered.")

    def unregister_chat(self, chat_id):
        """
        Unregister a chat ID from receiving notifications.

        Args:
            chat_id (str): The chat ID to unregister.
        """
        if chat_id in self.chats:
            self.chats.remove(chat_id)
            logging.info(f"Chat {chat_id} unregistered from notifications.")
        else:
            logging.warning(f"Chat {chat_id} is not registered.")

    def notify_observers(self, message, parse_mode=None):
        """
        Notify all registered chat IDs with the given message.

        Args:
            message (str or dict): The message to send. If a dict, it will be formatted using the default strategy.
            parse_mode (str): The parse mode for the message (e.g., 'MarkdownV2', 'HTML', 'plain').
                             If None, it will be inferred from the default strategy.
        """
        if not self.chats:
            logging.warning("No chats registered to notify.")
            return
        
        # If the message is a dict, format it using the default strategy
        # if isinstance(message, dict):
        if hasattr(message, 'default_strategy') and self._default_strategy is None:
            strategy = message.default_strategy.__name__
            print(f"Strategy: {strategy}")
        else:
            strategy = self._default_strategy.__name__
                    
        # if self._default_strategy is None:
        #     raise ValueError("No default strategy set. Use .with_default_strategy() to set one.")
        # message = self._default_strategy().format(message)
        if parse_mode is None:
            # Infer parse_mode from the default strategy
            if strategy == "MarkdownV2Strategy":
                parse_mode = "MarkdownV2"
            elif strategy == "HTMLStrategy":
                parse_mode = "HTML"
            else:
                parse_mode = "Markdown"
            

        for chat_id in self.chats:
            try:
                command = NotificationCommand(self.bot, chat_id, message, parse_mode)
                command.execute()
                logging.info(f"Message sent to chat {chat_id}.")
            except Exception as e:
                logging.error(f"Failed to send message to chat {chat_id}: {e}")