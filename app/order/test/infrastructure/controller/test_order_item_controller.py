import pytest
from fastapi.testclient import TestClient
from app.order.infrastructure.controller.order_item_controller import router
from app.order.application.order_item_services import OrderItemService
from app.order.domain.entities.order_items import OrderItems
from unittest.mock import MagicMock
import uuid

client = TestClient(router)

@pytest.fixture
def mock_order_item_service():
    service = MagicMock(spec=OrderItemService)
    return service

@pytest.fixture
def override_get_order_item_service(mock_order_item_service):
    async def _override_get_order_item_service():
        return mock_order_item_service
    return _override_get_order_item_service

def test_add_order_item(mock_order_item_service, override_get_order_item_service):
    order_item = OrderItems(id=uuid.uuid4(), name="Test Item", quantity=1, price=10.0)
    mock_order_item_service.add_order_item.return_value = order_item

    response = client.post("/order-item/", json=order_item.dict())
    assert response.status_code == 200
    assert response.json() == order_item.dict()

def test_get_order_items(mock_order_item_service, override_get_order_item_service):
    order_item = OrderItems(id=uuid.uuid4(), name="Test Item", quantity=1, price=10.0)
    mock_order_item_service.get_all_order_items.return_value = [order_item]

    response = client.get("/order-item/")
    assert response.status_code == 200
    assert response.json() == [order_item.dict()]

def test_get_order_item(mock_order_item_service, override_get_order_item_service):
    order_item_id = uuid.uuid4()
    order_item = OrderItems(id=order_item_id, name="Test Item", quantity=1, price=10.0)
    mock_order_item_service.get_order_item.return_value = order_item

    response = client.get(f"/order-item/{order_item_id}")
    assert response.status_code == 200
    assert response.json() == order_item.dict()

def test_update_order_item(mock_order_item_service, override_get_order_item_service):
    order_item = OrderItems(id=uuid.uuid4(), name="Updated Item", quantity=2, price=20.0)
    mock_order_item_service.update_order.return_value = order_item

    response = client.put("/order-item/", json=order_item.dict())
    assert response.status_code == 200
    assert response.json() == order_item.dict()

def test_delete_order_item(mock_order_item_service, override_get_order_item_service):
    order_item_id = uuid.uuid4()
    order_item = OrderItems(id=order_item_id, name="Test Item", quantity=1, price=10.0)
    mock_order_item_service.delete_order_items.return_value = order_item

    response = client.delete(f"/order-item/{order_item_id}")
    assert response.status_code == 200
    assert response.json() == order_item.dict()