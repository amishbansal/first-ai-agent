from agent import model
from tools import get_weather
from langchain.messages import HumanMessage, AIMessage, SystemMessage

response = model.invoke([HumanMessage(content="Why is current weather in chandigarh?")])
print(response.content)