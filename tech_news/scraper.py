import time
import requests

from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    url_news = []

    soup = BeautifulSoup(html_content, "html.parser")

    news = soup.find_all("h2", {"class": "entry-title"})
    for new in news:
        a = new.find('a')
        url = a.get('href')
        url_news.append(url)
    return url_news


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    try:
        new_page = soup.find("a", {"class": "next page-numbers"})
        url = new_page.get('href')
        return url
    except AttributeError:
        return None


# Requisito 4
def scrape_news(html_content):
    # soup = BeautifulSoup(html_content, "html.parser")
    # news = soup.find_all("div", {"class": "post-outer"})

    # for new in news:
    #     title_new = new.find("h2", {"class": "entry-title"})
    #     infos_new = new.find("ul", {"class": "post-meta"})
    #     writer_new = infos_new.find("span", {"class": "author"})

    #     url = title_new.find("a").get('href')
    #     title = title_new.get_text()
    #     timestamp = infos_new.find("li", {"class": "meta-date"}).get_text()
    #     writer = writer_new.find("a").get_text()
    #     reading_time = new.find("li", {"class": "meta-reading-time"})
    ...


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
