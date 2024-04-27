from fastapi import APIRouter
from src.services.recipe import RecipeService
from src.fetchers.recipe import RecipeFetcher
from src.schemas.category import CategoryId
from src.scraping import scraping_reciep_steps

router = APIRouter()

@router.get('/recipes/{category_id}')
async def get_recipes_by_category_id(category_id: CategoryId):
    recipe_service = RecipeService(RecipeFetcher())
    return recipe_service.fetch_recipes_by_category_ids([category_id])

@router.get('/recipes/{recipe_id}/details')
async def get_recipe_steps(recipe_id: int):
    recipe_ingredients, recipe_steps = scraping_reciep_steps(recipe_id=recipe_id)
    return {"recipe_id": recipe_id, "ingredients": recipe_ingredients, "steps": recipe_steps}
    
    
    

