from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from models import Book
from schemas import BookCreate, BookOut
from dependencies import get_current_user

router = APIRouter(prefix="/books", tags=["Books"])



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/", response_model=BookOut)
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.get("/")
def get_books(
    page: int = Query(1, ge=1),
    limit: int = Query(5, ge=1, le=50),
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    offset = (page - 1) * limit

    total = db.query(Book).count()
    books = db.query(Book).offset(offset).limit(limit).all()

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "books": books
    }



@router.put("/{book_id}", response_model=BookOut)
def update_book(
    book_id: int,
    data: BookCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = data.title
    book.author = data.author
    book.price = data.price

    db.commit()
    db.refresh(book)
    return book



@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
