from core.formatter import Formatter

class AlertFormatter(Formatter):
  """Formats messages as alerts with a title and message."""
  def __init__(self, alert_symbol="⚠️"):
    self.alert_symbol = alert_symbol
  
  def format(self, data):
    """
    Formats the alert message.

    Expected input: A dictionary with keys 'title' and 'message'.
    Example: {"title": "Server Down", "message": "The main server is unresponsive."}
    """
    if not isinstance(data, dict) or "title" not in data or "message" not in data:
      raise ValueError("Input data must be a dictionary with 'title' and 'message' keys.")
    
    return f"{self.alert_symbol} *{data['title']}*: {data['message']}"
