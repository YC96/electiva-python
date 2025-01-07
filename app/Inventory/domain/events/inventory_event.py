from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class InventoryEvent(BaseModel):
    event_type: str  # "ADD_STOCK" o "UPDATE_STOCK"
    product_id: int
    warehouse_id: int
    quantity: int
    timestamp: datetime
    triggered_by: Optional[str] = None  # Usuario que realiza la acción
