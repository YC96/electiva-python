from sqlmodel import SQLModel, Field, Session, select
from typing import Optional
from pydantic import BaseModel

class ProductStock(BaseModel):
    product_id: int
    total_quantity: int

class Inventory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int
    quantity: int
    warehouse_id: Optional[int]
    added_by: Optional[str]
    added_on: str

def execute_get_product_stock_query(product_id: int, session: Session) -> ProductStock:
    statement = select(Inventory).where(Inventory.product_id == product_id)
    results = session.exec(statement).all()

    if not results:
        raise ValueError(f"No stock found for product ID: {product_id}")

    total_quantity = sum(item.quantity for item in results)

    return ProductStock(product_id=product_id, total_quantity=total_quantity)
