import requests
from bs4 import BeautifulSoup

domain: str = "https://books.toscrape.com/"
url_seed: str = "https://books.toscrape.com/"

def get_html_parser(url: str) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def process_category_page(url: str) -> None:
    pass

def load_category_urls(soup: BeautifulSoup) -> list[str]:
    url_frontier: list[str] = []

    categories = soup.find("ul", class_="nav-list").find("ul").find_all("li")
    
    for category in categories:
        url_frontier.append(f"{domain}{category.find('a').get('href')}")

    return url_frontier

def main():
    soup_main_page = get_html_parser(url_seed)

    url_frontier: list[str] = load_category_urls(soup_main_page)



if __name__ == "__main__":
    main()