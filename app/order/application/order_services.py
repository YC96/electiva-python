
from typing import List, Optional
import uuid
from app.order.domain.entities.order import Order
from app.order.domain.repository.interface_order_repository import IOrderRepository

class OrderService:
    def __init__(self, repository: IOrderRepository):
        self.repository = repository


    def add_order(self, order: Order) -> Order:
        self.repository.create(order)
        return order

    def get_order(self, order_id: uuid) -> Optional[Order]:
        return self.repository.find_by_id(order_id)
    
    def get_all_orders(self) -> List[Order]:
        return self.repository.find_all()
    
    def delete_order(self, order_id: uuid) -> Optional[Order]:
        db_order = self.repository.find_by_id(order_id)
        if db_order:
            return self.repository.delete(db_order)
        return None
    
    def update_order(self,order_data: Order) -> Optional[Order]:
        return self.repository.update(order_data)
