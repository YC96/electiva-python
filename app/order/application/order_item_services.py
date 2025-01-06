
from typing import List, Optional
import uuid
from app.order.domain.entities.order_items import OrderItems
from app.order.domain.repository.interface_order_item_repository import IOrderItemsRepository

class OrderItemService:
    def __init__(self, repository: IOrderItemsRepository):
        self.repository = repository


    def add_order_item(self, order_item: OrderItems) -> OrderItems:
        self.repository.create(order_item)
        return order_item

    def get_order_item(self, order_item_id: uuid) -> Optional[OrderItems]:
        return self.repository.find_by_id(order_item_id)
    
    def get_all_order_items(self) -> List[OrderItems]:
        return self.repository.find_all()
    
    def delete_order_items(self, order_item_id: uuid) -> Optional[OrderItems]:
        db_order = self.repository.find_by_id(order_item_id)
        if db_order:
            return self.repository.delete(db_order)
        return None
    
    def update_order(self,order_data: OrderItems) -> Optional[OrderItems]:
        return self.repository.update(order_data)
