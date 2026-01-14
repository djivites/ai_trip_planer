Here’s a **clean, professional README.md** you can directly use for your project.
I’ve written it like a **final-year / hackathon / GitHub-ready** README and clearly mentioned the **multi-LLM architecture** (Gemini, Groq, Ollama) 👇

---

# 🌍 AI Trip Planner (Multi-Agent + Multi-LLM)

An intelligent **AI-powered Trip Planning system** built using **CrewAI** and **FastAPI**, where multiple specialized AI agents collaborate to generate a **complete, realistic travel plan** including destination analysis, attractions, budget estimation, itinerary, travel tips, and a final summary.

This project uniquely combines **multiple LLM providers** to optimize **speed, cost, reasoning quality, and reliability**.

---

## 🚀 Key Features

* 🧠 **Multi-Agent Architecture** (CrewAI)
* 🤖 **Multi-LLM Strategy** (Gemini + Groq + Ollama)
* 🗺️ Destination suitability analysis
* 📍 Attraction planning
* 💰 Realistic budget estimation
* 📅 Day-wise itinerary generation
* 💡 Practical travel tips
* 🧾 Clean final trip summary
* ⚡ FastAPI backend (API-ready)
* 🌐 Frontend-ready 

---

## 🧠 AI Agents Overview

| Agent                  | Responsibility                                        |
| ---------------------- | ----------------------------------------------------- |
| Destination Researcher | Evaluates if the destination matches user preferences |
| Attraction Planner     | Lists must-visit attractions and activities           |
| Budget Planner         | Provides realistic daily cost breakdown               |
| Travel Tips Expert     | Shares practical travel advice & mistakes             |
| Itinerary Planner      | Creates a balanced day-wise itinerary                 |
| Trip Summary Generator | Combines all outputs into a clean summary             |

---

## 🤖 Multi-LLM Architecture (IMPORTANT)

To avoid **rate limits**, **slow responses**, and **token exhaustion**, different agents use **different LLMs**:

| Agent                  | LLM Used             | Reason                      |
| ---------------------- | -------------------- | --------------------------- |
| Destination Researcher | **Ollama (LLaMA 3)** | Local, cost-free, stable    |
| Attraction Planner     | **Ollama (LLaMA 3)** | Lists & factual content     |
| Budget Planner         | **Ollama (LLaMA 3)** | Numerical reasoning         |
| Travel Tips Expert     | **Ollama (LLaMA 3)** | Extraction-focused          |
| Itinerary Planner      | **Gemini 2.5 Flash** | Strong reasoning & planning |
| Trip Summary Generator | **Groq (LLaMA 3.1)** | Fast, concise summarization |

✅ This design **significantly improves performance**
✅ Prevents single-model bottlenecks
✅ Makes the system scalable & production-ready

---

## 🏗️ Tech Stack

* **Python 3.10+**
* **CrewAI**
* **LiteLLM**
* **FastAPI**
* **Ollama (Local LLaMA 3)**
* **Google Gemini API**
* **Groq API**
* **Pydantic**
* **Uvicorn**

---

## 📁 Project Structure

```
ai-trip-planner/
│
├── frontend/
├── backend/
│   ├── agents/
│   │   ├── destination_agent.py
│   │   ├── attraction_agent.py
│   │   ├── budget_agent.py
│   │   ├── travels_trips_agent.py
│   │   ├── itinerary_agent.py
│   │   └── summary_agent.py
│   │
│   ├── task/
│   │   ├── destination_task.py
│   │   ├── attraction_task.py
│   │   ├── budget_task.py
│   │   ├── travels_tips_task.py
│   │   ├── itinerary_ask.py
│   │   └── summary_task.py
│   │
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-trip-planner.git
cd ai-trip-planner
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
pip install "litellm[proxy]"
```

### 4️⃣ Install & Run Ollama

```bash
ollama pull llama3
ollama run llama3
```

---

## 🔑 Environment Variables (`.env`)

```env
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
```

⚠️ **Gemini Free Tier has strict limits**
Use it only for critical agents (as done here).

---

## ▶️ Run the Backend

```bash
uvicorn backend.main:app --reload
```

Health check:

```
GET http://localhost:8000/api/health
```

Trip planning:

```
POST http://localhost:8000/api/plan-trip
```

---
📂 Navigate to Frontend Directory
cd frontend

📦 Install Dependencies

Run this only once:

npm install


This installs all required frontend packages listed in package.json.

▶️ Start the Frontend Server
npm start

🌐 Access the Application

Once started, the app will open automatically or be available at:

http://localhost:3000

## 📥 Sample API Request

```json
{
  "destination": "Japan",
  "start_location": "India",
  "days": 5,
  "budget": "Low",
  "style": "Relaxed"
}
```

---

## 📤 Sample API Response

* Destination analysis
* Attractions list
* Budget breakdown
* Travel tips
* Day-wise itinerary
* Final summarized trip plan

(All clearly separated by agent)

---

## 🧠 Why This Architecture Works

* ❌ Single LLM → slow, rate-limited, unreliable
* ✅ Multi-LLM → fast, scalable, robust
* ✅ Local Ollama → zero cost for heavy tasks
* ✅ Gemini → better itinerary reasoning
* ✅ Groq → lightning-fast summaries

---

## 🎯 Future Improvements

* Frontend UI (React / Streamlit)
* Caching agent outputs
* Agent dependency chaining
* User profile memory
* Currency auto-conversion
* Hotel & flight API integration

---

## 👨‍💻 Author

**Built by:** *Jivites*
**Domain:** AI / Multi-Agent Systems / LLM Orchestration

---

