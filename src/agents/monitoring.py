from phi.agent import Agent
from phi.model.groq import Groq
from src.tools.telegram_toolkit import TelegramToolkit

telegram_toolkit = TelegramToolkit()

def create_performance_monitoring_agent():
    return Agent(
        name="Performance Monitoring Agent",
        model=Groq(id='llama-3.3-70b-versatile'),
        tools=[telegram_toolkit],
        description="An agent that tracks and evaluates the performance of trading strategies.",
        instructions=[
            "Analyze the historical performance of executed trades.",
            "Identify strengths and weaknesses in trading strategies.",
            "Provide actionable recommendations for strategy refinement.",
            "Send performance updates via Telegram."
        ],
        show_tool_calls=True,
        markdown=True
    )