import uuid
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session
from app.order.domain.entities.order import Order
from app.order.domain.entities.order_items import OrderItems
from app.order.domain.repository.interface_order_item_repository import IOrderItemsRepository
from app.order.infrastructure.database.orm.order_item_orm import OrderItemOrm
from app.order.infrastructure.database.orm.order_orm import OrderOrm

class SQLAlchemyOrderItemsRepository(IOrderItemsRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, order_item):

        self.db.add(OrderItemOrm(**order_item))
        self.db.commit()
        self.db.refresh(order_item)
        return order_item    
    
    def find_by_id(self, order_items_id: uuid) -> OrderItems:
        order_items = self.db.query(OrderItemOrm).filter(OrderItemOrm.id == order_items_id).first()
        if order_items:
            return OrderItems.from_orm(order_items)
        return None

    def find_all(self) -> list[OrderItems]:
        orders = self.db.query(OrderItemOrm).all()
        return [OrderItems.from_orm(order) for order in orders]
    
    def delete(self, order_items_id: uuid) -> str:
        db_order = self.db.query(OrderItemOrm).filter(OrderItemOrm.id == order_items_id).first()
        if db_order:
            try:
                self.db.delete(db_order)
                self.db.commit()
            except IntegrityError as e:
                self.db.rollback()
                return None

    def update(self, order_item: OrderItems) -> OrderItems:
        db_order = self.db.query(OrderItemOrm).filter(OrderItemOrm.id == order_item.id).first()
        if db_order:
            db_order.quantity = order_item.quantity
            db_order.fk_product = order_item.fk_product
            db_order.fk_order = order_item.fk_order
            self.db.commit()
            self.db.refresh(db_order)
            return Order.from_orm(db_order)
        return None
