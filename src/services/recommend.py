from pydantic import BaseModel
from src.schemas.recommend import IRecommend
from src.schemas.category import CategoryForRecommend, CategoryIdWithRank
from src.schemas.recipe import RecipeForRecommend, RecipeIdWithRank

class RecommendService(BaseModel):
    _recommend: IRecommend
    
    def __init__(self, recommend: IRecommend):
        self._recommend = recommend
        
    def recommend_categories(self, psychorogical_test_results: list[str], categories: list[CategoryForRecommend], num_categories_to_recommend: int = 3) -> list[CategoryIdWithRank]:
        return self._recommend.recommend_categories(psychorogical_test_results, categories, num_categories_to_recommend)
    
    def recommend_recipes(self, conditions: list[str], category_2_recipes: dict[str, list[RecipeForRecommend]], categories_rank: list[CategoryIdWithRank]) -> list[RecipeIdWithRank]:
        return self._recommend.recommend_recipes(conditions, category_2_recipes, categories_rank)