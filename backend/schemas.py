from pydantic import BaseModel, Field

class TextInput(BaseModel):
    text: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="User input text for mood prediction"
    )
