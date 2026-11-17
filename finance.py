from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()
# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------
def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[YFinanceTools(), DuckDuckGoTools()],
        markdown=True,
        add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use given tools whenever possible. Format your response using markdown and use tables to display data where possible."],
        debug_mode=True
    )

agent = build_agent()
agent.print_response("share the MSFT stock price and analyst recommendationss")