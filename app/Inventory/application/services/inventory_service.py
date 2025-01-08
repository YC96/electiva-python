from sqlmodel import Session
from fastapi import Depends
from typing import List
from queries.get_inventory_query import execute_get_inventory_query
from queries.get_product_stock_query import execute_get_product_stock_query
from commands.add_stock_command import execute_add_stock_command
from commands.update_stock_command import execute_update_stock_command
from domain.models.inventory import Inventory
from infrastructure.database.db_config import get_db

class InventoryService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_inventory(self) -> List[Inventory]:
        return execute_get_inventory_query(self.session)

    def get_product_stock(self, product_id: int) -> int:
        product_stock = execute_get_product_stock_query(product_id, self.session)
        return product_stock.total_quantity

    def add_stock(self, product_id: int, quantity: int, warehouse_id: int, added_by: str) -> None:
        execute_add_stock_command(
            product_id=product_id,
            quantity=quantity,
            warehouse_id=warehouse_id,
            added_by=added_by,
            session=self.session
        )

    def update_stock(self, product_id: int, new_quantity: int, warehouse_id: int) -> None:
        execute_update_stock_command(
            product_id=product_id,
            new_quantity=new_quantity,
            warehouse_id=warehouse_id,
            session=self.session
        )
