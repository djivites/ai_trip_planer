from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crewai import Crew, LLM
from dotenv import load_dotenv

load_dotenv()

# ---------- IMPORT AGENTS & TASKS ----------
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

# ---------- FASTAPI ----------
app = FastAPI(title="AI Trip Planner API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- SCHEMAS ----------
class TripRequest(BaseModel):
    destination: str
    start_location: str
    days: int
    budget: str
    style: str

class AgentOutput(BaseModel):
    agent: str
    content: str

class TripResponse(BaseModel):
    result: list[AgentOutput]

# ---------- HEALTH ----------
@app.get("/api/health")
def health():
    return {"status": "ok"}

# ---------- MAIN ENDPOINT ----------
@app.post("/api/plan-trip", response_model=TripResponse)
def plan_trip(request: TripRequest):
    try:
        
        # GROQ (FAST, SHORT OUTPUT)
        llm_groq = LLM(
            model="groq/llama-3.1-8b-instant",
            temperature=0.2,
            
        )

        # GEMINI (REASONING)
        llm_gemini =  LLM(
    model="gemini/gemini-2.5-flash",
    provider="litellm",
    temperature=0.2,
            # SMALL
)

        # LOCAL LLAMA (LONG THINKING)
        llm_llama = LLM(
            model="ollama/llama3",
            provider="litellm",
            temperature=0.2,
            
        )


        # Agents
        destination_agent = create_destination_agent(llm_llama)
        attraction_agent  = create_attraction_agent(llm_llama)
        budget_agent      = create_budget_agent(llm_llama)
        tips_agent        = create_travel_tips_agent(llm_llama)
        itinerary_agent   = create_itinerary_agent(llm_gemini)
        summary_agent     = create_summary_agent(llm_groq)

        # Tasks
        user_preferences = f"""
Destination: {request.destination}
Starting location: {request.start_location}
Travel style: {request.style}
Budget: {request.budget}
Trip duration: {request.days} days
"""

        tasks = [
            create_destination_task(destination_agent, request.destination, user_preferences),
            create_attraction_task(attraction_agent, request.destination),
            create_budget_task(budget_agent, request.destination, request.budget, request.start_location),
            create_travel_tips_task(tips_agent, request.destination),
            create_itinerary_task(itinerary_agent, request.destination, request.days, request.style),
            create_summary_task(summary_agent, request.destination),
        ]

        crew = Crew(
            agents=[
                destination_agent,
                attraction_agent,
                budget_agent,
                tips_agent,
                itinerary_agent,
                summary_agent
            ],
            tasks=tasks,
            process="sequential",
            verbose=False
        )

        result = crew.kickoff()

      
        formatted = []
        for i, task_output in enumerate(result.tasks_output):
            content = task_output.raw
            if content:
                agent_name = (
                    task_output.agent.role
                    if hasattr(task_output.agent, "role")
                    else f"Agent {i+1}"
                )
                formatted.append({
                    "agent": agent_name,
                    "content": content.strip()
                })



        return TripResponse(result=formatted)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
