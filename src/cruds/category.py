import redis # type: ignore
from abc import ABC, abstractmethod
import redis.client
from src.schemas.category import Category
from src.services.category import ICategoryCRUD
import json
from typing import ClassVar
import src.config as config

class CategoryCRUD(ICategoryCRUD):
    
    r: ClassVar[redis.Redis] = redis.Redis(host=config.REDISHOST, port=config.REDISPORT, db=0, decode_responses=True)
    model_config = {
        'arbitrary_types_allowed': True
    }
        
    def cache_categories(self, categories: list[Category]):
        if not self.r:
            raise Exception('Redisの接続に失敗しました')
        for category in categories:
            self.r.hset('categories', str(category.id), category.model_dump_json())
            
    def get_all_categories(self) -> list[Category]:
        if not self.r:
            raise Exception('Redisの接続に失敗しました')
        
        categories: list[Category] = []
        
        redis_categories = self.r.hgetall('categories')
        
        for category_raw in redis_categories.values():
            category_dict = json.loads(category_raw)
            category = Category.model_validate(category_dict)
            categories.append(category)
            
        return categories

