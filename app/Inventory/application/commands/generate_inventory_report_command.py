from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.sql import select
from typing import List
from datetime import datetime
from pydantic import BaseModel

Base = declarative_base()

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    warehouse_id = Column(Integer, nullable=True)
    added_by = Column(String, nullable=True)
    added_on = Column(DateTime, default=datetime.utcnow)

class InventoryReport(BaseModel):
    product_id: int
    total_quantity: int

def execute_generate_inventory_report_command(session: Session) -> List[InventoryReport]:
    statement = (
        select(Inventory.product_id, func.sum(Inventory.quantity).label("total_quantity"))
        .group_by(Inventory.product_id)
    )
    results = session.execute(statement).fetchall()

    report = [
        InventoryReport(product_id=row.product_id, total_quantity=row.total_quantity)
        for row in results
    ]
    return report
