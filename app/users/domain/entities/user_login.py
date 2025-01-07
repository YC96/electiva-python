from pydantic import BaseModel

class UserEntity(BaseModel):
    username: str
    hashed_password: str
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        from_attributes = True