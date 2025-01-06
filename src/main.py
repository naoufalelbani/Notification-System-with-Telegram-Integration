from utils import setup_logging
from reactor.reactor import Reactor
from reactor.handlers import AlertHandler, QuoteHandler, TableHandler

def main():
    setup_logging()

    # Initialize the Reactor
    reactor = Reactor(zmq_address="tcp://*:5555")

    # Register handlers for different message types
    reactor.register_handler("alert", AlertHandler().handle)
    reactor.register_handler("quote", QuoteHandler().handle)
    reactor.register_handler("table", TableHandler().handle)

    # Start the Reactor
    reactor.start()

if __name__ == "__main__":
    main()