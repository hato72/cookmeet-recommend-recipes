from src.services.category import ICategoryFetcher
from src.schemas.category import Category
import requests
import src.config as config

class CategoryFetcher(ICategoryFetcher):
    def fetch(self) -> list[Category]:
        try:
            req = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?',
                            params={
                                'applicationId': config.RAKUTEN_APPLICATION_ID,
                                'format': 'json',
                                'categoryType': 'medium',
                                'elements': 'categoryId,categoryName,categoryUrl,parentCategoryId',
                            })
    
            data = req.json()
            categories = data['result']['medium']
    
            # Categoryのスキーマに合うようにリネーム
            for category in categories:
                category['id'] = str(category.pop('parentCategoryId')) + '-' + str(category.pop('categoryId'))
                category['name'] = category.pop('categoryName')
                category['url'] = category.pop('categoryUrl')
                
            # categoriesをリストに格納
            categories = [Category(**category) for category in categories]
   
            return categories
    
        # 一旦普通にエラーを投げる
        except Exception as e:
            raise e