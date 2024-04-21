import os
from dotenv import load_dotenv

load_dotenv()

RAKUTEN_APPLICATION_ID = os.getenv('RAKUTEN_APPLICATION_ID')
print (RAKUTEN_APPLICATION_ID)

