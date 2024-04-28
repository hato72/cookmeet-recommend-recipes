import os
from dotenv import load_dotenv

load_dotenv()

RAKUTEN_APPLICATION_ID = os.getenv('RAKUTEN_APPLICATION_ID')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
REDISHOST = os.getenv('REDISHOST', 'redis')
REDISPORT = int(os.getenv('REDISPORT', 6379))
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:3000')

