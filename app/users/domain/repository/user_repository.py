from abc import ABC, abstractmethod
from typing import Optional
import uuid
from app.users.domain.entities.user_entities import UserCreate, UserEntity

class IUserRepository(ABC):
  @abstractmethod
  def create(self,user:UserEntity)-> None:
    pass

  @abstractmethod
  def find_all(self)-> Optional[UserEntity]:
    pass

  @abstractmethod
  def find_by_id(self,user_id:uuid.UUID)-> Optional[UserEntity]:
    pass

  @abstractmethod
  def find_by_email(self,email:str)-> Optional[UserEntity]:
    pass

  @abstractmethod
  def find_by_role(self,role:str)-> Optional[UserCreate]:
    pass

  @abstractmethod
  def update(self,user:UserEntity)-> None:
    pass

  @abstractmethod
  def delete(self,user_id:uuid.UUID)-> None:
    pass
