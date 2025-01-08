from uuid import UUID
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field

class Product(BaseModel):
    id: UUID
    code: str = Field(..., min_length=5, max_length=5, description="The code must be 5 characters long")
    name: str = Field(..., min_length=3, max_length=30, description="The name must be between 3 and 30 characters long")
    description: str = Field(None, max_length=150, description="The description must be up to 150 characters long")
    cost: Decimal = Field(..., gt=0, description="The cost must be greater than 0")
    margin: Decimal = Field(..., gt=0, description="The margin must be greater than 0")
    price: Decimal = Field(..., gt=0, description="The price must be greater than 0")
    created_at: datetime
    updated_at: datetime