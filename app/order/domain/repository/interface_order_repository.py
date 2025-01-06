from abc import ABC, abstractmethod
from typing import Optional
import uuid

from order.domain.entities.order import Order


class IOrderRepository(ABC):
    @abstractmethod
    def create(self, order: Order) -> None:
        pass

    @abstractmethod
    def find_by_id(self, order_id: uuid) -> Optional[Order]:
        pass

    @abstractmethod
    def find_all(self) -> list[Order]:
        pass

    @abstractmethod
    def delete(self, order_id: uuid) -> str:
        pass

    @abstractmethod
    def update(self, order: Order) -> Order:
        pass