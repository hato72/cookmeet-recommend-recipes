from src.schemas.recipe import Recipe, IRecipeFetcher
import requests
import src.config as config

class RecipeFetcher(IRecipeFetcher):
    def fetch_recipe(self, category_id: str) -> list[Recipe]:
        res = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426', params={
            'applicationId': config.RAKUTEN_APPLICATION_ID,
            'format': 'json',
            'elemnts': 'recipeId,foodImageUrl,recipeDescription,recipeTitle,recipeUrl',
            'categoryId': category_id
        })
        
        data = res.json()
        recipes = data['result']
        
        # recipeのキー名を変更
        for recipe in recipes:
            recipe['id'] = recipe.pop('recipeId')
            recipe['title'] = recipe.pop('recipeTitle')
            recipe['url'] = recipe.pop('recipeUrl')
            recipe['description'] = recipe.pop('recipeDescription')
            recipe['image_url'] = recipe.pop('foodImageUrl')
            
        recipes = [Recipe(**recipe) for recipe in recipes]
        
        return recipes 