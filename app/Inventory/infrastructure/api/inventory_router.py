from fastapi import APIRouter, Depends
from application.services.inventory_service import InventoryService
from infrastructure.api.inventory_schemas import AddStockRequest

router = APIRouter(prefix="/inventories", tags=["Inventory"])

@router.post("/{product_id}")
async def add_stock(product_id: str, request: AddStockRequest, service: InventoryService = Depends()):
    command = AddStockCommand(product_id=product_id, quantity=request.quantity)
    await service.add_stock(command)
    return {"message": "Stock added successfully."}
