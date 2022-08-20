from pydantic import BaseModel

class ArticleType(BaseModel):
    name: str
    description: str
