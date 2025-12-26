from pydantic import BaseModel

from typing import Dict, Any,List

class DashboardStats(BaseModel):
    total_orders: int
    total_revenue: float
    avg_order_value: float
    highest_order: float


class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int

class BulkProductCreate(BaseModel):
    products: List[ProductCreate]

class FileCreate(BaseModel):
    filename: str
    metadata: Dict[str, Any]

class FileResponse(BaseModel):
    id: int
    filename: str
    metadata: Dict[str, Any]
