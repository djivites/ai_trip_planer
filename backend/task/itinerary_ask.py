from crewai import Task
def create_itinerary_task(agent, destination: str, days: int,style: str):
    return Task(
        description=f"""
        Destination: {destination}
        Trip duration: {days} days
        Travel style: {style}

        CONTEXT:
        - Attractions are already decided.
        - Do NOT add new places.

        TASK:
        - Create a COMPLETE itinerary based on the travel style.
        - Morning / Afternoon / Evening for EACH day.
        - Use at most 2 attractions per day.
        - Finish ALL {days} days.

        STRICT RULES:
        - DO NOT write thoughts.
        - DO NOT explain anything.
        - DO NOT stop early.
        - You MUST return the full itinerary.

        OUTPUT FORMAT (MANDATORY):

        Day 1:
        Morning:
        Afternoon:
        Evening:

        Day 2:
        Morning:
        Afternoon:
        Evening:
        IMPORTANT OUTPUT RULES:
- Do NOT include "Thought", "Action", or reasoning
- Do NOT explain your role
- Output ONLY the final answer
- Do NOT mention websites or tools


        """,
        agent=agent,
        expected_output="A complete day-wise itinerary for all days."
    )

