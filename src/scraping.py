import requests
from bs4 import BeautifulSoup

# URLからHTMLを取得
url = "https://recipe.rakuten.co.jp/recipe/1570003792/"
response = requests.get(url)
html_content = response.content

# HTMLを解析
soup = BeautifulSoup(html_content, 'html.parser')


# 材料の部分を取得
recipe_ingredients = soup.find("ul", class_="recipe_material__list").find_all("li", class_="recipe_material__item")

# レシピの材料を表示
print("材料:")
for ingredient in recipe_ingredients:
    ingredient_name = ingredient.find("span", class_="recipe_material__item_name").text.strip()
    ingredient_amount = ingredient.find("span", class_="recipe_material__item_serving").text.strip()
    print(f"{ingredient_name}: {ingredient_amount}")


# 作り方の部分を取得
recipe_steps = soup.find("ol", class_="recipe_howto__list").find_all("span", class_="recipe_howto__text")

# レシピの手順を表示
print()
print("作り方")
for index, step in enumerate(recipe_steps, start=1):
    print(f"{index}. {step.text.strip()}")
