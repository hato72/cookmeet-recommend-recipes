from fastapi import APIRouter
from src.services.category import CategoryService
from src.cruds.category import CategoryCRUD
from src.fetchers.category import CategoryFetcher
from src.services.recommend import RecommendService
from src.ai.recommend import Recommend
from src.schemas.recommend import RecommendRequestBody
from src.schemas.recipe import RecipeForRecommend
from src.services.recipe import RecipeService
from src.fetchers.recipe import RecipeFetcher

router = APIRouter()

@router.post('/recipes/recommend')
async def recommend_recipes(recomend_request_body: RecommendRequestBody):
    # 心理テストからおすすめのカテゴリを取得
    category_service = CategoryService(CategoryCRUD(), CategoryFetcher())
    all_categories = category_service.get_all_categories()
    recommened_service = RecommendService(Recommend())
    # AIに読み取らせるために余計なフィールドを省く（URLなど）
    all_categories_to_recommend = category_service.convert_categories_to_recommend(all_categories)
    # 順位付けされたカテゴリのIDを取得
    ranked_categories_id = recommened_service.recommend_categories(psychorogical_test_results=recomend_request_body.texts, categories=all_categories_to_recommend)
    # 順位付けされたカテゴリのIDからカテゴリのIDを抽出
    recommended_categories_id = list(map(lambda x: x.category_id, ranked_categories_id))
    
    # カテゴリからレシピを取得し、必須条件から最も合うものを選ぶ
    recipe_service = RecipeService(RecipeFetcher())
    # カテゴリのIDからレシピを取得
    recipes = recipe_service.fetch_recipes_by_category_ids(recommended_categories_id)
    # AIに読み取らせるために余計なフィールドを省く（URLなど）
    recipes_to_recommend: list[RecipeForRecommend] = recipe_service.convert_recipes_to_recommend(recipes)
    # おすすめのレシピのIDをランキング付きで取得
    ranked_recipe_ids = recommened_service.recommend_recipes(conditions=recomend_request_body.conditions, recipes=recipes_to_recommend, categories_rank=ranked_categories_id)
    # IDの情報を元のレシピに変換
    ranked_recipes = recipe_service.convert_recipe_ids_to_ranked_recipes(ranked_recipe_ids, recipes)
    return {"recipes": ranked_recipes}
        
    
    