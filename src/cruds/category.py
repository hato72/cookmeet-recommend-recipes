import redis
from abc import ABC, abstractmethod
from schemas.category import Category
from src.services.category import ICategoryCRUD

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

class CategoryCRUD(ICategoryCRUD):
    def cache_categories(self, categories: list[Category]):
        for category in categories:
            r.hset('categories', str(category.id), category.model_dump_json())
            
    def get_all_categories(self) -> list[Category]:
        categories: list[Category] = []
        
        redis_categories = r.hgetall('categories')
        
        for category_raw in redis_categories.values():
            category = Category.model_validate(category_raw)
            categories.append(category)
            
        return categories

