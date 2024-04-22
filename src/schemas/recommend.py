from pydantic import BaseModel
from abc import ABC, abstractmethod
from src.schemas.category import CategoryForRecommend
from src.schemas.recipe import RecipeForRecommend

class RecommendRequestBody(BaseModel):
    texts: list[str]
    conditions: list[str]
    
class Recommend(ABC):
    
    @abstractmethod
    def recommend_categories(self, psychorogical_test_results: list[str], categories: list[CategoryForRecommend], num_categories_to_recommend: int = 5) -> list[CategoryForRecommend]:
        pass
    
    @abstractmethod
    def recommend_recipes(self, contditions: list[str], recipes: list[RecipeForRecommend] ,num_recipes_to_recommend: int = 3) -> list[RecipeForRecommend]:
        pass