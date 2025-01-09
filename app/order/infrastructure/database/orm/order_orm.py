
from sqlalchemy import UUID, Column, DateTime, Float, ForeignKey, Integer, MetaData, String
from sqlalchemy.orm import relationship
from app.common.database.postgresql import Base, engine

class OrderOrm(Base):
    __tablename__ = "order"
    id = Column(UUID, primary_key=True)
    total_amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime)
    fk_user = Column(UUID, ForeignKey('user.id'))
    user = relationship("user", back_populates="order")

metadata = MetaData()
Base.metadata.create_all(bind=engine)

