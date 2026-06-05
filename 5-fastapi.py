# Day 4 21st May 2026 - Fast API

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    page_count: int = Field(ge=1) # Must be at least 1 page

# Notice the async def here!
@app.post("/books")
async def create_book(book: Book):
    # If the code reaches this line, Pydantic guarantees the data is 100% valid
    # We simulate saving to a database with a tiny async sleep
    import asyncio
    await asyncio.sleep(0.5) 
    
    return {"message": "Book saved successfully!", "data": book}

# Day 5 3rd June 2026

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/hello")
def hello(name: str = "Sameer"):
    return {"message": f"Hello {name}"}
