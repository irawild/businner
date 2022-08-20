from http.client import ResponseNotReady, responses
from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel
import app.controllers.article as article
import app.controllers.article_type as article_type
from app.models.article import Article
from app.models.article_type import ArticleType
from app.pages import home

api = FastAPI()

#  Article types API
@api.get("/article-types")
def get_article_types(name: str = None):
    if name is None:
        return article_type.get_all()

    return article_type.get_from_name(name)

@api.post("/article-types")
def create_article_type(article_type_received: ArticleType):
    return article_type.create(article_type_received)

@api.delete("/article-types/{name}")
def delete_article_type(name: str):
    return article_type.delete(name)

@api.put("/article-types/{name}")
def update_article_type(name: str, article_type_received: ArticleType):
    return article_type.update(name, article_type_received)

#  Articles API
@api.get("/articles/")
def get_articles_list(type = None):
    if type is None:
        return article.get_all()
    
    return article.get_from_type(type)

@api.post("/articles/")
def post_article(article_received: Article):
    return article.post(article_received)

@api.get("/articles/{id}", response_model=Article)
def get_article(id: int = 0):
    return article.get(id)

@api.delete("/articles/{id}", response_model=Article)
def delete_article(id: int = 0):
    return article.delete(id)

@api.put("/articles/{id}", response_model=Article)
def put_article(id: int = 0, article_received: Article = None):
    return article.put(id, article_received)

# Home page
@api.get("/home", response_class=HTMLResponse)
async def get_root_page():
    return home.get_home_page_html()