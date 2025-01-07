from sqlmodel import SQLModel, Field, Session, select
from typing import List, Optional
from pydantic import BaseModel

class InventoryItem(BaseModel):
    id: int
    product_id: int
    quantity: int
    warehouse_id: Optional[int]
    added_by: Optional[str]
    added_on: str

class Inventory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int
    quantity: int
    warehouse_id: Optional[int]
    added_by: Optional[str]
    added_on: str

def execute_get_inventory_query(session: Session) -> List[InventoryItem]:
    statement = select(Inventory)
    results = session.exec(statement).all()

    return [
        InventoryItem(
            id=item.id,
            product_id=item.product_id,
            quantity=item.quantity,
            warehouse_id=item.warehouse_id,
            added_by=item.added_by,
            added_on=item.added_on,
        )
        for item in results
    ]
