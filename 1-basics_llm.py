# Day 1 15th May 2026 - Basics of LLM

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model = 'gemini-flash-lite-latest' ,
    contents = """search the internet and tell the best ways to apply for a internship in AI engineering field.
     I am a 3rd year student who just gave his 6th sem final exams, research latest things in 2026""",
    
)

response1 = client.models.generate_content(
    model = 'gemini-flash-lite-latest' ,
    contents = """search the internet and tell the best ways to apply for a internship in AI engineering field.
     I am a 3rd year student who just gave his 6th sem final exams, research latest things in 2026""",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)


print(response.text)
