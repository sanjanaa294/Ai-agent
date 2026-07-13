from ai_client import client

def reviewer_agent(state):
    prompt = f"""
    You are a Senior Python Code Reviewer.

    Review the following code.

    User Request:
    {state["user_request"]}

    Planner Output:
    {state["plan"]}

    Research Output:
    {state["research"]}

    Generated Code:
    {state["code"]}

    Check for:

    1. Bugs
    2. Code Quality
    3. Best Practices
    4. Missing Features
    5. Suggestions for Improvement

    Give your review in a clear and organized format.
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
        "review": response.choices[0].message.content
    }