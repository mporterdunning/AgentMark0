from phi.agent import Agent
from phi.model.groq import Groq

def create_technical_analysis_agent(knowledge_base):
    return Agent(
        name="Technical Analysis Agent",
        model=Groq(id='llama-3.3-70b-versatile'),
        knowledge=knowledge_base,
        search_knowledge=True,
        description="An agent that performs technical analysis to identify trading signals.",
        instructions=[
            "Use the shared knowledge base or memory to retrieve collected market data.",
            "Analyze trends, patterns, and indicators such as RSI, MACD, Volume, and Bollinger Bands.",
            "Identify potential buy or sell opportunities based on calculated indicators.",
            "Generate trade opportunities with entry price, target price, stop loss, and leverage.",
            "Store identified trading opportunities in shared memory for execution."
        ],
        show_tool_calls=True,
        markdown=True
    )