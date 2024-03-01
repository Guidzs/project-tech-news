# Tech News

> this project is a data scraping on the website [betrybe](https://blog.betrybe.com)

this project was conceived by [Trybe](https://www.betrybe.com) with the objective of working and exercising technologies such as MongoDB and BeautifulSoup
and working with scraping data on the web and populating it in a NoSQL database called tech_news

## Prerequisites

- `git commands`
- `python`

## Install

- `git clone git@github.com:Guidzs/project-tech-news.git`
- `cd project-tech-news`
- `python3 -m venv .venv && source .venv/bin/activate`
- `python3 -m pip install -r dev-requirements.txt`

## Use

*run the aplication with `python3 -i tech_news/menu.py` and `analyzer_menu()`

## Running with Docker-Compose

-`docker-compose up -d --build`

-`ensure that there are no open containers that could conflict with the application`

## Test

*run `python3 -m pytest`

## Resources

- type 0 to populate the database
   \ inform the amount of news that will be searched
- type 1 to search news by title
- type 2 to search for news by date
- type 3 to search for news by category
- type 4 to search the top 5 categories
- type 5 to exit

## Contribution

some files were made by Trybe like:
    tech_news/analyzer/reading_plan.py
    tech_news/database.py
    .editorconfig
    .gitignore
    dev-requirements.txt
    docker-compose.yml
    Dockerfile
    pyproject.toml
    requirements.txt
    setup.cfg
    setup.py

## Contact

- author's name: [Guilherme Borges](https://www.linkedin.com/in/guidzsBorges/)
- E-mail: guidz.2004@gmail.com
