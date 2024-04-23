from src.schemas.category import CategoryForRecommend, CategoryIdWithRank
from src.schemas.recipe import RecipeForRecommend, RecipeIdWithRank
from src.schemas.recommend import IRecommend
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate

class Recommend(IRecommend):
    def recommend_categories(self, psychorogical_test_results: list[str], categories: list[CategoryForRecommend], num_categories_to_recommend: int) -> list[CategoryIdWithRank]:
        
        llm = ChatGoogleGenerativeAI(model='gemini-pro')
        
        prompt = PromptTemplate(
            template="""
            心理テストの結果からおすすめの料理のカテゴリを第1位から第3位まで教えてください。出力は出力形式に従ってください。
            
            心理テストの結果: {psychorogical_test_results}
            
            カテゴリのリスト: {categories}
           
            出力形式: {{"items": [{{"rank": 1, "category_id": "12343434"}}, {{"rank": 2, "category_id": "12343435"}}, {{"rank": 3, "category_id": "12343436"}}]}}
            """,
            input_variables=[
                'psychorogical_test_results',
                'categories'
            ]
        )
        
        class CategoryIdWithRankList(BaseModel):
            items: list[CategoryIdWithRank]
    
            
        output_parser = PydanticOutputParser(pydantic_object=CategoryIdWithRankList)
        result = llm.invoke(prompt.format(psychorogical_test_results=psychorogical_test_results, categories=categories))
        parsed_result = output_parser.parse(result.content)
        
        return parsed_result.items
    
    def recommend_recipes(self, conditions: list[str], recipes: list[RecipeForRecommend], categories_rank: list[CategoryIdWithRank] , num_recipes_to_recommend: int = 3) -> list[RecipeIdWithRank]:
        llm = ChatGoogleGenerativeAI(model='gemini-pro')
        
        class RecipeIdWithRankList(BaseModel):
            items: list[RecipeIdWithRank]
            
        prompt = PromptTemplate(
            template="""
            条件からおすすめのレシピを第1位から第3位まで教えてください。
            ただし、第n位のレシピは第n位のカテゴリに属するレシピから選んでください。
            出力は出力形式に従ってください.
            
            条件: {conditions}
            
            レシピのリスト: {recipes}
            
            カテゴリのランク: {categories_rank}
            
            出力形式: {{"items": [{{"recipe_id": 12343434, "rank": 1}}, {{"recipe_id": 12343435, "rank": 2}}, {{"recipe_id": 12343436, "rank": 3}}]}}
            """,
            input_variables=[
                'conditions',
                'recipes',
                'categories_rank'
            ]
        )
            
        parser = PydanticOutputParser(pydantic_object=RecipeIdWithRankList)
        result = llm.invoke(prompt.format(conditions=conditions, recipes=recipes, categories_rank=categories_rank))
        parsed_result = parser.parse(result.content)
        
        return parsed_result.items
