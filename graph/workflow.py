from langgraph.graph import StateGraph
from memory.state import AgentState

# Create a new graph
workflow = StateGraph(AgentState)

print("LangGraph workflow created successfully!")