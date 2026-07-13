from ai_client import client

def coding_agent(state):
    prompt = f"""
    You are a Coding Agent.

    Your job is to generate clean, well-structured Python code.

    User Request:
    {state["user_request"]}

    Planner Output:
    {state["plan"]}

    Research Output:
    {state["research"]}

    Write:
    1. Clean Python code
    2. Proper comments
    3. Explain the code briefly.

    Return the response in a clear format.
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
        "code": response.choices[0].message.content
    }