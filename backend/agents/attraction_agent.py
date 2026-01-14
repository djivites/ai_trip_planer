from crewai import Agent
from tools.web_tools import serper_tool
from tools.scrape_tools import scrape_tool

def create_attraction_agent(llm):
    return Agent(
        role="Attraction Planner",
        goal="Find major attractions and activities for a destination.",
        backstory=(
            "You are an expert travel guide who knows the most popular attractions "
            "and activities in major tourist destinations."
            "You do NOT include thoughts, actions, or tools."

        ),
        tools=[serper_tool, scrape_tool],
        
        llm=llm,
        max_retry_limit=1,
        verbose=False
    )
