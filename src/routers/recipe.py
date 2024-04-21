from fastapi import APIRouter
from src.services.recipe import RecipeService
from src.fetchers.recipe import RecipeFetcher

router = APIRouter()

@router.get('/recipes/{category_id}')
async def get_recipes(category_id: str):
    recipe_service = RecipeService(RecipeFetcher())
    return recipe_service.fetch_recipes_by_category_ids([category_id])

