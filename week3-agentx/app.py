from typing import TypedDict
from langgraph.graph import StateGraph


# =====================================
# State
# Data travelling through graph
# =====================================

class State(TypedDict):
    message: str


# =====================================
# Router Function
# Decides where to go next
# =====================================

def router(state):

    if "joke" in state["message"].lower():
        return "joke"

    return "math"


# =====================================
# Joke Node
# =====================================

def joke_node(state):

    return {
        "message": (
            "Why did the programmer quit his job? "
            "Because he didn't get arrays."
        )
    }


# =====================================
# Math Node
# =====================================

def math_node(state):

    return {
        "message": "4"
    }


# =====================================
# Create Empty Graph
# =====================================

builder = StateGraph(State)


# =====================================
# Add Nodes
# =====================================

builder.add_node(
    "joke",
    joke_node
)

builder.add_node(
    "math",
    math_node
)


# =====================================
# Router Node
# Just passes state forward
# =====================================

builder.add_node(
    "router",
    lambda state: state
)


# =====================================
# Start Graph From Router
# =====================================

builder.set_entry_point("router")


# =====================================
# Conditional Routing
#
# router() returns:
# "joke" -> Joke Node
# "math" -> Math Node
# =====================================

builder.add_conditional_edges(
    "router",
    router,
    {
        "joke": "joke",
        "math": "math"
    }
)


# =====================================
# End Points
# Graph can finish at either node
# =====================================

builder.set_finish_point("joke")
builder.set_finish_point("math")


# =====================================
# Compile Graph
# Blueprint -> Runnable Graph
# =====================================

graph = builder.compile()


# =====================================
# Test 1
# =====================================

result = graph.invoke(
    {
        "message": "tell joke"
    }
)

print(result)


# =====================================
# Test 2
# =====================================

result = graph.invoke(
    {
        "message": "2+2"
    }
)

print(result)