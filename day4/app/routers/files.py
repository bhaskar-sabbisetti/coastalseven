from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import File
from app.schemas import FileCreate

router = APIRouter(prefix="/files", tags=["Files"])

@router.post("/")
def upload_file(file: FileCreate, db: Session = Depends(get_db)):
    new_file = File(
        filename=file.filename,
        file_metadata=file.metadata  
    )
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    return {
        "id": new_file.id,
        "filename": new_file.filename,
        "metadata": new_file.file_metadata
    }
