import pytest
import uuid
from unittest.mock import Mock
from app.order.domain.entities.order import Order
from app.order.domain.repository.interface_order_repository import IOrderRepository
from app.order.application.order_services import OrderService

@pytest.fixture
def mock_repository():
    return Mock(spec=IOrderRepository)

@pytest.fixture
def order_service(mock_repository):
    return OrderService(repository=mock_repository)

def test_add_order(order_service, mock_repository):
    order = Order(id=uuid.uuid4(), name="Test Order")
    result = order_service.add_order(order)
    mock_repository.create.assert_called_once_with(order)
    assert result == order

def test_get_order(order_service, mock_repository):
    order_id = uuid.uuid4()
    order = Order(id=order_id, name="Test Order")
    mock_repository.find_by_id.return_value = order
    result = order_service.get_order(order_id)
    mock_repository.find_by_id.assert_called_once_with(order_id)
    assert result == order

def test_get_all_orders(order_service, mock_repository):
    orders = [Order(id=uuid.uuid4(), name="Test Order 1"), Order(id=uuid.uuid4(), name="Test Order 2")]
    mock_repository.find_all.return_value = orders
    result = order_service.get_all_orders()
    mock_repository.find_all.assert_called_once()
    assert result == orders

def test_delete_order(order_service, mock_repository):
    order_id = uuid.uuid4()
    order = Order(id=order_id, name="Test Order")
    mock_repository.find_by_id.return_value = order
    result = order_service.delete_order(order_id)
    mock_repository.find_by_id.assert_called_once_with(order_id)
    mock_repository.delete.assert_called_once_with(order)
    assert result == order

def test_delete_order_not_found(order_service, mock_repository):
    order_id = uuid.uuid4()
    mock_repository.find_by_id.return_value = None
    result = order_service.delete_order(order_id)
    mock_repository.find_by_id.assert_called_once_with(order_id)
    mock_repository.delete.assert_not_called()
    assert result is None

def test_update_order(order_service, mock_repository):
    order = Order(id=uuid.uuid4(), name="Updated Order")
    mock_repository.update.return_value = order
    result = order_service.update_order(order)
    mock_repository.update.assert_called_once_with(order)
    assert result == order