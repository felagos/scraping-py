import requests
from bs4 import BeautifulSoup


def process_category_page(url: str) -> None:
    pass


if __name__ == "__main__":
    domain: str = "https://books.toscrape.com/"

    url_seed: str = "https://books.toscrape.com/"
    url_frontier: list[str] = []

    response = requests.get(url_seed)
    soup = BeautifulSoup(response.content, "html.parser")

    categories = soup.find("ul", class_="nav-list").find("ul").find_all("li")
    for category in categories:
        url_frontier.append(f"{domain}{category.find('a').get('href')}")