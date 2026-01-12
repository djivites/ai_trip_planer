from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crewai import Crew, LLM
from dotenv import load_dotenv
import os

# Import agents and tasks
# Assuming running from root as: uvicorn backend.main:app
try:
    from backend.agents.destination_agent import create_destination_agent
    from backend.agents.attraction_agent import create_attraction_agent
    from backend.agents.budget_agent import create_budget_agent
    from backend.agents.travels_trips_agent import create_travel_tips_agent
    from backend.agents.itinerary_agent import create_itinerary_agent
    from backend.agents.summary_agent import create_summary_agent

    from backend.task.destination_task import create_destination_task
    from backend.task.attraction_task import create_attraction_task
    from backend.task.budget_task import create_budget_task
    from backend.task.travels_tips_task import create_travel_tips_task
    from backend.task.itinerary_ask import create_itinerary_task
    from backend.task.summary_task import create_summary_task
except ImportError:
    # Fallback for running directly from backend/
    from agents.destination_agent import create_destination_agent
    from agents.attraction_agent import create_attraction_agent
    from agents.budget_agent import create_budget_agent
    from agents.travels_trips_agent import create_travel_tips_agent
    from agents.itinerary_agent import create_itinerary_agent
    from agents.summary_agent import create_summary_agent

    from task.destination_task import create_destination_task
    from task.attraction_task import create_attraction_task
    from task.budget_task import create_budget_task
    from task.travels_tips_task import create_travel_tips_task
    from task.itinerary_ask import create_itinerary_task
    from task.summary_task import create_summary_task

load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Trip Planner API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TripRequest(BaseModel):
    destination: str
    start_location: str
    days: int
    budget: str
    style: str

class TripResponse(BaseModel):
    result: list[dict[str, str]]

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/plan-trip", response_model=TripResponse)
def plan_trip(request: TripRequest):
    try:
        # LLM Config
        llm = LLM(
    model="ollama/llama3",
    provider="litellm",
    temperature=0.2,
    max_tokens=600,
)

        # Agents
        destination_agent = create_destination_agent(llm)
        attraction_agent = create_attraction_agent(llm)
        budget_agent = create_budget_agent(llm)
        tips_agent = create_travel_tips_agent(llm)
        itinerary_agent = create_itinerary_agent(llm)
        summary_agent = create_summary_agent(llm)

        # Tasks
        user_preferences = f"""
        Destination: {request.destination}
        Starting location: {request.start_location}
        Travel style: {request.style}
        Budget: {request.budget}
        Trip duration: {request.days} days
        """

        task1 = create_destination_task(destination_agent, request.destination, user_preferences)
        task2 = create_attraction_task(attraction_agent, request.destination)
        task3 = create_budget_task(
            budget_agent,
            request.destination,
            request.budget,
            request.start_location
        )
        task4 = create_travel_tips_task(tips_agent, request.destination)
        task5 = create_itinerary_task(
            itinerary_agent,
            request.destination,
            request.days
        )
        task6 = create_summary_task(summary_agent, request.destination)

        # Crew
        crew = Crew(
            agents=[
                destination_agent,
                attraction_agent,
                budget_agent,
                tips_agent,
                itinerary_agent,
                summary_agent
            ],
            tasks=[task1, task2, task3, task4, task5, task6],
            process="sequential",
            verbose=True
        )

        result = crew.kickoff()
        
        # Format output
        formatted_results = []
        if hasattr(result, "tasks_output"):
             for task in result.tasks_output:
                 content = str(task.raw)
                 if content:
                     formatted_results.append({
                         "agent": str(task.agent),
                         "content": content
                     })
        else:
            formatted_results.append({"agent": "Result", "content": str(result)})

        return TripResponse(result=formatted_results)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
