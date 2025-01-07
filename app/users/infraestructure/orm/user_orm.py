from app.auth.infraestructure.auth_controller import JWTService
from sqlalchemy import UUID, Column, DateTime, MetaData, String,Boolean, Enum
from app.users.domain.enum.role import RoleEnum
from app.common.database.postgresql import Base, engine
from sqlalchemy import event
from sqlalchemy.orm import Session
import uuid
from datetime import datetime

class UserOrm(Base):
  __tablename__ = 'User'
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
  username = Column(String(50), nullable=False, unique=True, index=True)
  email = Column(String(50), nullable=False, unique=True, index=True)
  hashed_password = Column(String(200), nullable=False)
  is_active = Column(Boolean, default=True)
  role = Column(Enum(RoleEnum), nullable=False)
  created_at = Column(DateTime, nullable=False,default=datetime.now)
  updated_at = Column(DateTime,default=datetime.now)


def insert_initial_values(target, connection, **kw):
  with Session(bind=connection) as session:
    password = JWTService.encrypt_password('admin123')
    initial_user = UserOrm(
      username = 'administrador',
      email = 'superadmin@gmail.com',
      hashed_password = password,
      role = RoleEnum.SUPERADMIN,
      created_at = datetime.now(),
      updated_at = datetime.now()
    )
    session.add(initial_user)
    session.commit()
    session.refresh(initial_user)


metadata = MetaData()
event.listen(UserOrm.__table__, 'after_create', insert_initial_values)
Base.metadata.create_all(bind=engine)

