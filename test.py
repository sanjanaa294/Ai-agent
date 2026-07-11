from dotenv import load_dotenv
import os
from google import genai

# Load the .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Ask Gemini a question
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello! My name is Sanjana."
)

print(response.text)