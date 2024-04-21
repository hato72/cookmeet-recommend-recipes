from pydantic import BaseModel, Field

class Recipe(BaseModel):
    id: int
    title: str
    url: str = Field(..., title='URL', pattern="https?://[\\w!?/+\\-_~;.,*&@#$%()'\\[\\]]+") # URLの正規表現
    description: str
    image_url: str = Field(..., title='Image URL', pattern="https?://[\\w!?/+\\-_~;.,*&@#$%()'\\[\\]]+")
    