from typing import List, Optional
from pydantic import BaseModel, Field

class SizeModel(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[SizeModel]

class ProductOut(BaseModel):
    id: str
    name: str
    price: float

class OrderItem(BaseModel):
    productId: str
    qty: int

class OrderCreate(BaseModel):
    userId: str
    items: List[OrderItem]
