from fastapi import APIRouter

router = APIRouter()

@router.get('/categories/cache')
async def get_categories():
    pass