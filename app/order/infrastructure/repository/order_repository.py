import uuid
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session
from order.domain.entities.order import Order
from order.domain.repository.interface_order_repository import IOrderRepository
from order.infrastructure.database.orm.order_orm import OrderOrm

class SQLAlchemyOrderRepository(IOrderRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, order):

        self.db.add(OrderOrm(**order))
        self.db.commit()
        self.db.refresh(order)
        return order    
    
    def find_by_id(self, order_id: uuid) -> Order:
        order = self.db.query(OrderOrm).filter(OrderOrm.id == order_id).first()
        if order:
            return Order.from_orm(order)
        return None

    def find_all(self) -> list[Order]:
        orders = self.db.query(OrderOrm).all()
        return [Order.from_orm(order) for order in orders]
    
    def delete(self, order_id: uuid) -> str:
        db_order = self.db.query(OrderOrm).filter(OrderOrm.id == order_id).first()
        if db_order:
            try:
                self.db.delete(db_order)
                self.db.commit()
            except IntegrityError as e:
                self.db.rollback()
                return None

    def update(self, order: Order) -> Order:
        db_order = self.db.query(OrderOrm).filter(OrderOrm.id == order.id).first()
        if db_order:
            db_order.total_amount = order.total_amount
            db_order.status = order.status
            db_order.fk_user = order.fk_user
            self.db.commit()
            self.db.refresh(db_order)
            return Order.from_orm(db_order)
        return None
