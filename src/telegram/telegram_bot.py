import requests

class TelegramBot:
    _instance = None

    def __new__(cls, bot_token):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.bot_token = bot_token
        return cls._instance

    def send_message(self, chat_id, message, parse_mode='plain'):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": str(message),  # Convert message to string
            "parse_mode": parse_mode
        }
        print(f"Sending message: {payload['text']}")  # Debugging
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            raise Exception(f"Failed to send message: {response.text}")