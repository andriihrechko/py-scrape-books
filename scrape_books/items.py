from dataclasses import dataclass


@dataclass
class ScrapeBooksItem:
    title: str
    price: float | int
    amount_in_stock: int
    rating: int
    category: str
    description: str
    upc: str
