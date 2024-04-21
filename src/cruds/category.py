import redis # type: ignore
from abc import ABC, abstractmethod
from src.schemas.category import Category
from src.services.category import ICategoryCRUD
import json


class CategoryCRUD(ICategoryCRUD):
    r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
        
    def cache_categories(self, categories: list[Category]):
        for category in categories:
            self.r.hset('categories', str(category.id), category.model_dump_json())
            
    def get_all_categories(self) -> list[Category]:
        categories: list[Category] = []
        
        redis_categories = self.r.hgetall('categories')
        
        for category_raw in redis_categories.values():
            category_dict = json.loads(category_raw)
            category = Category.model_validate(category_dict)
            categories.append(category)
            
        return categories

