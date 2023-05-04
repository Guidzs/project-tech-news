import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category)


# Requisitos 11 e 12
def analyzer_menu():
    num = input(
        """Selecione uma das opções a seguir:
        0 - Popular o banco com notícias;
        1 - Buscar notícias por título;
        2 - Buscar notícias por data;
        3 - Buscar notícias por categoria;
        4 - Listar top 5 categorias;
        5 - Sair."""
    )

    if num == '0':
        get_tech_news(int(input("Digite quantas notícias serão buscadas:")))
    elif num == '1':
        r = search_by_title(input("Digite o título:"))
        print(r)
    elif num == '2':
        r = search_by_date(input("Digite a data no formato aaaa-mm-dd:"))
        print(r)
    elif num == '3':
        r = search_by_category(input("Digite a categoria:"))
        print(r)
    elif num == '4':
        r = top_5_categories()
        print(r)
    elif num == '5':
        r = "Encerrando script"
        return print(r)
    else:
        return print("Opção inválida", file=sys.stderr)
