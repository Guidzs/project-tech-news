# Tech News

> Este projeto é uma raspagem de dados no site [betrybe](https://blog.betrybe.com) 

Este projeto foi idealizado pela [Trybe](https://www.betrybe.com) com o objetivo de trabalhar e exercitar tecnologias como `MongoDB` e `BeautifulSoup`
e trabalhando com coleta de dados na web e preenchimento em um banco de dados `NoSQL` chamado `tech_news`

this project was conceived by [Trybe](https://www.betrybe.com) with the objective of working and exercising technologies such as `MongoDB` and `BeautifulSoup`
and working with scraping data on the web and populating it in a `NoSQL` database called `tech_news`

## Pré-Requisitos

- `git commands`
- `python`

## Instalando a Aplicação

```bash
# Clone este repositório
$ git clone git@github.com:Guidzs/project-tech-news.git

# Acesse a pasta do projeto no terminal/cmd
$ cd project-tech-news

# Rode esses comandos para entrar em abientre virtual e baixar as dependecias
$ python3 -m venv .venv && source .venv/bin/activate
$ python3 -m pip install -r dev-requirements.txt

``````
## Subindo o banco de dados com Docker-Compose `OPCIONAL`
É importante garantir que não haja conteineres abertos que possam entrar em conflito com a aplicação

```bash
# Instale o ambiente para a aplicação
$ docker-compoSse up -d --build

# Chame a função para popular o banco
$ tech-news-analyzer
$ digite a opção -0
$ siga os prompts para adicionar as notícias
```

## Como Usar

* Para etrar na interface da aplicação rode os comandos `python3 -i tech_news/menu.py` and `analyzer_menu()`


## Test

### Dentro do ambientre python execute o comando:
* run `python3 -m pytest`

### funcionalidades
=================
<!--ts-->
    [0 - Popular o banco com notícias](#Popular o banco com notícias)
        [Digite quantas notícias serão buscadas](#Digite quantas notícias serão buscadas)

    [1 - Buscar notícias por título](#A pesquisa não diferencia Maiúscula de Minúscula)
    [2 - Buscar notícias por data](#A data inserida tem que estar no formato ano-mes-dias)
    [3 - Buscar notícias por categoria](#)

    [4 - Listar top 5 categorias](#Exemplo de resposta: ['Tecnologia', 'Desenvolvimento Web', 'Carreira', 'Linguagem de Programação'])

    [5 - Selecione para sair da interface](#)
<!--te-->

## Contribution

Alguns arquivos foram feitos pelo Trybe como base do projeto:
<!--ts-->
    * tech_news/analyzer/reading_plan.py
    * tech_news/database.py
    * .editorconfig
    * .gitignore
    * dev-requirements.txt
    * docker-compose.yml
    * Dockerfile
    * pyproject.toml
    * requirements.txt
    * setup.cfg
    * setup.py
<!--te-->

## Contact

- [Guilherme Borges](https://www.linkedin.com/in/guidzsBorges/)
- E-mail: guidz.2004@gmail.com
