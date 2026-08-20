from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Product:
    title: str
    asin: str
    price: float
    monthly_sales: float
    monthly_revenue: float
    reviews: int
    rating: float

class DataProvider:
    """Interface for authorized Amazon/third-party data providers."""
    def search_products(self, query: str, marketplace: str) -> list[Product]:
        raise NotImplementedError

class DemoProvider(DataProvider):
    def search_products(self, query: str, marketplace: str) -> list[Product]:
        return [
            Product(f"{query.title()} Organizer", "DEMO-001", 29.99, 420, 12595.8, 186, 4.4),
            Product(f"{query.title()} Storage Rack", "DEMO-002", 34.99, 310, 10846.9, 92, 4.5),
            Product(f"{query.title()} Holder", "DEMO-003", 21.99, 680, 14953.2, 421, 4.3),
        ]
