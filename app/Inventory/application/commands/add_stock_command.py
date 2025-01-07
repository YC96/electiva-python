from sqlmodel import SQLModel, Field, Session
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AddStockCommand(BaseModel):
    product_id: int
    quantity: int
    warehouse_id: Optional[int] = None
    added_by: Optional[str] = None

class Inventory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int
    quantity: int
    warehouse_id: Optional[int]
    added_by: Optional[str]
    added_on: datetime = Field(default_factory=datetime.utcnow)

def execute_add_stock_command(command: AddStockCommand, session: Session):
    stock_entry = Inventory(
        product_id=command.product_id,
        quantity=command.quantity,
        warehouse_id=command.warehouse_id,
        added_by=command.added_by
    )
    session.add(stock_entry)
    session.commit()
    session.refresh(stock_entry)
    return stock_entry
