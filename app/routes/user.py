from bson import ObjectId
from fastapi import APIRouter, HTTPException
from ..database import db
from ..models import User

router = APIRouter()

@router.post("/users/", response_model=User )
async def create_user(user: User):
    user_dict = user.dict()
    user_dict["_id"] = ObjectId()  # Generate a new ObjectId
    db.users.insert_one(user_dict)
    user.id = str(user_dict["_id"])  # Set the id
    return user

@router.get("/users/{user_id}", response_model=User )
async def read_user(user_id: str):
    user_data = db.users.find_one({"_id": ObjectId(user_id)})
    if user_data is None:
        raise HTTPException(status_code=404, detail="User  not found")
    return User(id=str(user_data["_id"]), name=user_data["name"], email=user_data["email"])