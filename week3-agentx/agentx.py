import os
import sys
import datetime

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langgraph.errors import GraphRecursionError

# ── KEY ────────────────────────────────────────
os.environ["GROQ_API_KEY"] = "real_api_key"

# ── MODEL (upgraded to 70b — more reliable) ────
llm = ChatGroq(
   model="llama-3.1-8b-instant",
    temperature=0,
    max_retries=2,
)

# ── TOOLS ──────────────────────────────────────
@tool
def get_current_date(dummy: str = "") -> str:
    """Returns today's date. Use this for any question about today's date or current date."""
    return f"Today's date is {datetime.date.today().isoformat()}"

@tool
def web_search(query: str) -> str:
    """Search the web for current information."""
    try:
        result = DuckDuckGoSearchRun().run(query)
        return result if result else "No results found."
    except Exception as e:
        return f"Search failed: {e}"

@tool
def wiki_search(query: str) -> str:
    """Search Wikipedia for factual information."""
    try:
        result = WikipediaQueryRun(
            api_wrapper=WikipediaAPIWrapper(top_k_results=1)
        ).run(query)
        return result if result else "No Wikipedia results."
    except Exception as e:
        return f"Wikipedia search failed: {e}"

tools = [get_current_date, web_search, wiki_search]

# ── SYSTEM PROMPT ──────────────────────────────
system_prompt = SystemMessage(content="""You are AgentX, a helpful assistant.
Rules:
- For date/time questions: call get_current_date ONCE, then answer.
- For factual questions: use wiki_search ONCE, then answer.
- For current news/events: use web_search ONCE, then answer.
- After calling a tool and getting its result, give the final answer immediately.
- Do NOT call the same tool twice.
""")

# ── AGENT ──────────────────────────────────────
memory = MemorySaver()
agent = create_react_agent(
    llm,
    tools=tools,
    checkpointer=memory,
    prompt=system_prompt,
)

# ── RUN ────────────────────────────────────────
def run_agent(user_input: str, session_id: str):
    config = {
        "configurable": {"thread_id": session_id},
        "recursion_limit": 10,   # stops infinite loops
    }
    answer = ""
    trace = []

    try:
        for event in agent.stream(
            {"messages": [("user", user_input)]},
            config=config,
            stream_mode="values",
        ):
            msg = event["messages"][-1]

            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tc in msg.tool_calls:
                    trace.append(f"Tool → {tc['name']}  args={tc.get('args', {})}")

            elif hasattr(msg, "name") and msg.name:
                trace.append(f"Result ← {msg.name}: {str(msg.content)[:150]}")

            elif hasattr(msg, "content") and msg.content:
                answer = msg.content

    except GraphRecursionError:
        answer = "Agent got stuck in a loop. Please try rephrasing your question."
    except Exception as e:
        answer = f"Error: {e}"

    return answer, trace

# ── CLI ────────────────────────────────────────
print("\n===== AgentX Ready =====\n")
session = "session_001"

while True:
    try:
        query = input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nAgentX Closed")
        break

    if not query:
        continue
    if query.lower() in ("exit", "quit"):
        print("\nAgentX Closed")
        break

    print("\nThinking...\n")
    sys.stdout.flush()

    answer, trace = run_agent(query, session)

    print("TRACE:")
    if trace:
        for t in trace:
            print(" ", t)
    else:
        print("  No tools called")

    print("\nANSWER:")
    print(answer)
    print("\n" + "-" * 40 + "\n")
    sys.stdout.flush()