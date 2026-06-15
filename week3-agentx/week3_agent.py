from langchain_core.tools import tool

@tool
def calculator(expression: str):
    """
    Evaluate mathematical expressions.
    """
    return str(eval(expression))

@tool
def tell_joke(topic: str):
    """
    Tell a joke about a topic.
    """
    return f"😂 Joke about {topic}: Why did the {topic} cross the road? To get to the other side!"

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)
from langgraph.prebuilt import create_react_agent
tools = [
    calculator,
    tell_joke
]

agent = create_react_agent(
    llm,
    tools
)
response = agent.invoke(
    {
        "messages": [
            (
                "user",
                "Tell me a joke about programmers."
            )
        ]
    }
)
print(response["messages"][-1].content)
