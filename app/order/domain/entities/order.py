import datetime
import uuid
from pydantic import BaseModel, Field
from app.order.domain.entities.order_items import OrderItems
from app.order.domain.enum.order_status import OrderStatus


class Order(BaseModel):
    id: uuid.UUID = Field(...)
    user_id: uuid.UUID = Field(...)
    created_at: str = Field(..., default_factory=datetime.datetime.now)
    updated_at: str
    total_amount: float = Field(..., gt=0)
    status: OrderStatus = Field(...)