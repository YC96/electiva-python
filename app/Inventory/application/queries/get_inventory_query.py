from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, Session
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

Base = declarative_base()

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    warehouse_id = Column(Integer, nullable=True)
    added_by = Column(String, nullable=True)
    added_on = Column(DateTime, default=datetime.utcnow)

class InventoryItem(BaseModel):
    id: int
    product_id: int
    quantity: int
    warehouse_id: Optional[int]
    added_by: Optional[str]
    added_on: str

def execute_get_inventory_query(session: Session) -> List[InventoryItem]:
    results = session.query(Inventory).all()

    return [
        InventoryItem(
            id=item.id,
            product_id=item.product_id,
            quantity=item.quantity,
            warehouse_id=item.warehouse_id,
            added_by=item.added_by,
            added_on=item.added_on.isoformat(),  
        )
        for item in results
    ]
