from messages.message import Message

class AlertMessage(Message):
    def __init__(self, message, icon=None, alert_label="Alert:"):
        """
        Initialize an AlertMessage.

        Args:
            message (str): The message content.
            icon (AlertIcon, optional): The icon to display. Defaults to None.
            alert_label (str, optional): The label for the alert (e.g., "Alert:", "Warning:"). Defaults to "Alert:".
        """
        self.message = message
        self.icon = icon  # Store the AlertIcon enum value
        self.alert_label = alert_label  # Store the alert label

    def get_formatted_message(self, strategy):
        """
        Format the message using the provided strategy.

        Args:
            strategy (FormattingStrategy): The strategy to use for formatting.

        Returns:
            str: The formatted message.
        """
        # Pass a dictionary with icon, alert_label, and message
        return strategy.format({
            'icon': self.icon.value if self.icon else "",
            'alert_label': self.alert_label,
            'message': self.message
        })