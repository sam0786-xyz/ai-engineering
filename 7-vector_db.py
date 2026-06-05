import chromadb
from chromadb.utils import embedding_functions
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

gemini_client = genai.Client(api_key=api_key)

client = chromadb.PersistentClient(path = "vector_db")

collection = client.create_collection(
    name = 'first_collection',
    embedding_function = gemini_client
)

collection.add(
    documents = "Hello everyone",
    metadatas = {"source": "tutorial"},
    ids = "1"
)

print(collection.peek(10))