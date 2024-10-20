from pydantic import BaseModel
from src.schemas.recommend import IRecommend
from src.schemas.category import CategoryForRecommend, CategoryIdWithRank
from src.schemas.recipe import RecipeForRecommend, RecipeIdWithRank

class RecommendService(BaseModel):
    _recommend: IRecommend
    
    def __init__(self, recommend: IRecommend):
        super().__init__(recommend=recommend)
        self._recommend = recommend
        
    def recommend_categories(self, psychorogical_test_results: list[str], categories: list[CategoryForRecommend], num_categories_to_recommend: int = 3) -> list[CategoryIdWithRank]:
        try:
            return self._recommend.recommend_categories(psychorogical_test_results, categories, num_categories_to_recommend)
        except Exception as e:
            raise Exception(f"Error recommending categories: {str(e)}")
    
    def recommend_recipes(self, conditions: list[str], recipes: list[RecipeForRecommend], categories_rank: list[CategoryIdWithRank]) -> list[RecipeIdWithRank]:
        try:
            return self._recommend.recommend_recipes(conditions, recipes, categories_rank)
        except Exception as e:
            raise Exception(f"Error recommending recipes: {str(e)}")
