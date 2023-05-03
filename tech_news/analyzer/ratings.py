from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    categories = sorted([news["category"] for news in find_news()])
    top_5 = [c[0] for c in Counter(categories).most_common(5)]
    return top_5
