import streamlit as st
import time
from dotenv import load_dotenv
from litellm.exceptions import RateLimitError
from crewai import Crew, LLM

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- STREAMLIT CONFIG ----------------
st.set_page_config(
    page_title="AI Trip Planner (CrewAI)",
    layout="wide"
)

st.title("🌍 AI Trip Planner using CrewAI")
st.write("Plan a complete trip using a team of AI agents.")

# ---------------- SAFE CREW RUNNER ----------------
def run_crew_safely(crew, retries=2, wait=20):
    last_error = None
    for attempt in range(retries + 1):
        try:
            result = crew.kickoff()
            if result and hasattr(result, "tasks_output"):
                return result
            raise ValueError("Empty LLM response")
        except (ValueError, RateLimitError) as e:
            last_error = e
            if attempt < retries:
                st.warning(f"⚠️ LLM issue. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                break
    return f"❌ Trip plan could not be generated.\n\nError: {last_error}"

# ---------------- CLEAN RAW OUTPUT ----------------
def extract_final_answer(raw: str) -> str:
    if "Final Answer:" in raw:
        return raw.split("Final Answer:", 1)[1].strip()

    cleaned = []
    for line in raw.splitlines():
        if line.startswith(("Thought:", "Action:", "Observation:", "System:")):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()

# ---------------- FORMAT OUTPUT ----------------
def format_full_trip_output(result):
    if not hasattr(result, "tasks_output"):
        return str(result)

    sections = []
    for task in result.tasks_output:
        content = None

        if task.pydantic:
            content = str(task.pydantic)
        elif task.json_dict:
            content = str(task.json_dict)
        elif task.raw:
            content = extract_final_answer(task.raw)

        if content:
            sections.append(
                f"## 🧠 {task.agent}\n\n{content}"
            )

    return "\n\n---\n\n".join(sections)

# ---------------- USER INPUT ----------------
destination_pref = st.text_input(
    "📍 Where do you want to travel?",
    placeholder="e.g., Paris, Japan, Italy"
)

user_location = st.text_input(
    "🧳 Where are you traveling from?",
    placeholder="e.g., India, Chennai, USA"
)

days = st.number_input(
    "📅 Number of days",
    min_value=1,
    max_value=30,
    value=5
)

budget_range = st.selectbox(
    "💰 Budget range",
    ["Low", "Medium", "High"]
)

travel_style = st.selectbox(
    "🧭 Travel style",
    ["Relaxed", "Balanced", "Adventure"]
)

# ---------------- LLM CONFIG ----------------
llm = LLM(
    model="ollama/llama3",
    provider="litellm",
    temperature=0.2,
    max_tokens=600,
)

# ---------------- IMPORT AGENTS ----------------
from agents.destination_agent import create_destination_agent
from agents.attraction_agent import create_attraction_agent
from agents.budget_agent import create_budget_agent
from agents.travels_trips_agent import create_travel_tips_agent
from agents.itinerary_agent import create_itinerary_agent
from agents.summary_agent import create_summary_agent

# ---------------- IMPORT TASKS ----------------
from task.destination_task import create_destination_task
from task.attraction_task import create_attraction_task
from task.budget_task import create_budget_task
from task.travels_tips_task import create_travel_tips_task
from task.itinerary_ask import create_itinerary_task
from task.summary_task import create_summary_task

# ---------------- RUN BUTTON ----------------
if st.button("🚀 Plan My Trip"):

    if not destination_pref or not user_location:
        st.warning("Please enter both destination and starting location.")
        st.stop()

    # -------- AGENTS --------
    destination_agent = create_destination_agent(llm)
    attraction_agent = create_attraction_agent(llm)
    budget_agent = create_budget_agent(llm)
    tips_agent = create_travel_tips_agent(llm)
    itinerary_agent = create_itinerary_agent(llm)
    summary_agent = create_summary_agent(llm)

    # -------- TASKS --------
    user_preferences = f"""
    Destination: {destination_pref}
    Starting location: {user_location}
    Travel style: {travel_style}
    Budget: {budget_range}
    Trip duration: {days} days
    """

    task1 = create_destination_task(destination_agent, destination_pref, user_preferences)
    task2 = create_attraction_task(attraction_agent, destination_pref)
    task3 = create_budget_task(
        budget_agent,
        destination_pref,
        budget_range,
        user_location
    )
    task4 = create_travel_tips_task(tips_agent, destination_pref)
    task5 = create_itinerary_task(
        itinerary_agent,
        destination_pref,
        days
    )
    task6 = create_summary_task(summary_agent, destination_pref)

    # -------- CREW --------
    crew = Crew(
        agents=[
            destination_agent,
            attraction_agent,
            budget_agent,
            tips_agent,
            itinerary_agent,
            summary_agent
        ],
        tasks=[
            task1,
            task2,
            task3,
            task4,
            task5,
            task6
        ],
        process="sequential",
        verbose=False
    )

    # -------- EXECUTION --------
    with st.spinner("🧠 AI agents are planning your trip..."):
        result = run_crew_safely(crew)

    # -------- OUTPUT --------
    st.success("✅ Trip plan generated!")
    st.markdown("## ✈️ Your Trip Plan")

    st.markdown(format_full_trip_output(result))
