import zmq
import logging
import json
from typing import Callable, Dict

from config.settings import TELEGRAM_CHAT_ID
from notification import NotificationManager

class Reactor:
    def __init__(self, zmq_address: str = "tcp://*:5555"):
        self.zmq_address = zmq_address
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)  # Change to SUB
        self.socket.bind(self.zmq_address)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "telegram-notifier")  # Subscribe to specific topic
        self.handlers: Dict[str, Callable] = {}
        self.running = False

    def register_handler(self, message_type: str, handler: Callable):
        self.handlers[message_type] = handler

    def start(self):
        self.running = True
        logging.info(f"Reactor started and listening on {self.zmq_address}...")

        while self.running:
            try:
                # Wait for incoming messages
                logging.info("Waiting for messages...")
                topic, message = self.socket.recv_multipart()  # Receive topic and message
                message = json.loads(message.decode('utf-8'))  # Decode the message
                logging.info(f"Received message on topic '{topic.decode('utf-8')}': {message}")

                # Dispatch the message to the appropriate handler
                message_type = message.get("type", "default")
                logging.info(f"Message type: {message_type}")
                handler = self.handlers.get(message_type, self._default_handler)
                logging.info(f"Handler for message type '{message_type}': {handler}")

                handler_message = handler(message)
                logging.info(f"Handler message: {handler_message}")

                # Send the message to the NotificationManager
                manager = NotificationManager()
                manager.register_chat(TELEGRAM_CHAT_ID)
                manager.notify_observers(handler_message)

            except KeyboardInterrupt:
                logging.info("Shutting down Reactor...")
                self.running = False
            except Exception as e:
                logging.error(f"Error processing message: {e}")

    def _default_handler(self, message):
        logging.warning(f"No handler registered for message type: {message.get('type')}")