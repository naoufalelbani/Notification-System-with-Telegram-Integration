import requests

class TelegramBot:
    _instance = None

    def __new__(cls, bot_token):
        """
        Create a singleton instance of TelegramBot.

        Args:
            bot_token (str): The token for the Telegram bot.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.bot_token = bot_token
            cls._instance.base_url = f"https://api.telegram.org/bot{bot_token}"
        return cls._instance

    def send_message(self, chat_id, message, parse_mode='Markdown'):
        """
        Send a message to a specified chat ID using the Telegram Bot API.

        Args:
            chat_id (str): The chat ID to send the message to.
            message (str): The message content to send.
            parse_mode (str): The parse mode for the message (e.g., 'MarkdownV2', 'HTML', 'plain').

        Raises:
            Exception: If the message fails to send.
        """
        
        print(f"Parse mode: {parse_mode}")
        
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": str(message),  # Ensure the message is a string
            "parse_mode": parse_mode
        }

        # Remove None values from the payload
        payload = {k: v for k, v in payload.items() if v is not None}

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to send message: {e}")