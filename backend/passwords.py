from fastapi import APIRouter, Depends
from database import passwords_collection
from auth import get_email_from_token
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class PasswordData(BaseModel):
    website: str
    username: str
    password: str   # (we will encrypt this later)

@router.post("/add-password")
def add_password(data: PasswordData, email: str = Depends(get_email_from_token)):
    passwords_collection.insert_one({
        "owner": email,
        "website": data.website,
        "username": data.username,
        "password": data.password,
        "created_at": datetime.utcnow()
    })
    return {"status": "success", "message": "Password saved"}
