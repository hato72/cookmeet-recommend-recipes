from src.schemas.recipe import Recipe, IRecipeFetcher
from typing import Final
import time

class RecipeService():
    
    _recipe_fetcher: IRecipeFetcher
    SLEEP_TIME: Final = 1
    
    def __init__(self, recipe_fetcher: IRecipeFetcher):
        self._recipe_fetcher = recipe_fetcher
    
    def fetch_recipes_by_category_ids(self, category_ids: list[str]) -> dict[str, list[Recipe]] | dict[str, str]:
        # category_idのフォーマットをチェック
        for category_id in category_ids:
            parts = category_id.split('-')
            if len(parts) != 3:
                return {
                    'error': 'カテゴリーのIDは大-中-小の3つの部分で指定してください'
                }
                
        recipes: dict[str, list[Recipe]] = {}
        for category_id in category_ids:
            # 一定時間スリープしてからリクエストを送る
            time.sleep(self.SLEEP_TIME)
            recipes[category_id] = self._recipe_fetcher.fetch_recipe(category_id)
            
        return recipes