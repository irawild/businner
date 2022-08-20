import json
from app.models.article import Article

articles_list = []

def get_all():
    articles_list = get_list()
    return_list = []
    for article in articles_list:
        return_list.append(article)
    
    return return_list
    
def get_from_type(type):
    articles_list = get_list()
    return_list = []
    for article in articles_list:
        if article['type'] == type:
            return_list.append(article)

    return return_list

def get(article_id):
    articles_list = get_list()
    for article in articles_list:
        if article['id'] == article_id:
            return article

def get_max_id() -> int:
    articles_list = get_list()
    max = 0
    if len(articles_list) > 0:
        for article in articles_list:
            if article['id'] > max:
                max = article['id']
    
    return max

def post(article_received: Article):
    articles_list = get_list()
    article_dict = {
        "id": get_max_id()+1,
        "type": article_received.type, 
        "date": article_received.date,
        "name": article_received.name,
        "call": article_received.call,
        "content": article_received.content,
        "visible": bool(article_received.visible),
    }
    articles_list.append(article_dict)
    with open('app/data/articles.json', 'w') as outfile:
        json.dump(articles_list, outfile)

    return article_dict

def delete(id: int):
    articles_list = get_list()
    return_article = None
    for article in articles_list:
        return_article = article
        if article['id'] == id:
            articles_list.remove(article)
            with open('app/data/articles.json', 'w') as outfile:
                json.dump(articles_list, outfile)
            return return_article

def put(id: int, article_received: Article):
    articles_list = get_list()
    for article in articles_list:
        if article['id'] == id:
            article['type'] = article_received.type
            article['date'] = article_received.date
            article['name'] = article_received.name
            article['call'] = article_received.call
            article['content'] = article_received.content
            article['visible'] = bool(article_received.visible)
            with open('app/data/articles.json', 'w') as outfile:
                json.dump(articles_list, outfile)
            return article

def get_list():
    with open('app/data/articles.json', 'r') as articles_file:
        json_file = json.load(articles_file)
    
    return json_file
