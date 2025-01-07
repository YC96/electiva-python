from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class InventoryBase(BaseModel):
    product_id: UUID
    quantity: int


class InventoryCreateRequest(InventoryBase):
    pass


class InventoryUpdateRequest(BaseModel):
    quantity: int


class InventoryResponse(InventoryBase):
    id: UUID
    created_at: datetime
    updated_at: datetime | None
