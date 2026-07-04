from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

interaction = client.interactions.create(
    model = "gemini-3.5-flash",
    system_instruction = "Act as a harsh code reviewer and answer the question. if the question is not related to code, refuse to answer. and just say Rejected and nothing more",
    input = "what is a apple?"
)

print(interaction.output_text)