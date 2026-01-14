from crewai import Task

def create_summary_task(agent, destination: str):
    return Task(
        description=f"""
Destination: {destination}

Your task:
- Summarize the entire trip plan clearly
- Include:
  1. Why this destination fits the user
  2. Key attractions
  3. Budget overview (daily estimate)
  4. Itinerary overview (5 days)
  5. Travel tips (brief)

STRICT RULES:
- Do NOT say "I can now answer"
- Do NOT add new information
- Write in clear markdown
- Be concise but complete
IMPORTANT OUTPUT RULES:
- Do NOT include "Thought", "Action", or reasoning
- Do NOT explain your role
- Output ONLY the final answer
- Do NOT mention websites or tools


""",
        agent=agent,
        expected_output="A structured final trip summary."
    )


