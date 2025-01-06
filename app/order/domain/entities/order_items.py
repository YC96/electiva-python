import uuid

from pydantic import BaseModel, Field
from order.domain.enum.order_status import OrderStatus


class OrderItems(BaseModel):
    id: uuid.UUID = Field(...)
    order_id: uuid.UUID = Field(...)
    product_id: uuid.UUID = Field(...)
    quantity: int = Field(...)