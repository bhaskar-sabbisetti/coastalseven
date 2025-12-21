from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import requests
import uuid

from oauth import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL, USERINFO_URL
from jwt_utils import create_access_token
from redis_conn import redis_client
from jose import jwt, JWTError
import os

app = FastAPI()
security = HTTPBearer()
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"

@app.get("/login/google")
def login_google():
    url = (
        f"{AUTH_URL}"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&response_type=code"
        f"&scope=openid email profile"
    )
    return RedirectResponse(url)


# ---------------- OAUTH CALLBACK ----------------
@app.get("/auth/callback")
def auth_callback(code: str):
    # Exchange code for Google token
    token_data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    token_response = requests.post(TOKEN_URL, data=token_data)
    token_json = token_response.json()

    access_token = token_json.get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="OAuth failed")

    # Fetch Google user info
    headers = {"Authorization": f"Bearer {access_token}"}
    user_response = requests.get(USERINFO_URL, headers=headers)
    user = user_response.json()

    email = user["email"]

    # Create JWT for our app
    jwt_token = create_access_token({"sub": email})

    # Create Redis session
    session_id = str(uuid.uuid4())
    redis_client.setex(
        f"session:{session_id}",
        1800,  # 30 minutes
        jwt_token
    )

    return {
        "message": "Login successful",
        "session_id": session_id,
        "jwt_token": jwt_token,
        "user": {
            "email": email,
            "name": user.get("name")
        }
    }


# ---------------- AUTH DEPENDENCY ----------------
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Check Redis session
    for key in redis_client.scan_iter(match="session:*"):
        if redis_client.get(key) == token:
            return payload["sub"]

    raise HTTPException(status_code=401, detail="Session expired")


# ---------------- PROTECTED API ----------------
@app.get("/profile")
def profile(user_email: str = Depends(get_current_user)):
    return {
        "message": "Access granted",
        "email": user_email
    }


# ---------------- LOGOUT ----------------
@app.post("/logout")
def logout(session_id: str):
    redis_client.delete(f"session:{session_id}")
    return {"message": "Logged out successfully"}
