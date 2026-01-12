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
        - Separate costs into:
          Flights (round-trip estimate)
          Accommodation (per night)
          Food (per day)
          Local transport (per day)
        - Provide ranges, NOT exact numbers
        - Do NOT exaggerate
        """,
        agent=agent,
        expected_output="A clean budget breakdown with clear cost ranges."
    )
