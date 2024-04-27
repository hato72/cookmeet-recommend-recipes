import requests
from bs4 import BeautifulSoup
from src.schemas.recipe import RecipeStep, RecipeIngredient

# URLからHTMLを取得
def scraping_reciep_steps(recipe_id: int) -> tuple[list[RecipeIngredient], list[RecipeStep]]:
    url = f"https://recipe.rakuten.co.jp/recipe/{recipe_id}/"
    response = requests.get(url)
    html_content = response.content

    # HTMLを解析
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 材料の部分を取得
    recipe_ingredients = soup.find("ul", class_="recipe_material__list").find_all("li", class_="recipe_material__item")
    
    # 材料の部分をパース
    recipe_ingredients = [RecipeIngredient(name = recipe_ingredient.find("span", class_="recipe_material__item_name").text.strip(), amount=recipe_ingredient.find("span", class_="recipe_material__item_serving").text.strip()) for recipe_ingredient in recipe_ingredients]

    # 作り方の部分を取得
    recipe_steps = soup.find("ol", class_="recipe_howto__list").find_all("span", class_="recipe_howto__text")

    recipe_steps = [RecipeStep(index=index, step=step.text.strip()) for index, step in enumerate(recipe_steps, start=1)]

    return recipe_ingredients, recipe_steps
