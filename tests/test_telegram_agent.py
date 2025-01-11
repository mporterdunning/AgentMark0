import unittest
from unittest.mock import patch
from phi.agent import Agent
from phi.model.groq import Groq
from src.tools.telegram_toolkit import TelegramToolkit

class TestTelegramAgentIntegration(unittest.TestCase):
    def setUp(self):
        """Set up the TelegramToolkit and Agent instance."""
        self.toolkit = TelegramToolkit()
        self.agent = Agent(
            model=Groq(id='llama-3.3-70b-versatile'),
            tools=[self.toolkit],
            description="Test agent for Telegram notifications.",
            instructions=[
                "Use TelegramToolkit to send trade opportunity notifications."
            ]
        )

    @patch("src.telegram_toolkit.TelegramToolkit.send_telegram_message")
    def test_agent_notify_trade_opportunity(self, mock_send_message):
        """Test that the agent correctly calls the Telegram toolkit."""
        mock_send_message.return_value = "Message sent successfully!"

        opportunity_details = {
            "symbol": "TSLA",
            "signal": "Buy",
            "entry_price": 700.00,
            "target_price": 750.00,
            "risk_level": "Moderate"
        }
        input_prompt = {
            "message": (
                f"*TRADE OPPORTUNITY*\n"
                f"Stock: {opportunity_details['symbol']}\n"
                f"Signal: {opportunity_details['signal']}\n"
                f"Entry Price: ${opportunity_details['entry_price']:.2f}\n"
                f"Target Price: ${opportunity_details['target_price']:.2f}\n"
                f"Risk Level: {opportunity_details['risk_level']}\n"
            )
        }

        response = self.agent.print_response(input_prompt)
        self.assertIn("Message sent successfully!", response)
        mock_send_message.assert_called_once_with(input_prompt["message"])

if __name__ == "__main__":
    unittest.main()
