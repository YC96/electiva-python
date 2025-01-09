import pytest
from fastapi.testclient import TestClient
from app.order.infrastructure.controller.order_controller import router
from app.order.application.order_services import OrderService
from app.order.domain.entities.order import Order
from app.order.infrastructure.repository.order_repository import SQLAlchemyOrderRepository
from unittest.mock import AsyncMock, patch
import uuid

client = TestClient(router)

@pytest.fixture
def mock_order_service():
    with patch('app.order.infrastructure.controller.order_controller.get_order_service', new_callable=AsyncMock) as mock:
        yield mock

def test_add_order(mock_order_service):
    order_data = {"id": str(uuid.uuid4()), "name": "Test Order"}
    mock_order_service.return_value.add_order.return_value = Order(**order_data)
    
    response = client.post("/order/", json=order_data)
    
    assert response.status_code == 200
    assert response.json() == order_data

def test_get_orders(mock_order_service):
    order_data = [{"id": str(uuid.uuid4()), "name": "Test Order"}]
    mock_order_service.return_value.get_all_orders.return_value = [Order(**order_data[0])]
    
    response = client.get("/order/")
    
    assert response.status_code == 200
    assert response.json() == order_data

def test_get_order(mock_order_service):
    order_id = str(uuid.uuid4())
    order_data = {"id": order_id, "name": "Test Order"}
    mock_order_service.return_value.get_order.return_value = Order(**order_data)
    
    response = client.get(f"/order/{order_id}")
    
    assert response.status_code == 200
    assert response.json() == order_data

def test_update_order(mock_order_service):
    order_data = {"id": str(uuid.uuid4()), "name": "Updated Order"}
    mock_order_service.return_value.update_order.return_value = Order(**order_data)
    
    response = client.put("/order/", json=order_data)
    
    assert response.status_code == 200
    assert response.json() == order_data

def test_delete_order(mock_order_service):
    order_id = str(uuid.uuid4())
    order_data = {"id": order_id, "name": "Deleted Order"}
    mock_order_service.return_value.delete_order.return_value = Order(**order_data)
    
    response = client.delete(f"/order/{order_id}")
    
    assert response.status_code == 200
    assert response.json() == order_data