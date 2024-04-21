from fastapi import APIRouter

router = APIRouter()

@router.get('/categories')
async def get_categories():
    pass