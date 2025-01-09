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

class ProductStock(BaseModel):
    product_id: int
    total_quantity: int

def execute_get_product_stock_query(product_id: int, session: Session) -> ProductStock:
    results = session.query(Inventory).filter(Inventory.product_id == product_id).all()

    if not results:
        raise ValueError(f"No stock found for product ID: {product_id}")

    total_quantity = sum(item.quantity for item in results)

    return ProductStock(product_id=product_id, total_quantity=total_quantity)
