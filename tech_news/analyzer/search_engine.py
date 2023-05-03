from datetime import datetime
from ..database import db


# Requisito 7
def search_by_title(title):
    news = db.news.find(
        {
            'title': {
                '$regex': title, '$options': 'i'
            }})
    return [(new['title'], new['url']) for new in news]


# Requisito 8
def search_by_date(date):
    try:
        date_format = datetime.strptime(
            date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news = db.news.find({'timestamp': date_format})
        return [(new['title'], new['url']) for new in news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    news = db.news.find(
        {
            'category': {
                '$regex': category, '$options': 'i'
            }})
    return [(new['title'], new['url']) for new in news]
