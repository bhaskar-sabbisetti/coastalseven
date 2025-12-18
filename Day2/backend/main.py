from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import User
from schemas import Register, Login
from security import hash_password, verify_password
from jwt_handler import create_access_token
from fastapi.middleware.cors import CORSMiddleware
from books import router as book_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(book_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],   
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: Register, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username exists")
    db_user = User(username=user.username, email=user.email, hashed_password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    return {"msg": "Registered"}

@app.post("/login")
def login(user: Login, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.username})
    return {"access_token": token}
@app.post("/Books")
def create_book():
    return {"msg": "Book created"}