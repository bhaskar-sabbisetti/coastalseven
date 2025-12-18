from pydantic import BaseModel, EmailStr

class Register(BaseModel):
    username: str
    email: EmailStr
    password: str

class Login(BaseModel):
    username: str
    password: str
class BookCreate(BaseModel):
    title: str
    author: str
    price: float

class BookOut(BookCreate):
    id: int

    class Config:
        from_attributes = True
