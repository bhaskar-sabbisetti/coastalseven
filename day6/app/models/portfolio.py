from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.db.base import Base

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False, unique=True)
    bio = Column(Text, nullable=True)
    skills = Column(JSON, nullable=True)  # List of strings
    experience = Column(JSON, nullable=True)  # List of dicts
    education = Column(JSON, nullable=True)  # List of dicts
    projects = Column(JSON, nullable=True)  # List of dicts
    social_links = Column(JSON, nullable=True)  # Dict of links
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", backref="portfolio")
