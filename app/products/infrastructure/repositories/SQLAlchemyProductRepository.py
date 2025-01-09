from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from app.products.infrastructure.database.productORM import Product as ORMProduct
from app.products.infrastructure.database import schemas
from app.products.domain.entities.product import Product
from app.products.domain.repositories.product_repository import ProductRepository

class SQLAlchemyProductRepository(ProductRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_products(self, skip: int = 0, limit: int = 100) -> List[Product]:
        return self.db.query(ORMProduct).offset(skip).limit(limit).all()

    def get_product(self, product_id: UUID) -> Product:
        return self.db.query(ORMProduct).filter(ORMProduct.id == product_id).first()

    def create_product(self, product: schemas.ProductCreate) -> Product:
        db_product = ORMProduct(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def update_product(self, product_id: UUID, product: schemas.ProductUpdate) -> Product:
        db_product = self.db.query(ORMProduct).filter(ORMProduct.id == product_id).first()
        if db_product:
            for key, value in product.dict(exclude_unset=True).items():
                setattr(db_product, key, value)
            self.db.commit()
            self.db.refresh(db_product)
        return db_product

    def delete_product(self, product_id: UUID) -> Product:
        db_product = self.db.query(ORMProduct).filter(ORMProduct.id == product_id).first()
        if db_product:
            self.db.delete(db_product)
            self.db.commit()
        return db_product