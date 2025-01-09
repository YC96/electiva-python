from typing import List
from uuid import UUID
from app.products.domain.entities.product import Product
from app.products.domain.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_products(self, skip: int = 0, limit: int = 100) -> List[Product]:
        return self.repository.get_products(skip, limit)

    def get_product(self, product_id: UUID) -> Product:
        return self.repository.get_product(product_id)

    def create_product(self, product: Product) -> Product:
        return self.repository.create_product(product)

    def update_product(self, product_id: UUID, product: Product) -> Product:
        return self.repository.update_product(product_id, product)

    def delete_product(self, product_id: UUID) -> Product:
        return self.repository.delete_product(product_id)