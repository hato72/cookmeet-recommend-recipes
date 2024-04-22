from pydantic import BaseModel
from abc import ABC, abstractmethod
from src.schemas.category import CategoryForRecommend, CategoryIdWithRank
from src.schemas.recipe import RecipeForRecommend, RecipeIdWithRank

class RecommendRequestBody(BaseModel):
    texts: list[str]
    conditions: list[str]
    
class IRecommend(ABC):
    
    @abstractmethod
    def recommend_categories(self, psychorogical_test_results: list[str], categories: list[CategoryForRecommend], num_categories_to_recommend: int) -> list[CategoryIdWithRank]:
        """
        おすすめのカテゴリを返す。
        
        返り値は{"順位": "カテゴリID"}の形式で返す
        """
        pass
    
    @abstractmethod
    def recommend_recipes(self, contditions: list[str], rank2recipes: dict[int, list[RecipeForRecommend]] ,num_recipes_to_recommend: int = 3) -> list[RecipeIdWithRank]:
        """
        おすすめのレシピを返す
        
        返り値は{"順位": "レシピID"}の形式で返す
        """
        pass