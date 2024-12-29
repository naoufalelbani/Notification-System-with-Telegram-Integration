import pytest
from unittest.mock import patch, MagicMock

from notifier.telegram.formatters.alert import AlertFormatter
from notifier.telegram.formatters.table import TableFormatter
from core.notifier import Notifier
from notifier.telegram import TelegramNotifier

@pytest.fixture
def table_formatter():
  headers = ["Name", "Age", "Country"]
  return TableFormatter(headers=headers, tablefmt="grid")

@patch("notifier.telegram.telegram_notifier.requests.post")
def test_send_successfull(mock_post, table_formatter):
  # Mock the response
  mock_response = MagicMock()
  mock_response.status_code = 200
  mock_response.json.return_value = {"ok": True, "result": "Message sent"}
  mock_post.return_value = mock_response
  
  # Test data
  data = [
    ["Alice", 30, "USA"],
    ["Bob", 25, "Canada"],
    ["Charlie", 35, "UK"]
  ]
  telegram = TelegramNotifier(table_formatter)
  
  response = telegram.update(data)
  
  # Assert
  mock_post.assert_called_once()
  assert response["ok"] is True
  assert "Message sent" in response["result"]

@patch("notifier.telegram.telegram_notifier.requests.post")
def test_telegram_update_failure(mock_post):
  # Mock a failed response from requests.post
  mock_response = MagicMock()
  mock_response.status_code = 400
  mock_response.text = "Bad Request"
  mock_post.return_value = mock_response
  
  # Initialize TelegramNotifier without a formatter
  notifier = TelegramNotifier()
  
  # Act & Assert
  with pytest.raises(Exception, match="Failed to send message: Bad Request"):
    notifier.update("Test Message")
  
  mock_post.assert_called_once()
  
def test_send_table_message_to_telegram(table_formatter):
    # Test data
  data = [
    ["Alice", 30, "USA"],
    ["Bob", 25, "Canada"],
    ["Charlie", 35, "UK"]
  ]
  
  telegram_test = TelegramNotifier(AlertFormatter())
  telegram_test.update({"title": "Bot (test)", "message":"This is from test"})
  
  telegram = TelegramNotifier(formatter=table_formatter)
  response = telegram.update(data)
  
  
  # Assert
  assert response["ok"] is True
  assert "message_id" in response["result"]