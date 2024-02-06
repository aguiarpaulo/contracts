from pydantic import BaseModel
from datetime import datetime

class Sales(BaseModel):
    email: str
    date: datetime
    value: int
    product: str
    quantity: int
    category: str