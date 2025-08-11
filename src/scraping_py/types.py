from typing import TypedDict, List

class BookInfo(TypedDict):
    url: str
    title: str
    in_stock: bool
    price: float
    stars: int


class BookData(TypedDict):
    url: str
    info: List[BookInfo]
