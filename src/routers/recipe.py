from fastapi import APIRouter
from src.services.recipe import RecipeService
from src.fetchers.recipe import RecipeFetcher
from src.schemas.category import CategoryId
from src.schemas.recommend import RecommendRequestBody

router = APIRouter()

@router.post('/recipes/recommend')
async def recommend_recipes(recommend_request_body: RecommendRequestBody):
    pass

