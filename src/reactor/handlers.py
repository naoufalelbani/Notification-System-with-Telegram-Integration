import logging

from messages.alert import AlertMessageBuilder, AlertIcon
from messages.composite import CompositeMessageBuilder
from strategies import HTMLStrategy
from messages.quote import QuoteMessageBuilder
from messages.table import TableMessageBuilder

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



class QuoteHandler:
    def handle(self, message):
        """
        Handle a quote message.

        Args:
            message (dict): The incoming message.
        """
        try:
            # Build the quote message
            quote_message = QuoteMessageBuilder()
            quote_message.with_text(message['content']['text'])
            if 'author' in message['content']:
                quote_message.with_author(message['content']['author'])
            
            # Create a composite message
            composite_message = CompositeMessageBuilder()
            composite_message.add_component(quote_message.build())
            composite_message.with_default_strategy(HTMLStrategy)

            logging.info(f"Quote message built: {quote_message.build()}")
            logging.info(f"Composite message built: {composite_message.build()}")

            return composite_message.build()
        except Exception as e:
            logging.error(f"Error building quote message: {e}")
            raise

class TableHandler:
    def handle(self, message):
        """
        Handle a table message.

        Args:
            message (dict): The incoming message.
        """
        try:
            # Build the table message
            table_message = TableMessageBuilder()
            table_message.with_title(message['content'].get('title', ''))
            table_message.with_headers(message['content']['headers'])
            table_message.with_rows(message['content']['rows'])
            
            # Create a composite message
            composite_message = CompositeMessageBuilder()
            composite_message.add_component(table_message.build())
            composite_message.with_default_strategy(HTMLStrategy)

            logging.info(f"Table message built: {table_message.build()}")
            logging.info(f"Composite message built: {composite_message.build()}")

            return composite_message.build()
        except Exception as e:
            logging.error(f"Error building table message: {e}")
            raise