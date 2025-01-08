from typing import Optional
from uuid import UUID
from sqlmodel import SQLModel, Field
from datetime import datetime

class Inventory(SQLModel, table=True):
    id: UUID = Field(primary_key=True)
    product_id: UUID = Field(index=True, nullable=False) 
    quantity: int = Field(nullable=False) 
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)  
    updated_at: Optional[datetime] = Field(default=None) 
