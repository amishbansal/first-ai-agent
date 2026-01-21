from agent import agent
from agent import model
from tools import get_weather
from langchain.messages import HumanMessage, AIMessage, SystemMessage
messages = [
    SystemMessage(content="You are helpful assistant which solves weather related queries"),
    HumanMessage(content="Tell about agentic ai")
]

response = agent.invoke({
    "messages": messages
})
print(response)