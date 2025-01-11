from src.tools.telegram_toolkit import TelegramToolkit
from src.agents.data_collection import data_collection_agent

def send_trade_notification(opportunity_details):
    formatted_message = format_telegram_message(opportunity_details)
    result = TelegramToolkit().send_telegram_message(formatted_message)
    print(f"Telegram Notification Result: {result}")

def format_telegram_message(opportunity_details):
    return (
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

def collect_market_data():
    """Job to fetch and collect market data periodically."""
    try:
        print("Running scheduled data collection...")
        response = data_collection_agent.print_response("Fetch data for AAPL, BTC, and SPY.")
        print(f"Data Collection Response: {response}")
    except Exception as e:
        print(f"Error during data collection: {e}")