from src.schemas.category import Category
from typing import List
import requests

def fetch_category() -> List[Category]:
    req = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?',
                       params={
                           'applicationId': '1069371834256835280',
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