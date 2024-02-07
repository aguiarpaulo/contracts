from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime
from enum import Enum

class CategoryEnum(str, Enum):
    category1 = "category 1"
    category2 = "category 2"
    category3 = "category 3" 

class Sales(BaseModel):
    email: EmailStr
    date: datetime
    value: PositiveFloat
    product: str
    quantity: PositiveInt
    category: CategoryEnum

    @field_validator('category')
    def category_in_enum(cls, error):
        return error