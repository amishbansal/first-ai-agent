from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


@tool
def get_weather(city: str) -> str:
    """
    Fetch current weather information for a city.
    Returns temperature, weather condition, and rain status.
    """
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return "Unable to fetch weather data for this city."

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"].lower()

    is_raining = "rain" in description or "drizzle" in description

    return (
        f"City: {city}\n"
        f"Temperature: {temperature}°C\n"
        f"Condition: {description}\n"
        f"Raining: {'Yes' if is_raining else 'No'}"
    )
