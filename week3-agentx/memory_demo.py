from dotenv import load_dotenv
from langchain_groq import ChatGroq

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

memory = MemorySaver()

agent = create_react_agent(
    llm,
    tools=[],
    checkpointer=memory
)

agent.invoke(
    {
        "messages": [
            ("user", "My name is Lakshya")
        ]
    },
    config={
        "configurable": {
            "thread_id": "chat1"
        }
    }
)
response = agent.invoke(
    {
        "messages": [
             ("user", "Tell me everything you know about me")
        ]
    },
    config={
        "configurable": {
            "thread_id": "chat1"
        }
    }
)

print(
    response["messages"][-1].content
)
