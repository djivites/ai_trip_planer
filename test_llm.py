from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

try:
    print("Testing connection to Ollama (llama3)...")
    llm = LLM(
        model="ollama/llama3",
        provider="litellm",
        api_base="http://localhost:11434"
    )
    response = llm.call("Hello, are you working?")
    print("Success! Response:", response)
except Exception as e:
    print("FAILED:", e)
