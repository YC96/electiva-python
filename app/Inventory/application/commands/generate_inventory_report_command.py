from sqlmodel import SQLModel, Field, Session, select
from typing import List, Optional
from pydantic import BaseModel

class InventoryReport(BaseModel):
    product_id: int
    total_quantity: int

class Inventory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int
    quantity: int
    warehouse_id: Optional[int]
    added_by: Optional[str]
    added_on: datetime

def execute_generate_inventory_report_command(session: Session) -> List[InventoryReport]:
    statement = select(Inventory.product_id, Inventory.quantity)
    results = session.exec(statement).all()

    report = {}
    for result in results:
        if result.product_id not in report:
            report[result.product_id] = 0
        report[result.product_id] += result.quantity

    return [InventoryReport(product_id=pid, total_quantity=qty) for pid, qty in report.items()]
