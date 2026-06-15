from typing import TypedDict

from langgraph.graph import StateGraph

from groq import Groq
from dotenv import load_dotenv

import os

# =====================
# Load API Key
# =====================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =====================
# State
# Data travelling through graph
# =====================

class State(TypedDict):
    question: str
    route: str
    answer: str


# =====================
# Router Node
# Decides joke or math
# =====================

def router(state):

    query = state["question"]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": f"""
Classify this query.

Return ONLY one word:

joke
math

Query:
{query}
"""
            }
        ]
    )

    route = (
        response
        .choices[0]
        .message
        .content
        .strip()
        .lower()
    )

    return {
        "route": route
    }


# =====================
# Joke Node
# Uses original question
# =====================

def joke_node(state):

    question = state["question"]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return {
        "answer":
        response.choices[0].message.content
    }


# =====================
# Math Node
# Uses original question
# =====================

def math_node(state):

    question = state["question"]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return {
        "answer":
        response.choices[0].message.content
    }


# =====================
# Routing Function
# Reads route field
# =====================

def decide_route(state):

    return state["route"]


# =====================
# Build Graph
# =====================

builder = StateGraph(State)

builder.add_node(
    "router",
    router
)

builder.add_node(
    "joke",
    joke_node
)

builder.add_node(
    "math",
    math_node
)

builder.set_entry_point(
    "router"
)

builder.add_conditional_edges(
    "router",
    decide_route,
    {
        "joke": "joke",
        "math": "math"
    }
)

builder.set_finish_point("joke")
builder.set_finish_point("math")

graph = builder.compile()

# =====================
# Run
# =====================

result = graph.invoke(
    {
        "question": "2345*21",
        "route": "",
        "answer": ""
    }
)

print(result)