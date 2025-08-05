import requests
from bs4 import BeautifulSoup
from typing import TypedDict, Dict

domain: str = "https://books.toscrape.com/"
url_seed: str = "https://books.toscrape.com/"
urls_processed: Dict[str, bool] = {}
books_processed: Dict[str, bool] = {}


class BookInfo(TypedDict):
    url: str
    title: str
    in_stock: bool
    price: float
    stars: int


class BookData(TypedDict):
    url: str
    info: BookInfo


star_mapping = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def get_html_parser(url: str) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def process_category_page(url: str) -> BookData:
    books_data: BookData = {}
    books_info = []

    soup = get_html_parser(url)
    books_container = (
        soup.find("section")
        .find("ol", class_="row")
        .find_all("article", class_="product_pod")
    )

    for book in books_container:
        book_url = book.find("h3").find("a").get("href")

        if book_url in books_processed:
            continue

        stars_class = book.find("p", class_="star-rating").get("class")[1]
        stars = star_mapping[stars_class]
        in_stock = (
            book.find("p", class_="instock availability").text.strip() == "In stock"
        )
        price = book.find("p", class_="price_color").text.strip()
        title = book.find("h3").find("a").get("title")

        books_info.append(
            BookInfo(
                url=f"{domain}{book_url}",
                title=title,
                in_stock=in_stock,
                price=price,
                stars=stars,
            )
        )

    books_data["url"] = url
    books_data["info"] = books_info
    return books_data


def load_category_urls(soup: BeautifulSoup) -> list[str]:
    url_frontier: list[str] = []

    categories = soup.find("ul", class_="nav-list").find("ul").find_all("li")

    for category in categories:
        url_frontier.append(f"{domain}{category.find('a').get('href')}")

    return url_frontier


def main():
    data_processed: BookData = []
    soup_main_page = get_html_parser(url_seed)

    url_categories_frontier: list[str] = load_category_urls(soup_main_page)

    for category_url in url_categories_frontier:
        if category_url not in urls_processed:
            urls_processed[category_url] = True
            data = process_category_page(category_url)
            data_processed.append(data)

    print(
        f"Processed {len(data_processed)} categories with {sum(len(d['info']) for d in data_processed)} books."
    )


if __name__ == "__main__":
    main()
