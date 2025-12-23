from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict, Any
from datetime import datetime

class PortfolioBase(BaseModel):
    bio: Optional[str] = None
    skills: Optional[List[str]] = []
    experience: Optional[List[Dict[str, Any]]] = []
    education: Optional[List[Dict[str, Any]]] = []
    projects: Optional[List[Dict[str, Any]]] = []
    social_links: Optional[Dict[str, str]] = {}

class PortfolioCreate(PortfolioBase):
    pass

class PortfolioUpdate(PortfolioBase):
    pass

class PortfolioResponse(PortfolioBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ResumeExtractRequest(BaseModel):
    # This might be just a file upload in the endpoint, 
    # but we can use this for the text-based extraction too.
    text: Optional[str] = None
