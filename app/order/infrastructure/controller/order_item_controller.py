
import uuid
from fastapi import APIRouter, Depends
from app.order.application.order_item_services import OrderItemService
from app.order.application.order_item_services import OrderItemService
from app.order.domain.entities.order_items import OrderItems
from app.order.infrastructure.repository.order_item_repository import SQLAlchemyOrderItemsRepository
from order.domain.entities.order import Order
from order.infrastructure.repository.order_repository import SQLAlchemyOrderRepository


router = APIRouter()

async def get_order_item_service():
    repository = SQLAlchemyOrderItemsRepository()
    return OrderItemService(repository)

@router.post("/order-item/", response_model= OrderItems)
async def add_order_item(order_items: OrderItems, order_item_service: OrderItemService = Depends(get_order_item_service)):
    return order_item_service.add_order_item(order_items)

@router.get("/order-item/", response_model=list[OrderItems])
async def get_order_items(order_item_service: OrderItemService = Depends(get_order_item_service)):
    return order_item_service.get_all_order_items()

@router.get("/order-item/{order_item_id}", response_model=OrderItems)
async def get_order_item(order_item_id: uuid, order_item_service: OrderItemService = Depends(get_order_item_service)):
    return order_item_service.get_order_item(order_item_id)

@router.put("/order-item/", response_model=OrderItems)
async def update_order_item(order_item: OrderItems, order_item_service: OrderItemService = Depends(get_order_item_service)):
    return order_item_service.update_order(order_item)

@router.delete("/order-item/{order_item_id}", response_model=OrderItems)
async def delete_order_item(order_item_id: uuid, order_item_service: OrderItemService = Depends(get_order_item_service)):
    return order_item_service.delete_order_items(order_item_id)