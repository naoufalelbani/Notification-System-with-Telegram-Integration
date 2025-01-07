from messages.alert.alert_message import AlertMessage
from messages.alert.alert_icon import AlertIcon  # Assuming AlertIcon is defined in alert_icon.py

class AlertMessageBuilder:
    def __init__(self):
        self.message = ""
        self.icon = AlertIcon.WARNING  # Default to no icon
        self.alert_label = "Alert:"  # Default to "Alert:"

    def with_message(self, message):
        """
        Set the message content.

        Args:
            message (str): The message content.

        Returns:
            AlertMessageBuilder: The builder instance.
        """
        self.message = message
        return self

    def with_icon(self, icon: AlertIcon):
        """
        Set the icon for the alert message.

        Args:
            icon (AlertIcon): The icon to use for the alert.

        Returns:
            AlertMessageBuilder: The builder instance.
        """
        if not isinstance(icon, AlertIcon):
            raise TypeError("Icon must be an instance of AlertIcon")
        self.icon = icon
        return self

    def with_alert_label(self, alert_label):
        """
        Set the alert label (e.g., "Alert:", "Warning:").

        Args:
            alert_label (str): The label to use for the alert.

        Returns:
            AlertMessageBuilder: The builder instance.
        """
        self.alert_label = alert_label
        return self

    def build(self):
        """
        Build the AlertMessage.

        Returns:
            AlertMessage: The constructed AlertMessage.

        Raises:
            ValueError: If the message is empty.
        """
        if not self.message:
            raise ValueError("Message is required for AlertMessage")
        return AlertMessage(self.message, self.icon, self.alert_label)