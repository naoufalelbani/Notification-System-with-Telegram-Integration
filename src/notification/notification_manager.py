from config.settings import TELEGRAM_BOT_TOKEN
from messages.composite.composite_message import CompositeMessage
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
        self._setup_logging()

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
            message (str or Message): The message to send. If it's a Message object, it will be formatted using its strategy.
            parse_mode (str, optional): The parse mode for the message (e.g., 'MarkdownV2', 'HTML', 'plain').
                                       If None, it will be inferred from the default strategy or the message's strategy.
        """
        if not self.chats:
            logging.warning("No chats registered to notify.")
            return

        # Determine the parse mode if not provided
        if parse_mode is None:
            parse_mode = self._determine_parse_mode(message)

        # Format the message if it's a Message object
        formatted_message = self._format_message(message)

        # Send the message to all registered chats
        for chat_id in self.chats:
            try:
                command = NotificationCommand(self.bot, chat_id, formatted_message, parse_mode)
                command.execute()
                logging.info(f"Message sent to chat {chat_id}.")
            except Exception as e:
                logging.error(f"Failed to send message to chat {chat_id}: {e}")

    def _setup_logging(self):
        """Set up logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def _determine_parse_mode(self, message):
        """
        Determine the parse mode based on the message and the default strategy.

        Args:
            message: The message to send.

        Returns:
            str: The inferred parse mode.
        """
        # If the message has a strategy, use it to infer the parse mode
        if hasattr(message, 'get_formatted_message'):
            strategy = message.default_strategy if hasattr(message, 'default_strategy') else None
            if strategy:
                return self._infer_parse_mode_from_strategy(strategy)

        # Fall back to the class-level default strategy
        if self._default_strategy:
            return self._infer_parse_mode_from_strategy(self._default_strategy)

        # Default to Markdown if no strategy is set
        return "Markdown"

    def _infer_parse_mode_from_strategy(self, strategy):
        """
        Infer the parse mode based on the strategy.

        Args:
            strategy: The formatting strategy.

        Returns:
            str: The inferred parse mode.
        """
        strategy_name = strategy.__name__
        if strategy_name == "MarkdownV2Strategy":
            return "MarkdownV2"
        elif strategy_name == "HTMLStrategy":
            return "HTML"
        elif strategy_name == "PlainTextStrategy":
            return "plain"
        else:
            return "Markdown"

    def _format_message(self, message):
        """
        Format the message if it's a Message object.

        Args:
            message: The message to format.

        Returns:
            str: The formatted message.
        """
        if hasattr(message, 'get_formatted_message'):
            # If the message is a CompositeMessage, pass the strategy class
            if isinstance(message, CompositeMessage):
                return message.get_formatted_message(self._default_strategy)
            # For other Message objects, use the default strategy instance
            strategy = self._default_strategy() if self._default_strategy else None
            if strategy:
                return message.get_formatted_message(strategy)
        return str(message)