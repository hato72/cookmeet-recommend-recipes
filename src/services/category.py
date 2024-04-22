from src.schemas.category import Category
import src.config as config
import requests
from abc import ABC, abstractmethod
from pydantic import BaseModel

# データベースとやり取りするための抽象クラス
class ICategoryCRUD(ABC):
    @abstractmethod
    def cache_categories(self, categories: list[Category]):
        pass
    
    @abstractmethod
    def get_all_categories(self) -> list[Category]:
        pass
    
# カテゴリー情報を取得するための抽象クラス
class ICategoryFetcher(ABC):
    @abstractmethod
    def fetch(self) -> list[Category]:
        pass

class CategoryService(BaseModel):
    category_crud: ICategoryCRUD
    category_fetcher: ICategoryFetcher
    
    def __init__(self, category_crud: ICategoryCRUD, category_fetcher: ICategoryFetcher):
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
  