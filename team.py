from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

eng_agent = Agent(
    name="English Agent",
    role="You answer questions in English"
)

chi_agent = Agent(
    name="Chinese Agent",
    role="You answer questions in Chinese"
)

hindi_agent = Agent(
    name="Hindi Agent",
    role="You answer questions in Hindi"
)

team_leader = Team(
    name="Answer & Translation Team",
    members=[
        eng_agent,
        chi_agent,
        hindi_agent
    ],
    model=Groq(id="openai/gpt-oss-120b"),
    markdown=True,
    show_members_responses=True,
    instructions="""
    All member agents must answer the query in their specific language.
    Do not route to just one agent.
    Return responses from all agents.
    """
)

team_leader.print_response(
    "what is capital of india"
)