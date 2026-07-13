from typing import TypedDict

class AgentState(TypedDict):
    user_request: str
    plan: str
    research: str
    code: str
    review: str
    report: str