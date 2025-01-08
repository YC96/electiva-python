from pydantic import BaseModel, validator
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class ProductBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    cost: float
    margin: float

    @validator('margin')
    def validate_margin(cls, v):
        if v <= 0 or v >= 100:
            raise ValueError('Margin must be between 0 and 100 (exclusive)')
        return v

    @property
    def price(self) -> float:
        return round(self.cost / (1 - self.margin / 100), 2)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    price: float

    class Config:
        orm_mode = True

class ProductList(BaseModel):
    products: List[ProductCreate]