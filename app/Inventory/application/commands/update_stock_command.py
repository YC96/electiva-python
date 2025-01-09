from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, Session
from pydantic import BaseModel
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

class UpdateStockCommand(BaseModel):
    inventory_id: int
    quantity: int

def execute_update_stock_command(command: UpdateStockCommand, session: Session):
    inventory_item = session.query(Inventory).filter(Inventory.id == command.inventory_id).first()

    if not inventory_item:
        raise ValueError("Inventory item not found")

    inventory_item.quantity = command.quantity

    session.commit()

    session.refresh(inventory_item)

    return inventory_item
