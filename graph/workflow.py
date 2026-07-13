from langgraph.graph import StateGraph, START, END
from memory.state import AgentState
from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.coder import coding_agent
from agents.reviewer import reviewer_agent
from agents.reporter import reporter_agent

# Create the graph
workflow = StateGraph(AgentState)

# Add Planner node
workflow.add_node("planner", planner_agent)

# Add Research node
workflow.add_node("research", research_agent)

# Add Coding node
workflow.add_node("coder", coding_agent)
# Add Reviewer node
workflow.add_node("reviewer", reviewer_agent)

# Add Reporter node
workflow.add_node("reporter", reporter_agent)

workflow.add_edge(START, "planner")
workflow.add_edge("planner", "research")
workflow.add_edge("research", "coder")
workflow.add_edge("coder", "reviewer")
workflow.add_edge("reviewer", "reporter")
workflow.add_edge("reporter", END)

# Compile the graph
graph = workflow.compile()

print("LangGraph workflow created successfully!")

# Test the graph
state = {
    "user_request": "Build a portfolio website",
    "plan": "",
    "research": "",
    "code": "",
    "review": "",
    "report": ""
}

result = graph.invoke(state)

print("\n===== Planner Output =====")
print(result["plan"])

print("\n===== Research Output =====")
print(result["research"])

print("\n===== Coding Output =====")
print(result["code"])

print("\n===== Reviewer Output =====")
print(result["review"])

print("\n===== Final Report =====")
print(result["report"])