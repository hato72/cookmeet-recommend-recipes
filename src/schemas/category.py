from pydantic import BaseModel, Field
from typing import NewType

CategoryId = NewType('CategoryId', str)

class Category(BaseModel):
    id: CategoryId = Field(..., title='ID', description='10-200のような形式', pattern='[0-9]+-[0-9]+')
    name: str
    url: str = Field(..., title="URL", pattern="https?://[\\w!?/+\\-_~;.,*&@#$%()'\\[\\]]+") # urlの正規表現