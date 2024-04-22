from src.schemas.category import CategoryForRecommend, CategoryIdWithRank
from src.schemas.recipe import RecipeForRecommend, RecipeIdWithRank
from src.schemas.recommend import IRecommend

class Recommend(IRecommend):
    def recommend_categories(self, psychorogical_test_results: list[str], categories: list[CategoryForRecommend], num_categories_to_recommend: int) -> list[CategoryIdWithRank]:
        return super().recommend_categories(psychorogical_test_results, categories, num_categories_to_recommend)
    
    def recommend_recipes(self, contditions: list[str], rank2recipes: dict[int, list[RecipeForRecommend]], num_recipes_to_recommend: int = 3) -> list[RecipeIdWithRank]:
        return super().recommend_recipes(contditions, rank2recipes, num_recipes_to_recommend)