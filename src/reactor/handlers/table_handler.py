import logging

from messages.table import TableMessageBuilder
from messages.composite import CompositeMessageBuilder
from strategies import HTMLStrategy

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