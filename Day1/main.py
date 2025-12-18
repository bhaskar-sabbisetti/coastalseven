from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/about")
# def about():
#     return{"about":"this msg is from bhaskar"}
# @app.get("/contact")
# def contact():
#     return{"contact":6281007255}
# @app.get("/student/{student_id}")
# def student(student_id:int):
#     return{"student_id":student_id}



# @app.get("/users")
# def my_profile(name : str = None,age: int = None):
#     return {
#         "name":name,
#         "age":age,
#     }
# from fastapi import HTTPException

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     if user_id != 1:
#         raise HTTPException(status_code=404, detail="User not found")
#     return {"user_id": user_id}


class User(BaseModel):
    name: str
    age: int
    email: str
# @app.post("/users")
# def create_user(user: User):
#     return {"name": user.name, "age": user.age, "email": user.email}
@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI application"}
user_data={
    1: {"name": "bhaskar", "age": 20, "email": "bhaskar@gmail.com" },
    2: {"name": "anvesh", "age": 22, "email": "anvesh@gmail.com"}
}
@app.get("/users")
def get_users():
    return user_data
@app.post("/register")
def register_user(user: User):
    user_id = len(user_data) + 1
    for i in user_data:
        if user.email==user_data[i]["email"]:
            return {"message":"User with this email already exists"}
    else:
        user_data[user_id] = {"name": user.name, "age": user.age, "email": user.email}
        return {"message": "User registered successfully", "user_id": user_id}
@app.put("/update/{user_id}")
def update_user(user_id: int, user: User):
    if user_id in user_data:
        user_data[user_id] = {"name": user.name, "age": user.age, "email": user.email}
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
@app.delete("/delete/{user_id}")
def delete_user(user_id: int):
    if user_id in user_data:
        del user_data[user_id]
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.patch("/update-email/{user_id}")
def update_email(user_id:int,update_user:User):
    for user in user_data:
        if user_id==user:
            if update_user.email is not None:
                user_data[user_id]["email"]=update_user.email
            if update_user.name is not None:
                user_data[user_id]["name"]=update_user.name
            if update_user.age is not None:
                user_data[user_id]["age"]=update_user.age
            return{"message":"user details updated successfully"}
    else:
        raise HTTPException(status_code=404,detail="user not found")
   