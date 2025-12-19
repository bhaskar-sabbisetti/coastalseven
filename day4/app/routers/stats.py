from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models import Order

router = APIRouter(prefix="/stats", tags=["Stats"])

@router.get("/dashboard")
def dashboard_stats(db: Session = Depends(get_db)):
    total_orders = db.query(func.count(Order.id)) \
        .filter(Order.status == "completed") \
        .scalar()

    total_revenue = db.query(func.coalesce(func.sum(Order.amount), 0)) \
        .filter(Order.status == "completed") \
        .scalar()

    avg_order_value = db.query(func.coalesce(func.avg(Order.amount), 0)) \
        .filter(Order.status == "completed") \
        .scalar()

    highest_order = db.query(func.coalesce(func.max(Order.amount), 0)) \
        .filter(Order.status == "completed") \
        .scalar()

    return {
        "total_orders": total_orders,
        "total_revenue": float(total_revenue),
        "avg_order_value": float(avg_order_value),
        "highest_order": float(highest_order)
    }
