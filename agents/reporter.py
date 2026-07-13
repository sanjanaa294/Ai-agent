from ai_client import client

def reporter_agent(state):
    prompt = f"""
    You are a Report Generator Agent.

    Create a professional project report using the following information.

    User Request:
    {state["user_request"]}

    Planner Output:
    {state["plan"]}

    Research Output:
    {state["research"]}

    Coding Output:
    {state["code"]}

    Reviewer Output:
    {state["review"]}

    Generate a report with the following sections:

    1. Project Overview
    2. Project Plan Summary
    3. Technologies Recommended
    4. Code Summary
    5. Review Summary
    6. Suggested Improvements
    7. Final Conclusion

    Make the report professional and easy to read.
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
        "report": response.choices[0].message.content
    }