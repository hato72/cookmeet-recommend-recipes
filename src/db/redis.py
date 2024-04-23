import redis
from pydantic import BaseModel
import redis.client

class RedisClient(BaseModel):
    host: str
    port: int
    db: int
    connection: redis.client.Redis | None = None
    
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        self.host = host
        self.port = port
        self.db = db
        
    def connect(self):
        self.connection = redis.Redis(host=self.host, port=self.port, db=self.db, decode_responses=True)
        
    def get_connection(self):
        if not self.connection:
            self.connect()
        
        return self.connection