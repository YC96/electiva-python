from abc import ABC, abstractmethod
from typing import Optional, List
from models.inventory import Inventory

class InventoryRepositoryInterface(ABC):
    @abstractmethod
    def get_stock(self, product_id: int) -> Optional[Inventory]:
        """Obtiene el inventario de un producto específico."""
        pass

    @abstractmethod
    def update_stock(self, product_id: int, new_quantity: int, warehouse_id: int) -> None:
        """Actualiza el stock de un producto."""
        pass

    @abstractmethod
    def add_stock(self, product_id: int, quantity: int, warehouse_id: int, added_by: str) -> None:
        """Agrega stock para un producto específico."""
        pass

    @abstractmethod
    def generate_report(self, start_date: str, end_date: str) -> List[Inventory]:
        """Genera un reporte del inventario entre dos fechas."""
        pass
