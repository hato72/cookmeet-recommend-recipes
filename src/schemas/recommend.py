from pydantic import BaseModel
from abc import ABC, abstractmethod
from src.schemas.category import CategoryForRecommend, CategoryIdWithRank
from src.schemas.recipe import RecipeForRecommend, RecipeWithRank

class RecommendRequestBody(BaseModel):
    texts: list[str]
    conditions: list[str]
    
class Recommend(ABC):
    
    @abstractmethod
    def recommend_categories(self, psychorogical_test_results: list[str], categories: list[CategoryForRecommend], num_categories_to_recommend: int = 5) -> list[CategoryIdWithRank]:
        """
        おすすめのカテゴリを返す。
        
        返り値は{"順位": "カテゴリID"}の形式で返す
        """
        pass
    
    @abstractmethod
    def recommend_recipes(self, contditions: list[str], recipes: list[RecipeForRecommend] ,num_recipes_to_recommend: int = 3) -> list[RecipeWithRank]:
        """
        おすすめのレシピを返す
        
        返り値は{"順位": "レシピ"}の形式で返す
        """
        pass