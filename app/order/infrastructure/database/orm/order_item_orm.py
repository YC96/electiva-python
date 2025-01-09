from app.order.infrastructure.database.database_config import Base
from sqlalchemy import UUID, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class OrderItemOrm(Base):
    __tablename__ = "order_item"
    id = Column(UUID, primary_key=True)
    quantity = Column(Integer, nullable=False)
    fk_order = Column(UUID, ForeignKey('order.id'))
    order = relationship("order", back_populates="order_item")
    fk_product = Column(UUID, ForeignKey('product.id'))
    product = relationship("product", back_populates="order_item")
