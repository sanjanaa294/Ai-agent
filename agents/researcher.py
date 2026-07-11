from ai_client import client

def research_agent(state):
    prompt = f"""
    You are a Research Agent.

    Your job is to research the user's request based on the planner's task list.

    User Request:
    {state.user_request}

    Planner Output:
    {state.plan}

    Give:
    1. Recommended technologies
    2. Useful libraries
    3. Best practices
    4. Helpful resources
    5. Important things to remember

    Keep the response clear and well organized.
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

    state.research = response.choices[0].message.content
    return state