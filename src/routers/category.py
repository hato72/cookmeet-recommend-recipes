from fastapi import APIRouter
from src.services.category import CategoryService
from src.cruds.category import CategoryCRUD
from src.fetchers.category import CategoryFetcher

router = APIRouter()

@router.get('/categories/cache')
async def cache_categories():
    category_service = CategoryService(CategoryCRUD(), CategoryFetcher())
    category_service.cache_categories()

@router.get('/categories')
async def get_categories():
    category_service = CategoryService(CategoryCRUD(), CategoryFetcher())
    return category_service.get_all_categories()