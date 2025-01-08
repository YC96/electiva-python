from sqlalchemy import Column, String, Float, Text, DateTime, event
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import datetime
import uuid

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    cost = Column(Float, nullable=False)
    margin = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    @staticmethod
    def calculate_price(mapper, connection, target):
        target.price = round(target.cost / (1 - target.margin / 100), 2)

event.listen(Product, 'before_insert', Product.calculate_price)
event.listen(Product, 'before_update', Product.calculate_price)