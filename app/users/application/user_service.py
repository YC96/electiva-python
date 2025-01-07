from datetime import datetime
from typing import List, Optional
import uuid
from app.users.domain.entities.user_entities import UserEntity, UserCreate, UserUpdate
from app.users.domain.repository.user_repository import IUserRepository
import bcrypt
import re
from app.users.domain.enum.role import RoleEnum

class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def create_user(self, user: UserEntity) -> None:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, user.email):
            return False
        
        existing_user_email = self.user_repository.find_by_email(user.email)
        if existing_user_email:
            raise ValueError("El usuario ya existe")
        
        user.hashed_password = bcrypt.hashpw(user.hashed_password.encode('utf-8'), bcrypt.gensalt())
        
        if user.role == "superadmin":
            user.role = RoleEnum.SUPERADMIN
        
        if user.role == "manager":
            user.role = RoleEnum.MANAGER
        
        if user.role == "customer":
            user.role = RoleEnum.CUSTOMER

        user = UserCreate(
            username=user.username,
            email=user.email,
            hashed_password=user.hashed_password,
            role=user.role
        )

        return self.user_repository.create(user)

    def find_user_by_id(self, user_id: uuid.UUID) -> Optional[UserEntity]:
        return self.user_repository.find_by_id(user_id)
    
    def find_all_users(self) -> List[UserEntity]:
        return self.user_repository.find_all()

    def find_user_by_email(self, email: str) -> Optional[UserEntity]:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("El email no es válido")
        return self.user_repository.find_by_email(email)

    def find_user_by_role(self, role: str) -> Optional[UserCreate]:
        if role != "manager":
            raise ValueError("El rol no es válido debe ser un gerente")
        else:
            role = RoleEnum.MANAGER
        response = self.user_repository.find_by_role(role)
        return response

    def update_user(self, user: UserUpdate) -> None:
        user.updated_at = datetime.now()
        return self.user_repository.update(user)

    def delete_user(self, user: UserUpdate) -> None:
        user.is_active = False
        return self.user_repository.update(user)