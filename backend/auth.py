import jwt
import bcrypt
import os
from datetime import datetime, timedelta
from database import users_collection
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

def create_user(email, password):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users_collection.insert_one({"email": email, "password": hashed_pw})

def verify_user(email, password):
    user = users_collection.find_one({"email": email})
    if not user:
        return None

    if bcrypt.checkpw(password.encode(), user["password"].encode()):
        token = jwt.encode(
            {"email": user["email"], "exp": datetime.utcnow() + timedelta(hours=24)},
            JWT_SECRET,
            algorithm="HS256"
        )
        return token
    
    return None

def get_email_from_token(token):
    decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    return decoded["email"]
