from fastapi import FastAPI
from src.routers import category, recipe, recommend

app = FastAPI()

app.include_router(category.router, prefix='/v1')
app.include_router(recipe.router, prefix='/v1')
app.include_router(recommend.router, prefix='/v1')