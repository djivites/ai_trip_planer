from dotenv import load_dotenv
import os
import sys

# Ensure root is in path
sys.path.append(os.getcwd())

from crewai import Crew, LLM

# Try importing from backend package
try:
    from backend.agents.destination_agent import create_destination_agent
    from backend.task.destination_task import create_destination_task
    print("Imports successful from backend package.")
except ImportError as e:
    print(f"Import failed: {e}")
    # Try direct path manipulation if package import fails
    sys.path.append(os.path.join(os.getcwd(), 'backend'))
    from agents.destination_agent import create_destination_agent
    from task.destination_task import create_destination_task
    print("Imports successful via sys.path hack.")

load_dotenv()

def run_test():
    print("Initializing LLM...")
    llm = LLM(
        model="ollama/llama3",
        provider="litellm",
        api_base="http://localhost:11434",
        temperature=0.2,
        max_tokens=600,
    )

    print("Creating Agent...")
    destination_agent = create_destination_agent(llm)

    print("Creating Task...")
    dest = "London"
    user_preferences = "Destination: London\nBudget: High"

    task1 = create_destination_task(destination_agent, dest, user_preferences)
    
    crew = Crew(
        agents=[destination_agent],
        tasks=[task1],
        process="sequential",
        verbose=True
    )

    print("Kicking off Crew...")
    result = crew.kickoff()
    print("Success! Result:", result)

if __name__ == "__main__":
    try:
        run_test()
    except Exception as e:
        print("\nCRITICAL ERROR CAPTURED:")
        print(e)
