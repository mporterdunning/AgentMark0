from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.crawl4ai_tools import Crawl4aiTools

def create_data_collection_agent():
    return Agent(
        name="Data Collection Agent",
        model=Groq(id='llama-3.3-70b-versatile'),
        tools=[
            YFinanceTools(),
            DuckDuckGo(search=True),
            Crawl4aiTools(max_length=5000)
        ],
        description="An agent that collects and prepares market, crypto, ETF, and stock data for analysis.",
        instructions=[
            "Fetch live and historical data for stocks, ETFs, and cryptocurrencies.",
            "Analyze trends and calculate technical indicators such as MACD, RSI, and Bollinger Bands.",
            "Retrieve market sentiment or breaking news related to financial markets.",
        ],
        show_tool_calls=True,
        markdown=True
    )