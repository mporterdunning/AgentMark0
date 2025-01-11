from phi.tools import Toolkit
import os
import requests
from dotenv import load_dotenv
from src.utils.utils import error_handler
import logging

class TelegramToolkit(Toolkit):
    def __init__(self):
            load_dotenv()
            self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
            self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
            if not self.bot_token or not self.chat_id:
                raise EnvironmentError("Telegram bot token or chat ID not set in .env")
            super().__init__(name="telegram_toolkit")
            self.register(self.send_telegram_message)

    @error_handler
    def send_telegram_message(self, message):
        """Send a message via Telegram."""
        if not self.bot_token or not self.chat_id:
            return "Telegram bot token or chat ID not set in .env"

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown"  # Optional: Use Markdown formatting
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return "Message sent successfully!"
        except requests.exceptions.RequestException as e:
            return f"Failed to send message: {str(e)}"
        
    @error_handler
    def notify_trade_opportunity(self, opportunity_details):
        if not opportunity_details:
            return "Opportunity details are missing."

        message = (
            f"*TRADE OPPORTUNITY*\n"
            f"Stock: {opportunity_details.get('symbol', 'N/A')}\n"
            f"Signal: {opportunity_details.get('signal', 'N/A')}\n"
            f"Entry Price: ${opportunity_details.get('entry_price', 0):.2f}\n"
            f"Target Price: ${opportunity_details.get('target_price', 0):.2f}\n"
            f"Stop Loss: ${opportunity_details.get('stop_loss', 0):.2f}\n"
            f"Leverage: {opportunity_details.get('leverage', 'N/A')}x\n"
            f"Triggered Indicators: {', '.join(opportunity_details.get('indicators', []))}\n"
            f"Risk Level: {opportunity_details.get('risk_level', 'Unknown')}\n"
        )
        result = self.send_telegram_message(message)
        if "Failed" in result:
            logging.error(f"Failed to notify trade opportunity: {result}")
        return result
