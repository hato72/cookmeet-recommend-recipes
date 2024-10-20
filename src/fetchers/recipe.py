from src.schemas.recipe import Recipe, IRecipeFetcher
import requests
import src.config as config
from src.schemas.category import CategoryId

class RecipeFetcher(IRecipeFetcher):
    def fetch_recipe(self, category_id: CategoryId) -> list[Recipe]:
        res = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426', params={
            'applicationId': config.RAKUTEN_APPLICATION_ID,
            'format': 'json',
            'elemnts': 'recipeId,foodImageUrl,recipeDescription,recipeTitle,recipeUrl,recipeMaterial',
            'categoryId': category_id
        })
        
        if res.status_code != 200:
            raise Exception(f"Error fetching recipes: {res.status_code} - {res.text}")
        
        data = res.json()
        recipes = data.get('result', [])
        
        # recipeのキー名を変更
        for recipe in recipes:
            recipe['id'] = recipe.pop('recipeId')
            recipe['title'] = recipe.pop('recipeTitle')
            recipe['url'] = recipe.pop('recipeUrl')
            recipe['description'] = recipe.pop('recipeDescription')
            recipe['image_url'] = recipe.pop('foodImageUrl')
            recipe['recipe_materials'] = recipe.pop('recipeMaterial')
            recipe['category_id'] = category_id
            
        recipes = [Recipe(**recipe) for recipe in recipes]
        
        return recipes 