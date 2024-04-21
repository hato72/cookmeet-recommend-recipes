from pydantic import BaseModel

class RecommendRequestBody(BaseModel):
    texts: list[str]
    conditions: list[str]