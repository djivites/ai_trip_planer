from crewai import Task

def create_travel_tips_task(agent, destination: str):
    return Task(
        description=f"""
        Destination: {destination}

        Your task:
        - Search the web for travel tips and common mistakes.
        - Prioritize reputable travel blogs and video descriptions.
        - Extract practical advice only.
        - Limit output to 5 bullet points.
        IMPORTANT OUTPUT RULES:
- Do NOT include "Thought", "Action", or reasoning
- Do NOT explain your role
- Output ONLY the final answer
- Do NOT mention websites or tools


        """,
        agent=agent,
        expected_output="""
        A list of 5 practical travel tips also provide the source url.
        """
    )
