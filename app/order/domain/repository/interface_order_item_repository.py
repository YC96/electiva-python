from abc import ABC, abstractmethod
from typing import Optional
import uuid

from app.order.domain.entities.order_items import OrderItems


class IOrderItemsRepository(ABC):
    @abstractmethod
    def create(self, order_item: OrderItems) -> None:
        pass

    @abstractmethod
    def find_by_id(self, order_items_id: uuid) -> Optional[OrderItems]:
        pass

    @abstractmethod
    def find_all(self) -> list[OrderItems]:
        pass

    @abstractmethod
    def delete(self, order_items_id: uuid) -> str:
        pass

    @abstractmethod
    def update(self, order_items: OrderItems) -> OrderItems:
        pass