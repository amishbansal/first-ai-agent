from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools import get_weather

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.6
)

agent = create_agent(
    model = model,
    tools=[get_weather],
    system_prompt=(
        "You are a weather-aware assistant.\n"
        "STRICT RULES:\n"
        "1. If the user asks ANY question about weather, rain, temperature, umbrella, or forecast, "
        "you MUST call the get_weather tool.\n"
        "2. You are NOT allowed to answer weather questions from general knowledge.\n"
        "3. If the city is NOT mentioned, ask the user to provide the city.\n"
        "4. For non-weather questions (like greetings or general knowledge), answer directly."
        "5. When prompt is related to weather, dont give it by yourself, get the data from get_weather tool and then reply accordingly"
    )
)