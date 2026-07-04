from pydantic import BaseModel, Field
import os
from google import genai
from google.genai import types
from google.oauth2 import service_account

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
credentials = service_account.Credentials.from_service_account_file("credentials.json", scopes=["https://www.googleapis.com/auth/cloud-platform"])

client = genai.Client(
    vertexai=True, 
    project="gen-lang-client-0845898590", 
    location="us-central1",
    credentials=credentials
)

class CodeReviewResult(BaseModel):
    is_secure: bool
    vulnerabilities_found: list[str]
    severity_score: int = Field(ge = 1, le = 10)
    recommended_fix: str

code = """
import os
api_key = 'AQ.skjjgsugdetepKhgGFEP'
print(api_key)
"""

response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents = code,
    config={
        "response_mime_type": "application/json",
        "response_schema": CodeReviewResult
    }

)

result = response.parsed

# 3. Prove it works programmatically
print(f"Is Secure? {result.is_secure}")
print(f"Severity Score: {result.severity_score}/10")
print(f"Vulnerabilities: {result.vulnerabilities_found}")
print(f"Recommended Fix: {result.recommended_fix}")