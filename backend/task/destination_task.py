from crewai import Task

def create_destination_task(agent, destination: str, user_preferences: str):
    return Task(
        description=f"""
        Destination: {destination}

        User preferences:
        {user_preferences}

        Your task:
        - Evaluate whether the GIVEN destination matches the user's preferences.
        - Consider budget, travel style, crowd levels, and trip duration.
        - List 2–3 strengths of this destination.
        - List 1–2 limitations (if any) and how to manage them.

        STRICT RULES:
        - DO NOT suggest other destinations.
        - DO NOT replace or override the destination.
        - The destination provided by the user is FINAL.
        IMPORTANT OUTPUT RULES:
- Do NOT include "Thought", "Action", or reasoning
- Do NOT explain your role
- Output ONLY the final answer
- Do NOT mention websites or tools


        """,
        agent=agent,
        expected_output="""
        A short suitability analysis of the given destination with pros and cons.
        """
    )

