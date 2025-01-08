from sqlmodel import SQLModel, Field, Session, select
from typing import Optional
from pydantic import BaseModel

class UpdateStockCommand(BaseModel):
    inventory_id: int
    quantity: int

class Inventory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int
    quantity: int
    warehouse_id: Optional[int]
    added_by: Optional[str]
    added_on: datetime

def execute_update_stock_command(command: UpdateStockCommand, session: Session):
    statement = select(Inventory).where(Inventory.id == command.inventory_id)
    result = session.exec(statement).first()

    if not result:
        raise ValueError("Inventory item not found")
    
    result.quantity = command.quantity
    session.add(result)
    session.commit()
    session.refresh(result)
    return result
