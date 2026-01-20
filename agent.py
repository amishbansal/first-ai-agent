from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools import get_weather

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt=(
        "You are a helpful assistant. "
        "Answer general everyday questions directly. "
        "If a question depends on real weather conditions, "
        "use the weather tool to get accurate information "
        "before answering."
    )
)