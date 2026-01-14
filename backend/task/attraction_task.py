from crewai import Task

def create_attraction_task(agent, destination: str):
    return Task(
        description=f"""
Destination: {destination}

STRICT RULES:
- Output ONLY a list of attractions
- Each attraction must be ONE bullet
- Each bullet must have:
  Attraction name – 1-line description
- NO website descriptions
- NO meta commentary
- NO system text

Example format:
• Attraction – short description

Limit to 6–8 attractions.
IMPORTANT OUTPUT RULES:
- Do NOT include "Thought", "Action", or reasoning
- Do NOT explain your role
- Output ONLY the final answer
- Do NOT mention websites or tools


""",
        agent=agent,
        expected_output="A clean bullet list of attractions with short descriptions."
    )


