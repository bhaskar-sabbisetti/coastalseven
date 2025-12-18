from fastapi import APIRouter, HTTPException
from app.database import get_db
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.post("/teachers")
def add_teacher(teacher: dict):
    db = get_db()

    teacher["createdAt"] = datetime.utcnow()
    teacher["updatedAt"] = datetime.utcnow()
    teacher["isDeleted"] = False

    result = db.teacher.insert_one(teacher)

    return {
        "message": "Teacher added successfully",
        "id": str(result.inserted_id)
    }
@router.get("/teachers")
def get_teachers():
    db = get_db()

    teachers = list(db.teacher.find({"isDeleted": {"$ne": True}}))

    for t in teachers:
        t["_id"] = str(t["_id"])

    return teachers
@router.get("/teachers/{teacher_id}")
def get_teacher_by_id(teacher_id: str):
    db = get_db()

    teacher = db.teacher.find_one({
        "_id": ObjectId(teacher_id),
        "isDeleted": {"$ne": True}
    })

    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    teacher["_id"] = str(teacher["_id"])
    return teacher
@router.patch("/teachers/{teacher_id}")
def update_teacher(teacher_id: str, data: dict):
    db = get_db()

    data["updatedAt"] = datetime.utcnow()

    result = db.teacher.update_one(
        {"_id": ObjectId(teacher_id), "isDeleted": {"$ne": True}},
        {"$set": data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Teacher not found")

    return {"message": "Teacher updated successfully"}
@router.put("/teachers/{teacher_id}")
def replace_teacher(teacher_id: str, teacher: dict):
    db = get_db()

    teacher["updatedAt"] = datetime.utcnow()

    result = db.teacher.replace_one(
        {"_id": ObjectId(teacher_id), "isDeleted": {"$ne": True}},
        teacher
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Teacher not found")

    return {"message": "Teacher replaced successfully"}
@router.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: str):
    db = get_db()

    result = db.teacher.update_one(
        {"_id": ObjectId(teacher_id)},
        {
            "$set": {
                "isDeleted": True,
                "deletedAt": datetime.utcnow()
            }
        }
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Teacher not found")

    return {"message": "Teacher deleted successfully (soft delete)"}
@router.patch("/teachers/restore/{teacher_id}")
def restore_teacher(teacher_id: str):
    db = get_db()

    result = db.teacher.update_one(
        {"_id": ObjectId(teacher_id)},
        {"$unset": {"isDeleted": "", "deletedAt": ""}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Teacher not found")

    return {"message": "Teacher restored successfully"}
