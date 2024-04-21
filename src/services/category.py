from src.schemas.category import Category
import src.config as config
from typing import List
import requests

def fetch_categories() -> List[Category] | Exception:
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
    
        return categories
    
    # 一旦普通にエラーを投げる
    except Exception as e:
        raise e