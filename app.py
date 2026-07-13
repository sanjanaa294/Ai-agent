from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.coder import coding_agent
from agents.reviewer import reviewer_agent
from agents.reporter import reporter_agent

# Get input from user
user_request = input("Enter your task: ")

# Create state as a dictionary
state = {
    "user_request": user_request,
    "plan": "",
    "research": "",
    "code": "",
    "review": "",
    "report": ""
}

# Run Planner Agent
state.update(planner_agent(state))

print("\n===== Planner Output =====")
print(state["plan"])

# Run Research Agent
state.update(research_agent(state))

print("\n===== Research Output =====")
print(state["research"])

# Run Coding Agent
state.update(coding_agent(state))

print("\n===== Coding Output =====")
print(state["code"])

# Run Reviewer Agent
state.update(reviewer_agent(state))

print("\n===== Reviewer Output =====")
print(state["review"])

# Run Reporter Agent
state.update(reporter_agent(state))

print("\n===== Final Report =====")
print(state["report"])