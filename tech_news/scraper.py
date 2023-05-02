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
    soup = BeautifulSoup(html_content, "html.parser")

    new_infos = soup.find("div", {"class": "entry-header-inner"})
    new_content = soup.find("div", {"class": "entry-content"})

    category_span = new_infos.find("div", {"class": "meta-category"})
    writer_new = new_infos.find("span", {"class": "author"})

    return {
        "url": soup.find('link', {"rel": 'canonical'}).get('href'),
        "title": new_infos.find("h1", {"class": "entry-title"}).string.strip(),
        "timestamp": new_infos.find("li", {"class": "meta-date"}).string,
        "writer": writer_new.find("a").string,
        "reading_time": int(
            new_infos.find("li", {"class": "meta-reading-time"}).text[0:2]),
        "summary": "".join(new_content.p.text).strip(),
        "category": category_span.find("span", {"class": "label"}).string,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
