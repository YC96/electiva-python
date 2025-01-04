from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from app.products.infrastructure.database import schemas
from app.products.infrastructure.database.database import SessionLocal
from app.products.application.services.product_service import ProductService
from app.products.infrastructure.repositories.SQLAlchemyProductRepository import SQLAlchemyProductRepository

controller = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_product_service(db: Session = Depends(get_db)):
    repository = SQLAlchemyProductRepository(db)
    return ProductService(repository)

@controller.get("/products", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, service: ProductService = Depends(get_product_service)):
    return service.get_products(skip, limit)

@controller.post("/products/bulk", response_model=List[schemas.Product])
def create_products(products: schemas.ProductList, service: ProductService = Depends(get_product_service)):
    created_products = []
    for product in products.products:
        created_product = service.create_product(product)
        created_products.append(created_product)
    return created_products

@controller.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: UUID, service: ProductService = Depends(get_product_service)):
    product = service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@controller.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, service: ProductService = Depends(get_product_service)):
    return service.create_product(product)

@controller.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: UUID, product: schemas.ProductUpdate, service: ProductService = Depends(get_product_service)):
    return service.update_product(product_id, product)

@controller.delete("/products/{product_id}", response_model=schemas.Product)
def delete_product(product_id: UUID, service: ProductService = Depends(get_product_service)):
    return service.delete_product(product_id)