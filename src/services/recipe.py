from src.schemas.recipe import Recipe, IRecipeFetcher, RecipeForRecommend
from typing import Final
import time
from src.schemas.category import CategoryId, CategoryIdWithRank

class RecipeService():
    
    _recipe_fetcher: IRecipeFetcher
    SLEEP_TIME: Final = 1
    
    def __init__(self, recipe_fetcher: IRecipeFetcher):
        self._recipe_fetcher = recipe_fetcher
    
    def fetch_recipes_by_category_ids(self, category_ids: list[CategoryId]) -> list[Recipe]:
        recipes: list[Recipe] = []
        for category_id in category_ids:
            # 一定時間スリープしてからリクエストを送る
            time.sleep(self.SLEEP_TIME)
            fetched_recipes = self._recipe_fetcher.fetch_recipe(category_id)
            for fetched_recipe in fetched_recipes:
                fetched_recipe.category_id = category_id
            
            recipes.extend(fetched_recipes)
            
        return recipes
    
    @classmethod
    def convert_recipes_to_recommend(cls, recipes: list[Recipe]) -> list[RecipeForRecommend]:
        return [RecipeForRecommend(recipe) for recipe in recipes]