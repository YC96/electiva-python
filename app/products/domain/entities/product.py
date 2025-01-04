from uuid import UUID
from datetime import datetime

class Product:
    def __init__(self, id: UUID, code: str, name: str, description: str, cost: float, margin: float, price: float, created_at: datetime, updated_at: datetime):
        self.id = id
        self.code = code
        self.name = name
        self.description = description
        self.cost = cost
        self.margin = margin
        self.price = price
        self.created_at = created_at
        self.updated_at = updated_at