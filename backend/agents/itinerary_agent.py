from crewai import Agent

def create_itinerary_agent(llm):
    return Agent(
        role="Itinerary Planner",
        goal="Create a balanced day-by-day travel itinerary.",
        backstory=(
            "You are a professional itinerary planner who organizes trips "
            "to balance sightseeing, rest, and travel time."
        ),
        tools=[],  # NO tools
        llm=llm,
        max_retry_limit=1,
        verbose=False
    )
