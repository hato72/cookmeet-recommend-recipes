from src.schemas.category import Category
from src.schemas.recipe import Recipe
from src.schemas.recommend import Recommend

class Recommend(Recommend):
    def recommend_categories(self, psychorogical_test_results: list[str], num_categories_to_recommend: int = 5) -> list[Category]:
        return super().recommend_categories(psychorogical_test_results, num_categories_to_recommend)
    
    def recommend_recipes(self, contditions: list[str], num_recipes_to_recommend: int = 3) -> list[Recipe]:
        return super().recommend_recipes(contditions, num_recipes_to_recommend)