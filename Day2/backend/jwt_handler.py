from datetime import datetime, timedelta
from jose import jwt
import secrets
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"

def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=30)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)