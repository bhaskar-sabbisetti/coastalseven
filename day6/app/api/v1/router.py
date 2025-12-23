from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, contact, portfolios

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(contact.router, prefix="/contact", tags=["contact"])
api_router.include_router(portfolios.router, prefix="/portfolios", tags=["portfolios"])
