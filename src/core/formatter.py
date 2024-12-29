from abc import ABC, abstractmethod

class Formatter(ABC):
    """Abstract base class for all formatters."""
    @abstractmethod
    def format(self, data):
        """Format the input data."""
        pass
