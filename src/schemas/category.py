from pydantic import BaseModel, Field
from typing import NewType
from abc import ABC, abstractmethod

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
    category_id: CategoryId
    
# データベースとやり取りするための抽象クラス
class ICategoryCRUD(ABC, BaseModel):
    @abstractmethod
    def cache_categories(self, categories: list[Category]):
        pass
    
    @abstractmethod
    def get_all_categories(self) -> list[Category]:
        pass
    
# カテゴリー情報を取得するための抽象クラス
class ICategoryFetcher(ABC, BaseModel):
    @abstractmethod
    def fetch(self) -> list[Category]:
        pass