from models.article_type import ArticleType
from typing import Union
import json

def get_list():
    with open('data/article_types.json', 'r') as types_file:
        json_file = json.load(types_file)
    
    return json_file

def get_all():
    types_list = get_list()
    return_list = []
    for article_type in types_list:
        return_list.append(article_type)
    
    return return_list

def get_from_name(name: str) -> Union[ArticleType, None]:
    types_list = get_list()
    for article_type in types_list:
        if article_type['name'] == name:
            return article_type
    
    return None

def create(article_type_received: ArticleType) -> Union[ArticleType, None]:
    types_list = get_list()
    for article_type in types_list:
        if article_type['name'] == article_type_received.name:
            return None

    article_type_dict = {
        "name": article_type_received.name,
        "description": article_type_received.description, 
    }
    types_list.append(article_type_dict)
    with open('data/article_types.json', 'w') as outfile:
        json.dump(types_list, outfile)
    
    return article_type_dict

def delete(name: str) -> Union[ArticleType, None]:
    types_list = get_list()
    return_article = None
    for article_type in types_list:
        return_article = article_type
        if article_type['name'] == name:
            types_list.remove(article_type)
            with open('data/article_types.json', 'w') as outfile:
                json.dump(types_list, outfile)
            return return_article
    
    return None

def update(name: str, article_received: ArticleType) -> Union[ArticleType, None]:
    types_list = get_list()
    for article_type in types_list:
        if article_type['name'] == name:
            article_type['description'] = article_received.description
            with open('data/article_types.json', 'w') as outfile:
                json.dump(types_list, outfile)
            return article_received
    
    return None