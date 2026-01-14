from crewai import Task

def create_budget_task(agent, destination: str, budget_range: str, user_location: str):
    return Task(
        description=f"""
        Destination: {destination}
        Traveler origin: {user_location}
        Budget preference: {budget_range}

        STRICT RULES:
        - Use ONLY ONE currency according to the user location.
        - Provide a clear budget breakdown for a trip to {destination}.
        - make sure the budget aligns with the user's budget preference {budget_range}.
        - Separate costs into:
          Flights (round-trip estimate)
          Accommodation (per night)
          Food (per day)
          Local transport (per day)
        - Provide ranges, NOT exact numbers
        - Do NOT exaggerate
        -Do not ask question to user
        -Destination: {destination}
        -Traveler origin: {user_location}
        -Budget preference: {budget_range}
IMPORTANT OUTPUT RULES:
- Do NOT include "Thought", "Action", or reasoning
- Do NOT explain your role
- Output ONLY the final answer
- Do NOT mention websites or tools


        """,
        agent=agent,
        expected_output="A clean budget breakdown with clear cost ranges."
    )
