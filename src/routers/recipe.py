from fastapi import APIRouter
from src.services.recipe import RecipeService
from src.fetchers.recipe import RecipeFetcher
from src.schemas.category import CategoryId
from src.schemas.recommend import RecommendRequestBody

router = APIRouter()

@router.get('/recipes/{category_id}')
async def get_recipes_by_category_id(category_id: CategoryId):
    recipe_service = RecipeService(RecipeFetcher())
    return recipe_service.fetch_recipes_by_category_ids([category_id])

@router.post('/recipes/recommend')
async def recommend_recipes(recommend_request_body: RecommendRequestBody):
    pass

