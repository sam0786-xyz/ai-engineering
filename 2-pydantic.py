# # Day 2 - Pydantic Validation
# Uncomment the code to run it

from pydantic import BaseModel,ValidationError, Field, field_validator, ConfigDict
import json

class Author(BaseModel):
    name : str
    is_verified : bool

class Book(BaseModel):
    title : str
    author : Author
    page_count : int = Field(ge=0)

# class User(BaseModel):
#     username: str
#     age: int
#     is_active: bool

# book = Book(
#     title = "Learn AI",
#     author = "sameer",
#     page_count = "100"
# )

# my_user = User(
#     username = "sameer",
#     age = 22,
#     is_active = True
# )

# book2 = Book(
#     title = "Learn AI",
#     author = {
#         "name" : "sameer",
#         "is_verified" : True
#     },
#     page_count = "100"
# )


# # try:
# #     book1 = Book(title="Learn AI", author="sameer", page_count="5")
# # except ValidationError as e:
# #     print("❌ We caught an error!")
# #     print(e)

class Book_v2(BaseModel):
    title : str
    author : Author
    page_count : int = Field(ge=0)
    tags : list[str] = []
    subtitle : str | None = None
    @field_validator('title')
    @classmethod
    def check_dummy_data(cls, value: str) -> str:
        if "blaah" in value:
            raise ValueError("Titles cannot contain the word 'blaah'")
        return value
    model_config = ConfigDict(extra='forbid')

# book_v2 = Book_v2(
#     title = "Learn AI",
#     author = {
#         "name" : "sam",
#         "is_verified" : True
#     },
#     page_count = "100",
#     tags = ["AI", "Machine Learning"],
#     subtitle = "A Comprehensive Guide"
# )

# print(book_v2.model_dump_json(indent=2))


class User(BaseModel):
    username: str

    @field_validator('username')
    @classmethod
    def check_no_spaces(cls, value: str) -> str:
        if " " in value:
            # Raising a ValueError tells Pydantic the validation failed
            raise ValueError("Username cannot contain spaces") 
        return value # If it passes, you must return the value!

# book_v2 = Book_v2(
#     title = "Learn AI",
#     author = {
#         "name" : "sam",
#         "is_verified" : True
#     },
#     page_count = "100",
#     tags = ["AI", "Machine Learning"],
#     subtitle = "A Comprehensive Guide",
#     rating = 5
# )

incoming_json = """
{
  "title": "Learn AI",
  "author": {
    "name": "Sameer",
    "is_verified": true
  },
  "page_count": 120,
  "tags": ["AI", "Coding"]
}
"""
def process_payload(json_string: str):
    try:
        Book_v2.model_validate_json(json_string)
        print(Book_v2.model_dump_json(indent=2))
    except ValidationError as e:
        print(e.errors())

# process_payload(incoming_json)

schema = Book_v2.model_json_schema()
print(json.dumps(schema, indent=2))