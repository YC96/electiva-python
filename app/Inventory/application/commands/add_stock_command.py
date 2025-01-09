from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from models import Base  

class AddStockCommand(BaseModel):
    product_id: int
    quantity: int
    warehouse_id: Optional[int] = None
    added_by: Optional[str] = None

class Inventory(Base):
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    quantity = Column(Integer)
    warehouse_id = Column(Integer, nullable=True)
    added_by = Column(String, nullable=True)
    added_on = Column(DateTime, default=datetime.utcnow)

def execute_add_stock_command(command: AddStockCommand, session: Session):
    stock_entry = Inventory(
        product_id=command.product_id,
        quantity=command.quantity,
        warehouse_id=command.warehouse_id,
        added_by=command.added_by,
        added_on=datetime.utcnow()  
    )
    session.add(stock_entry)
    session.commit()
    session.refresh(stock_entry)
    return stock_entry
