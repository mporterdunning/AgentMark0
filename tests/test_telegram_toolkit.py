import unittest
from unittest.mock import patch
import sys
import os
from src.utils.utils import error_handler

# Add src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.tools.telegram_toolkit import TelegramToolkit  # Correct import path

class TestTelegramToolkit(unittest.TestCase):
    def setUp(self):
        """Set up a TelegramToolkit instance."""
        self.toolkit = TelegramToolkit()

    @patch("src.telegram_toolkit.requests.post")  # Correct mock path
    def test_send_message_success(self, mock_post):
        """Test that send_message works correctly when API responds successfully."""
        # Mock a successful API response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"ok": True}

        response = self.toolkit.send_telegram_message("Test message")  # Correct method name
        self.assertEqual(response, "Message sent successfully!")

    @patch("src.telegram_toolkit.requests.post")  # Correct mock path
    def test_send_message_failure(self, mock_post):
        """Test that send_message handles API failures correctly."""
        # Mock a failed API response
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {"error": "Invalid request"}

        response = self.toolkit.send_telegram_message("Test message")  # Correct method name
        self.assertIn("Failed to send message", response)

    '''
    def test_notify_trade_opportunity_missing_details(self):
        """Test notify_trade_opportunity with missing details."""
        response = self.toolkit.notify_trade_opportunity(None)
        self.assertEqual(response, "Opportunity details are missing.") '''

    @patch("src.telegram_toolkit.TelegramToolkit.send_telegram_message")  # Correct mock path
    def test_notify_trade_opportunity_success(self, mock_send_message):
        """Test notify_trade_opportunity sends the correct message."""
        mock_send_message.return_value = "Message sent successfully!"

        opportunity_details = {
            "symbol": "TSLA",
            "signal": "Buy",
            "entry_price": 700.00,
            "target_price": 750.00,
            "risk_level": "Moderate"
        }
        response = self.toolkit.notify_trade_opportunity(opportunity_details)
        self.assertEqual(response, "Message sent successfully!")
        mock_send_message.assert_called_once_with(
            "*TRADE OPPORTUNITY*\n"
            "Stock: TSLA\n"
            "Signal: Buy\n"
            "Entry Price: $700.00\n"
            "Target Price: $750.00\n"
            "Risk Level: Moderate\n"
        )

if __name__ == "__main__":
    unittest.main()