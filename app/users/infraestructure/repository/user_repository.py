import uuid
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session
from app.users.domain.entities.user_entities import UserCreate, UserEntity
from app.users.domain.repository.user_repository import IUserRepository
from app.users.infraestructure.orm.user_orm import UserOrm

class SqlAlchemyUserRepository(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: UserEntity) -> UserEntity:
        user_dict = user.dict()
        user_orm = UserOrm(**user_dict)
        try:
            self.session.add(user_orm)
            self.session.commit()
            self.session.refresh(user_orm)
            return user_orm
        except IntegrityError as e:
            self.session.rollback()
            raise e

    def find_all(self) -> UserEntity:
        users = self.session.query(UserOrm).all()
        return users

    def find_by_id(self, user_id: uuid.UUID) -> UserEntity:
        user = self.session.query(UserOrm).filter(UserOrm.id == user_id).first()
        return user

    def find_by_email(self, email: str) -> UserEntity:
        user = self.session.query(UserOrm).filter(UserOrm.email == email).first()
        return user

    def find_by_role(self, role: str) -> UserCreate:
        users = self.session.query(UserOrm).filter(UserOrm.role == role, UserOrm.is_active == True).all()
        return users

    def update(self, user: UserEntity) -> None:
        user_orm = self.session.query(UserOrm).filter(UserOrm.id == user.id).first()
        user_orm.username = user.username
        user_orm.hashed_password = user.hashed_password
        user_orm.is_active = user.is_active
        user_orm.role = user.role
        user_orm.updated_at = user.updated_at
        self.session.commit()
        return user_orm

    def delete(self, user_id: uuid.UUID) -> None:
        user = self.session.query(UserOrm).filter(UserOrm.id == user_id).first()
        self.session.delete(user)
        self.session.commit()