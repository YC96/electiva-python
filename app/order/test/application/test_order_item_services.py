import pytest
from unittest.mock import Mock
from app.order.application.order_item_services import OrderItemService
from app.order.domain.entities.order_items import OrderItems
import uuid

@pytest.fixture
def mock_repository():
    return Mock()

@pytest.fixture
def order_item_service(mock_repository):
    return OrderItemService(mock_repository)

def test_add_order_item(order_item_service, mock_repository):
    order_item = OrderItems(id=uuid.uuid4(), name="Test Item", quantity=1, price=100)
    result = order_item_service.add_order_item(order_item)
    mock_repository.create.assert_called_once_with(order_item)
    assert result == order_item

def test_get_order_item(order_item_service, mock_repository):
    order_item_id = uuid.uuid4()
    order_item = OrderItems(id=order_item_id, name="Test Item", quantity=1, price=100)
    mock_repository.find_by_id.return_value = order_item
    result = order_item_service.get_order_item(order_item_id)
    mock_repository.find_by_id.assert_called_once_with(order_item_id)
    assert result == order_item

def test_get_all_order_items(order_item_service, mock_repository):
    order_items = [
        OrderItems(id=uuid.uuid4(), name="Test Item 1", quantity=1, price=100),
        OrderItems(id=uuid.uuid4(), name="Test Item 2", quantity=2, price=200)
    ]
    mock_repository.find_all.return_value = order_items
    result = order_item_service.get_all_order_items()
    mock_repository.find_all.assert_called_once()
    assert result == order_items

def test_delete_order_items(order_item_service, mock_repository):
    order_item_id = uuid.uuid4()
    order_item = OrderItems(id=order_item_id, name="Test Item", quantity=1, price=100)
    mock_repository.find_by_id.return_value = order_item
    mock_repository.delete.return_value = order_item
    result = order_item_service.delete_order_items(order_item_id)
    mock_repository.find_by_id.assert_called_once_with(order_item_id)
    mock_repository.delete.assert_called_once_with(order_item)
    assert result == order_item

def test_delete_order_items_not_found(order_item_service, mock_repository):
    order_item_id = uuid.uuid4()
    mock_repository.find_by_id.return_value = None
    result = order_item_service.delete_order_items(order_item_id)
    mock_repository.find_by_id.assert_called_once_with(order_item_id)
    mock_repository.delete.assert_not_called()
    assert result is None

def test_update_order(order_item_service, mock_repository):
    order_item = OrderItems(id=uuid.uuid4(), name="Updated Item", quantity=2, price=150)
    mock_repository.update.return_value = order_item
    result = order_item_service.update_order(order_item)
    mock_repository.update.assert_called_once_with(order_item)
    assert result == order_item