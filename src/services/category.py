from src.schemas.category import Category, CategoryForRecommend, ICategoryCRUD, ICategoryFetcher
import src.config as config
import requests
from abc import ABC, abstractmethod
from pydantic import BaseModel

class CategoryService(BaseModel):
    category_crud: ICategoryCRUD
    category_fetcher: ICategoryFetcher
    
    def __init__(self, category_crud: ICategoryCRUD, category_fetcher: ICategoryFetcher):
        super().__init__(category_crud=category_crud, category_fetcher=category_fetcher)
        self.category_crud = category_crud
        self.category_fetcher = category_fetcher
        
    def cache_categories(self):
        categories = self.category_fetcher.fetch()
        self.category_crud.cache_categories(categories)
        
    def get_all_categories(self) -> list[Category]:
        categories = self.category_crud.get_all_categories()
        
        if not categories:
            # もしキャッシュにデータがなければもう一度取得してそれをキャッシュする
            categories = self.category_fetcher.fetch()
            self.category_crud.cache_categories(categories)
            return categories
        
        return categories
            
    @classmethod
    def convert_categories_to_recommend(cls, categories: list[Category]) -> list[CategoryForRecommend]:
        return [CategoryForRecommend(category) for category in categories]
  