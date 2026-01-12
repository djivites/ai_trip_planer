from crewai import Agent

def create_summary_agent(llm):
    return Agent(
        role="Trip Summary Generator",
        goal="Generate a clear and user-friendly summary of the trip plan.",
        backstory=(
            "You specialize in presenting complex travel plans in a clean, "
            "easy-to-understand format for travelers."
        ),
        tools=[],  # NO tools
        llm=llm,
        max_retry_limit=1,
        verbose=False
    )
