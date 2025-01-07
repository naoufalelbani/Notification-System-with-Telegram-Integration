import logging

from messages.alert import AlertMessageBuilder, AlertIcon
from messages.composite import CompositeMessageBuilder
from strategies import HTMLStrategy

class AlertHandler:
    def handle(self, message):
        """
        Handle an alert message.

        Args:
            message (dict): The incoming message.
        """
        try:
            alert_message = AlertMessageBuilder()
            alert_message.with_alert_label(message['content']['alert_label'])
            alert_message.with_message(message['content']['message'])
            alert_message.with_icon(AlertIcon[message['content']['type']])
            
            # Create a composite message
            composite_message = CompositeMessageBuilder()
            composite_message.add_component(alert_message.build())
            composite_message.with_default_strategy(HTMLStrategy)
            

            # logging.info(f"Alert message built: {alert_message}")
            # logging.info(f"Composite message built: {composite_message}")

            return composite_message.build()
        except Exception as e:
            logging.error(f"Error building alert message: {e}")
            raise