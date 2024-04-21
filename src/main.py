from fastapi import FastAPI
from src.routers import category

app = FastAPI()

app.include_router(category.router, prefix='/v1')