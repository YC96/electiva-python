from app.common.database.postgresql import get_db
from fastapi import APIRouter, HTTPException, Depends
from uuid import UUID
from sqlalchemy.orm import Session
from application.commands.add_stock_command import AddStockCommand
from application.commands.update_stock_command import UpdateStockCommand
from application.queries.get_product_stock_query import GetProductStockQuery
from application.services.inventory_service import InventoryService
from api.inventory_schemas import AddStockRequest, UpdateStockRequest, ProductStockResponse
    

router = APIRouter()

def get_inventory_service(db: Session = Depends(get_db)) -> InventoryService:
    return InventoryService(db)

@router.get("/inventories/{product_id}", response_model=ProductStockResponse)
async def get_product_stock(
    product_id: UUID,
    inventory_service: InventoryService = Depends(get_inventory_service),
):
    """
    Obtiene la cantidad en inventario de un producto.
    """
    try:
        product_stock = inventory_service.get_product_stock(product_id)
        return ProductStockResponse(product_id=product_id, quantity=product_stock)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Producto no encontrado: {str(e)}")

@router.post("/inventories/{product_id}")
async def add_product_stock(
    product_id: UUID,
    request: AddStockRequest,
    inventory_service: InventoryService = Depends(),
):
    """
    Agrega productos al inventario.
    """
    try:
        command = AddStockCommand(
            product_id=product_id,
            quantity=request.quantity
        )
        await inventory_service.add_stock(command)
        return {"message": "Stock agregado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al agregar stock: {str(e)}")


@router.put("/inventories/{product_id}")
async def update_product_stock(
    product_id: UUID,
    request: UpdateStockRequest,
    inventory_service: InventoryService = Depends(),
):
    """
    Actualiza la cantidad en inventario de un producto.
    """
    try:
        command = UpdateStockCommand(
            product_id=product_id,
            new_quantity=request.new_quantity
        )
        await inventory_service.update_stock(command)
        return {"message": "Stock actualizado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al actualizar stock: {str(e)}")
