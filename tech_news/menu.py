import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category)


def exit():
    return ("Encerrando script")


def execute_action(num: str):
    actions = {
        '0': get_tech_news,
        '1': search_by_title,
        '2': search_by_date,
        '3': search_by_category,
        '4': top_5_categories,
        '5': exit
    }
    questions = {
        '1': "Digite o título:",
        '2': "Digite a data no formato aaaa-mm-dd:",
        '3': "Digite a categoria:",
    }

    if num in questions:
        param = input(questions[num])
        print(actions[num](param))
    elif num == '0':
        param = int(input("Digite quantas notícias serão buscadas:"))
        print(actions[num](param))
    else:
        print(actions[num]())


# Requisitos 11 e 12
def analyzer_menu():
    num = input(
        """Selecione uma das opções a seguir:
        0 - Popular o banco com notícias;
        1 - Buscar notícias por título;
        2 - Buscar notícias por data;
        3 - Buscar notícias por categoria;
        4 - Listar top 5 categorias;
        5 - Sair.
        """
    )
    options = ['0', '1', '2', '3', '4', '5']

    if num in options:
        execute_action(num)
    else:
        return print("Opção inválida", file=sys.stderr)
