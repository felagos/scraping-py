import requests
from bs4 import BeautifulSoup
from typing import TypedDict, Dict

domain: str = "https://books.toscrape.com/"
url_seed: str = "https://books.toscrape.com/"
urls_processed: Dict[str, bool] = {}

class BookInfo(TypedDict):
    url: str
    title: str
    in_stock: bool
    price: float

class BookData(TypedDict):
    url: str
    info: BookInfo

def get_html_parser(url: str) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def process_category_page(url: str) -> BookData:
    books_data: BookData = {}

    soup = get_html_parser(url)
    
    books_data

def load_category_urls(soup: BeautifulSoup) -> list[str]:
    url_frontier: list[str] = []

    categories = soup.find("ul", class_="nav-list").find("ul").find_all("li")
    
    for category in categories:
        url_frontier.append(f"{domain}{category.find('a').get('href')}")

    return url_frontier

def main():
    soup_main_page = get_html_parser(url_seed)

    url_categories_frontier: list[str] = load_category_urls(soup_main_page)

    for category_url in url_categories_frontier:
        if category_url not in urls_processed:
            urls_processed[category_url] = True
            process_category_page(category_url)

if __name__ == "__main__":
    main()
