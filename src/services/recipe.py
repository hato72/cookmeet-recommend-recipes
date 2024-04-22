from src.schemas.recipe import Recipe, IRecipeFetcher, RecipeForRecommend
from typing import Final
import time
from src.schemas.category import CategoryId, CategoryIdWithRank

class RecipeService():
    
    _recipe_fetcher: IRecipeFetcher
    SLEEP_TIME: Final = 1
    
    def __init__(self, recipe_fetcher: IRecipeFetcher):
        self._recipe_fetcher = recipe_fetcher
    
    def fetch_recipes_by_ranked_category_ids(self, ranked_category_ids: list[CategoryIdWithRank]) -> dict[int, list[Recipe]]:
        recipes: dict[int, list[Recipe]] = {}
        for ranked_category_id in ranked_category_ids:
            # 一定時間スリープしてからリクエストを送る
            time.sleep(self.SLEEP_TIME)
            recipes[ranked_category_id.rank] = self._recipe_fetcher.fetch_recipe(ranked_category_id.cateogry_id)
            
        return recipes
    
    @classmethod
    def convert_recipes_to_recommend(cls, recipes: list[Recipe]) -> list[RecipeForRecommend]:
        return [RecipeForRecommend(recipe) for recipe in recipes]