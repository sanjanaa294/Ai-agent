from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.coder import coding_agent
from agents.reviewer import reviewer_agent
from agents.reporter import reporter_agent
from memory.state import AgentState


# Get input from user
user_request = input("Enter your task: ")
state = AgentState(user_request)

# Run Planner Agent
state = planner_agent(state)

print("\n===== Planner Output =====")
print(state.plan)

# Run Research Agent
state = research_agent(state)

print("\n===== Research Output =====")
print(state.research)
# Run Coding Agent
state = coding_agent(state)

print("\n===== Coding Output =====")
print(state.code)

# Run Reviewer Agent
state = reviewer_agent(state)

print("\n===== Reviewer Output =====")
print(state.review)

# Run Reporter Agent
state = reporter_agent(state)

print("\n===== Final Report =====")
print(state.report)