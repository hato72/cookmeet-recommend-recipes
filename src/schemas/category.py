from pydantic import BaseModel, Field
from typing import NewType

CategoryId = NewType('CategoryId', str)

class Category(BaseModel):
    id: CategoryId
    name: str
    url: str = Field(..., title="URL", pattern="https?://[\\w!?/+\\-_~;.,*&@#$%()'\\[\\]]+") # urlの正規表現