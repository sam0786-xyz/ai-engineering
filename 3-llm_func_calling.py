# Day 3 18th May 2026 - LLM Function Calling & Pydantic V2 Integration

from pydantic import BaseModel,ValidationError, Field, field_validator, ConfigDict
import json, datetime, os
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
class FlightDetails(BaseModel):
    departure_city : str
    arrival_city : str
    departure_date : datetime.date

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model = 'gemini-flash-lite-latest',
    contents = "book a flight from Delhi to Abu Dhabi on 22th June 2026",
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=FlightDetails,
    )
)

# print(response.text)

validated_flight = FlightDetails.model_validate_json(response.text)
print(validated_flight.departure_date)
print(type(validated_flight.departure_date))
