import pytest
import uuid
from sqlalchemy.orm import Session
from app.order.infrastructure.repository.order_item_repository import SQLAlchemyOrderItemsRepository
from app.order.infrastructure.database.orm.order_item_orm import OrderItemOrm
from app.order.domain.entities.order_items import OrderItems

@pytest.fixture
def session():
    # Setup the database session here
    # This is a placeholder, replace with actual session setup
    return Session()

@pytest.fixture
def repository(session):
    return SQLAlchemyOrderItemsRepository(session)

def test_create_order_item(repository, session):
    order_item_data = {
        'id': uuid.uuid4(),
        'quantity': 10,
        'fk_product': uuid.uuid4(),
        'fk_order': uuid.uuid4()
    }
    order_item = repository.create(order_item_data)
    assert order_item.id == order_item_data['id']
    assert order_item.quantity == order_item_data['quantity']
    assert order_item.fk_product == order_item_data['fk_product']
    assert order_item.fk_order == order_item_data['fk_order']

def test_find_by_id(repository, session):
    order_item_id = uuid.uuid4()
    order_item_orm = OrderItemOrm(id=order_item_id, quantity=10, fk_product=uuid.uuid4(), fk_order=uuid.uuid4())
    session.add(order_item_orm)
    session.commit()
    found_order_item = repository.find_by_id(order_item_id)
    assert found_order_item.id == order_item_id

def test_find_all(repository, session):
    order_item_orm1 = OrderItemOrm(id=uuid.uuid4(), quantity=10, fk_product=uuid.uuid4(), fk_order=uuid.uuid4())
    order_item_orm2 = OrderItemOrm(id=uuid.uuid4(), quantity=5, fk_product=uuid.uuid4(), fk_order=uuid.uuid4())
    session.add(order_item_orm1)
    session.add(order_item_orm2)
    session.commit()
    order_items = repository.find_all()
    assert len(order_items) == 2

def test_delete_order_item(repository, session):
    order_item_id = uuid.uuid4()
    order_item_orm = OrderItemOrm(id=order_item_id, quantity=10, fk_product=uuid.uuid4(), fk_order=uuid.uuid4())
    session.add(order_item_orm)
    session.commit()
    repository.delete(order_item_id)
    deleted_order_item = session.query(OrderItemOrm).filter(OrderItemOrm.id == order_item_id).first()
    assert deleted_order_item is None

def test_update_order_item(repository, session):
    order_item_id = uuid.uuid4()
    order_item_orm = OrderItemOrm(id=order_item_id, quantity=10, fk_product=uuid.uuid4(), fk_order=uuid.uuid4())
    session.add(order_item_orm)
    session.commit()
    updated_order_item = OrderItems(id=order_item_id, quantity=20, fk_product=uuid.uuid4(), fk_order=uuid.uuid4())
    result = repository.update(updated_order_item)
    assert result.quantity == 20