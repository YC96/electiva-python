import unittest
from unittest.mock import MagicMock
from uuid import uuid4
from datetime import datetime
from app.products.application.services.product_service import ProductService
from app.products.domain.entities.product import Product
from app.products.domain.repositories.product_repository import ProductRepository

class TestProductService(unittest.TestCase):
    def setUp(self):
        self.mock_repository = MagicMock(spec=ProductRepository)
        self.product_service = ProductService(self.mock_repository)
        self.sample_product = Product(
            id=uuid4(),
            code="P001",
            name="Sample Product",
            description="This is a sample product",
            cost=100.0,
            margin=20.0,
            price=125.0,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

    def test_get_products(self):
        self.mock_repository.get_products.return_value = [self.sample_product]
        products = self.product_service.get_products()
        self.mock_repository.get_products.assert_called_once()
        self.assertEqual(products, [self.sample_product])

    def test_get_product(self):
        self.mock_repository.get_product.return_value = self.sample_product
        product = self.product_service.get_product(self.sample_product.id)
        self.mock_repository.get_product.assert_called_once_with(self.sample_product.id)
        self.assertEqual(product, self.sample_product)

    def test_create_product(self):
        self.mock_repository.create_product.return_value = self.sample_product
        product = self.product_service.create_product(self.sample_product)
        self.mock_repository.create_product.assert_called_once_with(self.sample_product)
        self.assertEqual(product, self.sample_product)

    def test_update_product(self):
        updated_product = self.sample_product
        updated_product.name = "Updated Product"
        self.mock_repository.update_product.return_value = updated_product
        product = self.product_service.update_product(self.sample_product.id, updated_product)
        self.mock_repository.update_product.assert_called_once_with(self.sample_product.id, updated_product)
        self.assertEqual(product.name, "Updated Product")

    def test_delete_product(self):
        self.mock_repository.delete_product.return_value = self.sample_product
        product = self.product_service.delete_product(self.sample_product.id)
        self.mock_repository.delete_product.assert_called_once_with(self.sample_product.id)
        self.assertEqual(product, self.sample_product)

if __name__ == '__main__':
    unittest.main()