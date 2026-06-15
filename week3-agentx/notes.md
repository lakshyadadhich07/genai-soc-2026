# Week 3: AgentX using LangGraph + Groq

## Objective

The objective of Week 3 was to understand how AI Agents work and build an interactive agent capable of using external tools and maintaining execution flow.

## What I learned

* Basics of AI Agents
* LangGraph workflow and graph execution
* Agent architecture
* Tool calling mechanism
* Memory concepts
* Streaming responses
* Conditional execution
* Using external APIs with Groq
* Debugging tool loops and recursion issues

## Features Implemented

### AgentX

An AI assistant built using LangGraph and Groq.

Capabilities:

* Returns current date using custom tool
* Searches factual information
* Performs web-based lookup
* Handles user interaction in CLI
* Uses memory checkpoints
* Displays internal execution trace
* Prevents infinite recursion
## Screenshots:-
![alt text](<Screenshot 2026-06-14 151009.png>)
![alt text](<Screenshot 2026-06-14 150924.png>)
![alt text](<Screenshot 2026-06-14 151040.png>)
![alt text](<Screenshot 2026-06-14 150908.png>)


## Tech Stack

* Python
* LangGraph
* LangChain
* Groq API
* DuckDuckGo Search
* Wikipedia API
* dotenv

## Challenges Faced

* Tool calling loops
* Rate limits
* Function calling validation errors
* Recursion handling
* Environment configuration issues
* Prompt tuning for correct tool selection

## Outcome

Successfully created AgentX and understood how agent execution, tools, memory, and reasoning pipelines work in practice.

Week 3 completed successfully.
