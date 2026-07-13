from ai_client import client

def planner_agent(state):
    prompt = f"""
    You are a Planner Agent.

    Your job is to break the user's request into small, clear tasks.

    User Request:
    {state["user_request"]}

    Return only a numbered list of tasks.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "plan": response.choices[0].message.content
    }