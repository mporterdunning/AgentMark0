from phi.agent import Agent
from phi.model.groq import Groq

def create_risk_management_agent():
    return Agent(
        name="Risk Management Agent",
        model=Groq(id='llama-3.3-70b-versatile'),
        description="An agent that monitors and manages risk for the portfolio.",
        instructions=[
            "Evaluate current portfolio positions and calculate overall risk exposure.",
            "Recommend adjustments to rebalance the portfolio and mitigate risk.",
            "Ensure that risk parameters (e.g., maximum drawdown) are not violated.",
            "Store risk management recommendations in shared memory."
        ],
        show_tool_calls=True,
        markdown=True
    )