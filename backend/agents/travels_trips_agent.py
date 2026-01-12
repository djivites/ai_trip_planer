from crewai import Agent
from tools.web_tools import serper_tool
from tools.scrape_tools import scrape_tool

def create_travel_tips_agent(llm):
    return Agent(
        role="Travel Tips Expert",
        goal="Provide practical travel tips and common mistakes to avoid.",
        backstory=(
            "You are an experienced traveler who gathers practical advice "
            "from blogs, forums, and travel websites."
        ),
        tools=[serper_tool, scrape_tool],
        llm=llm,
        max_retry_limit=1,
        
        verbose=False
    )
