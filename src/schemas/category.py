from pydantic import BaseModel, Field
from typing import NewType

CategoryId = NewType('CategoryId', str)

class Category(BaseModel):
    id: CategoryId = Field(..., title='ID', description='10-200のような形式', pattern='[0-9]+-[0-9]+')
    name: str
    url: str = Field(..., title="URL", pattern="https?://[\\w!?/+\\-_~;.,*&@#$%()'\\[\\]]+") # urlの正規表現
    
    
class CategoryForRecommend(BaseModel):
    id: str
    name: str
    
    def __init__(self, category: Category):
        self.id = category.id
        self.name = category.name
        
        
# レコメンドした後の返り値はこの形式で返す
class CategoryIdWithRank(BaseModel):
    rank: int
    cateogry_id: CategoryId