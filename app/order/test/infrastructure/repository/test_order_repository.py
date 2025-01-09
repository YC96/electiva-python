import pytest
import uuid
from sqlalchemy.orm import Session
from app.order.domain.entities.order import Order
from app.order.infrastructure.repository.order_repository import SQLAlchemyOrderRepository
from app.order.infrastructure.database.orm.order_orm import OrderOrm

@pytest.fixture
def session():
    # Mock the SQLAlchemy session
    session = Session()
    yield session
    session.close()

@pytest.fixture
def repository(session):
    return SQLAlchemyOrderRepository(db=session)

def test_create_order(repository, session):
    order_data = {
        'id': uuid.uuid4(),
        'total_amount': 100.0,
        'status': 'pending',
        'fk_user': uuid.uuid4()
    }
    order = Order(**order_data)
    created_order = repository.create(order)
    assert created_order.id == order_data['id']
    assert created_order.total_amount == order_data['total_amount']
    assert created_order.status == order_data['status']
    assert created_order.fk_user == order_data['fk_user']

def test_find_by_id(repository, session):
    order_id = uuid.uuid4()
    order_orm = OrderOrm(id=order_id, total_amount=100.0, status='pending', fk_user=uuid.uuid4())
    session.add(order_orm)
    session.commit()
    found_order = repository.find_by_id(order_id)
    assert found_order.id == order_id

def test_find_all(repository, session):
    order_orm1 = OrderOrm(id=uuid.uuid4(), total_amount=100.0, status='pending', fk_user=uuid.uuid4())
    order_orm2 = OrderOrm(id=uuid.uuid4(), total_amount=200.0, status='completed', fk_user=uuid.uuid4())
    session.add(order_orm1)
    session.add(order_orm2)
    session.commit()
    orders = repository.find_all()
    assert len(orders) == 2

def test_delete_order(repository, session):
    order_id = uuid.uuid4()
    order_orm = OrderOrm(id=order_id, total_amount=100.0, status='pending', fk_user=uuid.uuid4())
    session.add(order_orm)
    session.commit()
    repository.delete(order_id)
    deleted_order = session.query(OrderOrm).filter(OrderOrm.id == order_id).first()
    assert deleted_order is None

def test_update_order(repository, session):
    order_id = uuid.uuid4()
    order_orm = OrderOrm(id=order_id, total_amount=100.0, status='pending', fk_user=uuid.uuid4())
    session.add(order_orm)
    session.commit()
    updated_order_data = Order(id=order_id, total_amount=150.0, status='completed', fk_user=uuid.uuid4())
    updated_order = repository.update(updated_order_data)
    assert updated_order.total_amount == 150.0
    assert updated_order.status == 'completed'