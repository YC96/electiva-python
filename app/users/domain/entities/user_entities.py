import uuid
from pydantic import BaseModel, Field
from datetime import datetime
from app.users.domain.enum.role import RoleEnum
from typing import Optional


class UserEntity(BaseModel):
    username: str
    email: str
    hashed_password: str
    role: RoleEnum
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        from_attributes = True

class UserCreate(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str
    email: str
    hashed_password: str
    is_active: bool = True
    role: RoleEnum
    created_at: datetime = Field(..., default_factory=datetime.now)
    updated_at: datetime = Field(..., default_factory=datetime.now)
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        from_attributes = True

class UserUpdate(BaseModel):
    id: Optional[uuid.UUID] = None
    username: Optional[str] = None
    email: Optional[str] = None
    hashed_password: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[RoleEnum] = None
    updated_at: Optional[datetime] = None
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        from_attributes = True