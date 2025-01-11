from phi.agent import Agent
from phi.model.groq import Groq
from src.tools.telegram_toolkit import TelegramToolkit

telegram_toolkit = TelegramToolkit()

def create_execution_agent():
    return Agent(
        name="Execution Agent",
        model=Groq(id='llama-3.3-70b-versatile'),
        tools=[telegram_toolkit],
        description="An agent responsible for orchestrating trades based on team decisions.",
        instructions=[
            "Receive trade opportunities from analysis agents with detailed information.",
            "Ensure the message includes the triggered indicators, stop loss, leverage, and risk level.",
            "Send this trade opportunity as a formatted Telegram notification."
        ],
        show_tool_calls=True,
        markdown=True
    )