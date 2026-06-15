from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

agent = create_react_agent(
    llm,
    tools=[]
)

print("\nAgent Ready\n")
response = ""

for chunk in agent.stream(
    {
        "messages": [
            ("user", "Explain AI agents")
        ]
    },
    stream_mode="values"
):

    message = chunk["messages"][-1]

    if hasattr(message, "content"):
        print(
           "\n----\n"
        )
        print(message.content)