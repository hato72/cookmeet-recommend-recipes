from fastapi import APIRouter

router = APIRouter()

@router.get('/recipes/{category_id}')
async def get_recipes(category_id: str, num: int = 5):
    pass

