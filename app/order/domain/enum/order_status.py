
from enum import Enum

class OrderStatus(str, Enum):
    Cancelled = "Cancelled"
    Pending = "Pending"
    Completed = "Completed"