from pydantic import BaseModel, Field

class Category(BaseModel):
    id: int
    name: str
    url: str = Field(..., title="URL", regex="https?://[\w!?/+\-_~;.,*&@#$%()'[\]]+") # urlの正規表現