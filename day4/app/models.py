from sqlalchemy import Column, Integer, Numeric, String, DateTime, JSON
from datetime import datetime
from app.database import Base




class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    file_metadata = Column("metadata", JSON)
    created_at = Column(DateTime, default=datetime.utcnow)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount = Column(Numeric)
    status = Column(String)
    created_at = Column(DateTime)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    quantity = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)