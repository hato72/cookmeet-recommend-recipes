from typing_extensions import Unpack
from pydantic import BaseModel, ConfigDict, Field, field_validator
from abc import ABC, abstractmethod
from src.schemas.category import CategoryId

class Recipe(BaseModel):
    id: int
    title: str
    url: str = Field(..., title='URL', pattern="https?://[\\w!?/+\\-_~;.,*&@#$%()'\\[\\]]+") # URLの正規表現
    description: str
    image_url: str = Field(..., title='Image URL', pattern="https?://[\\w!?/+\\-_~;.,*&@#$%()'\\[\\]]+")
    category_id: CategoryId | None = None,
    recipe_materials: list[str]
    
# レコメンドの際に使うレシピのスキーマ
class RecipeForRecommend(BaseModel):
    id: int
    title: str
    description: str
    
    def __init__(self, recipe: Recipe):
        super().__init__(id=recipe.id, title=recipe.title, description=recipe.description)
        self.id = recipe.id
        self.title = recipe.title
        self.description = recipe.description
        
# おすすめとして返すレシピの返り値
class RecipeWithRank(BaseModel):
    rank: int
    recipe: Recipe
    
# レコメンド後のレシピの返り値
class RecipeIdWithRank(BaseModel):
    rank: int
    recipe_id: int
    
# レシピ取得用の抽象クラス
class IRecipeFetcher(ABC):
    @abstractmethod
    def fetch_recipe(self, category_id: CategoryId) -> list[Recipe]:
        """
        レシピを取得する
        
        category_idは大-中の順で指定する
        例: 10-200
        """
        pass