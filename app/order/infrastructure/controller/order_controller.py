
import uuid
from fastapi import APIRouter, Depends
from app.order.application.order_services import OrderService
from order.domain.entities.order import Order
from order.infrastructure.repository.order_repository import SQLAlchemyOrderRepository


router = APIRouter()

async def get_order_service():
    repository = SQLAlchemyOrderRepository()
    return OrderService(repository)

@router.post("/order/", response_model= Order)
async def add_order(order: Order, order_service: OrderService = Depends(get_order_service)):
    return order_service.add_order(Order)

@router.get("/order/", response_model=list[Order])
async def get_orders(order_service: OrderService = Depends(get_order_service)):
    return order_service.get_all_orders()

@router.get("/order/{order_id}", response_model=Order)
async def get_order(order_id: uuid, order_service: OrderService = Depends(get_order_service)):
    return order_service.get_order(order_id)

@router.put("/order/", response_model=Order)
async def update_order(order: Order, order_service: OrderService = Depends(get_order_service)):
    return order_service.update_order(order)

@router.delete("/order/{order_id}", response_model=Order)
async def delete_order(order_id: uuid, order_service: OrderService = Depends(get_order_service)):
    return order_service.delete_order(order_id)