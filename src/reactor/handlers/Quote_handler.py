import logging

from messages.quote import QuoteMessageBuilder
from messages.composite import CompositeMessageBuilder
from strategies import HTMLStrategy

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