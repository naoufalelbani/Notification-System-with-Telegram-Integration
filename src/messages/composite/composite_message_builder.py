from messages.composite.composite_message import CompositeMessage
from messages.message import Message
from strategies import FormattingStrategy

class CompositeMessageBuilder:
    def __init__(self):
        self.components = []
        self.default_strategy = None  # Default to None

    def add_component(self, component: Message):
        """
        Add a component to the composite message.

        Args:
            component (Message): The component to add.

        Returns:
            CompositeMessageBuilder: The builder instance.

        Raises:
            TypeError: If the component is not an instance of Message.
        """
        if not isinstance(component, Message):
            raise TypeError("Component must be an instance of Message")
        self.components.append(component)
        return self

    def with_default_strategy(self, default_strategy: FormattingStrategy):
        """
        Set the default strategy for the composite message.

        Args:
            default_strategy (FormattingStrategy): The default strategy to use for formatting.

        Returns:
            CompositeMessageBuilder: The builder instance.
        """
        self.default_strategy = default_strategy
        return self

    def build(self):
        """
        Build the CompositeMessage.

        Returns:
            CompositeMessage: The constructed CompositeMessage.
        """
        return CompositeMessage(self.components, default_strategy=self.default_strategy)