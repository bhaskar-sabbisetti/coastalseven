from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user import Token, UserCreate, UserResponse, GoogleLogin
from app.services.auth_service import AuthService
from app.repositories.user_repository import UserRepository
from app.models.user import User

router = APIRouter()

@router.post("/google", response_model=Token)
async def google_login(
    login_data: GoogleLogin,
    db: AsyncSession = Depends(get_db)
):
    """
    Google OAuth2 Login.
    """
    user_repo = UserRepository(User, db)
    auth_service = AuthService(user_repo)
    return await auth_service.authenticate_google(login_data.credential)

@router.post("/login", response_model=Token)
async def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    user_repo = UserRepository(User, db)
    auth_service = AuthService(user_repo)
    return await auth_service.authenticate(form_data.username, form_data.password)

@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Create new user without the need to be logged in.
    """
    user_repo = UserRepository(User, db)
    auth_service = AuthService(user_repo)
    return await auth_service.register_user(user_in)
