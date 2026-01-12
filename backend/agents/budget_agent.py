from crewai import Agent
from tools.web_tools import serper_tool
from tools.scrape_tools import scrape_tool

def create_budget_agent(llm):
    return Agent(
        role="Budget Planner",
        goal="Estimate realistic travel costs based on web data.",
        backstory=(
            "You are a travel budget analyst who estimates realistic daily costs "
            "for accommodation, food, and local transportation."
        ),
        tools=[serper_tool, scrape_tool],
       
        llm=llm,
        max_retry_limit=1,
        verbose=False
    )
