from datetime import timedelta
from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, Token
from app.core import security
from app.core.config import settings

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def _create_tokens(self, user_id: str) -> Token:
        access_token = security.create_access_token(subject=user_id)
        refresh_token = security.create_refresh_token(subject=user_id)
        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer"
        )

    async def authenticate(self, email: str, password: str) -> Token:
        user = await self.user_repo.get_by_email(email)
        if not user or not user.hashed_password or not security.verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return self._create_tokens(user.id)

    async def authenticate_google(self, token: str) -> Token:
        from google.oauth2 import id_token
        from google.auth.transport import requests as google_requests
        
        try:
            # If Client ID is not set, validation will still check signature but not audience
            # In production, ALWAYS set GOOGLE_CLIENT_ID
            id_info = id_token.verify_oauth2_token(
                token, 
                google_requests.Request(), 
                settings.GOOGLE_CLIENT_ID or None
            )
            
            email = id_info['email']
            name = id_info.get('name', '')
            
        except ValueError as e:
            print(f"Google Auth Error: {e}")
            raise HTTPException(status_code=400, detail="Invalid Google Token")
            
        user = await self.user_repo.get_by_email(email)
        if not user:
            # Auto-register
            user = await self.user_repo.create({
                "email": email,
                "full_name": name,
                "hashed_password": None,
                "role": "student",
                "is_active": True
            })
            
        return self._create_tokens(user.id)

    async def register_user(self, user_in: UserCreate):
        existing_user = await self.user_repo.get_by_email(user_in.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        hashed_password = security.get_password_hash(user_in.password)
        user_data = user_in.model_dump(exclude={"password"})
        user_data["hashed_password"] = hashed_password
        
        return await self.user_repo.create(user_data)
