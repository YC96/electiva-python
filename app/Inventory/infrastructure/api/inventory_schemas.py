from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class InventoryBase(BaseModel):
    product_id: UUID
    quantity: int


class AddStockRequest(InventoryBase):
    warehouse_id: UUID  
    added_by: str  


class UpdateStockRequest(BaseModel):
    new_quantity: int 


class ProductStockResponse(BaseModel):
    product_id: UUID
    quantity: int
