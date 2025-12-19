from pydantic import BaseModel

from typing import Dict, Any

class DashboardStats(BaseModel):
    total_orders: int
    total_revenue: float
    avg_order_value: float
    highest_order: float


class FileCreate(BaseModel):
    filename: str
    metadata: Dict[str, Any]

class FileResponse(BaseModel):
    id: int
    filename: str
    metadata: Dict[str, Any]
