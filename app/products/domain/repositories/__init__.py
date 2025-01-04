from typing import List
from uuid import UUID
from app.products.domain.entities.product import Product

class ProductRepository:
    def get_products(self, skip: int = 0, limit: int = 100) -> List[Product]:
        raise NotImplementedError

    def get_product(self, product_id: UUID) -> Product:
        raise NotImplementedError

    def create_product(self, product: Product) -> Product:
        raise NotImplementedError

    def update_product(self, product_id: UUID, product: Product) -> Product:
        raise NotImplementedError

    def delete_product(self, product_id: UUID) -> Product:
        raise NotImplementedError