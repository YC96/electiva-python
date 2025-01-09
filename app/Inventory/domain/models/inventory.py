from typing import Optional
from uuid import UUID
from sqlalchemy import BaseModel,Field
from datetime import datetime

class Inventory(BaseModel):
    id: UUID = Field(primary_key=True)
    product_id: UUID = Field(index=True, nullable=False) 
    quantity: int = Field(nullable=False) 
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)  
    updated_at: Optional[datetime] = Field(default=None) 
    class Config:
        orm_mode = True 
        
