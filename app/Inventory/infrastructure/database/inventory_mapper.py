from domain.models.inventory import Inventory as DomainInventory
from domain.models.inventory import Inventory as ORMInventory
from infrastructure.api.inventory_schemas import InventoryResponse


class InventoryMapper:
    @staticmethod
    def to_domain(orm_inventory: ORMInventory) -> DomainInventory:
        return DomainInventory(
            id=orm_inventory.id,
            product_id=orm_inventory.product_id,
            quantity=orm_inventory.quantity,
            created_at=orm_inventory.created_at,
            updated_at=orm_inventory.updated_at,
        )

    @staticmethod
    def to_orm(domain_inventory: DomainInventory) -> ORMInventory:
        return ORMInventory(
            id=domain_inventory.id,
            product_id=domain_inventory.product_id,
            quantity=domain_inventory.quantity,
            created_at=domain_inventory.created_at,
            updated_at=domain_inventory.updated_at,
        )

    @staticmethod
    def to_response(orm_inventory: ORMInventory) -> InventoryResponse:
        return InventoryResponse(
            id=orm_inventory.id,
            product_id=orm_inventory.product_id,
            quantity=orm_inventory.quantity,
            created_at=orm_inventory.created_at,
            updated_at=orm_inventory.updated_at,
        )
