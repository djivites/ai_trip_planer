from crewai import Agent
from tools.web_tools import serper_tool

def create_destination_agent(llm):
    return Agent(
        role="Destination Researcher",
        goal="Identify suitable travel destinations based on user preferences.",
        backstory=(
            "You are a professional travel researcher who specializes in identifying "
            "destinations based on season, popularity, and traveler preferences."
        ),
        tools=[serper_tool],   # ✅ tool attached here
        llm=llm,
       
        max_retry_limit=1,
        verbose=False
    )
