from fastapi import FastAPI
from src.routers import category, recipe, recommend
import src.config as config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #config.FRONTEND_URL,
    'http://localhost:3000',
    "https://cook-meet.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
async def root():
    return {'message': 'レシピレコメンドのAPIサーバーです'}

app.include_router(category.router, prefix='/v1')
app.include_router(recipe.router, prefix='/v1')
app.include_router(recommend.router, prefix='/v1')