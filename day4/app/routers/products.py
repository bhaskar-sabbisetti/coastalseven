from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Product
from app.schemas import BulkProductCreate

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/bulk")
def bulk_insert_products(
    payload: BulkProductCreate,
    db: Session = Depends(get_db)
):
    product_objects = [
        Product(
            name=p.name,
            price=p.price,
            quantity=p.quantity
        )
        for p in payload.products
    ]

    db.bulk_save_objects(product_objects)
    db.commit()

    return {
        "inserted_count": len(product_objects),
        "message": "Products inserted successfully"
    }
