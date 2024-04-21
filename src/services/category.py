from src.schemas.category import Category
import src.config as config
import requests
from abc import ABC, abstractmethod
from dataclasses import dataclass

# データベースとやり取りするための抽象クラス
class ICategoryCRUD(ABC):
    @abstractmethod
    def cache_categories(self, categories: list[Category]):
        pass
    
    @abstractmethod
    def get_all_categories(self) -> list[Category]:
        pass
    

@dataclass
class CategoryService():
    category_crud: ICategoryCRUD
    
    def __init__(self, category_crud: ICategoryCRUD):
        self.category_crud = category_crud
        
    def fetch_categories(self) -> list[Category]:
        try:
            req = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?',
                            params={
                                'applicationId': config.RAKUTEN_APPLICATION_ID,
                                'format': 'json',
                                'categoryType': 'small',
                                'elements': 'categoryId,categoryName,categoryUrl',
                            })
    
            data = req.json()
            categories = data['result']['small']
    
            # Categoryのスキーマに合うようにリネーム
            for category in categories:
                category['id'] = category.pop('categoryId')
                category['name'] = category.pop('categoryName')
                category['url'] = category.pop('categoryUrl')
                
            # categoriesをリストに格納
            categories = [Category(**category) for category in categories]
   
            return categories
    
        # 一旦普通にエラーを投げる
        except Exception as e:
            raise e