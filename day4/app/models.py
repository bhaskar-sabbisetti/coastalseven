from sqlalchemy import Column, Integer, Numeric, String, DateTime,JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()




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
