from pydantic import BaseModel
from bson import ObjectId

class User(BaseModel):
    id: str = None
    name: str
    email: str

    class Config:
        orm_mode = True