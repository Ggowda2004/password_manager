from fastapi import FastAPI, Header
from auth import create_user, verify_user, get_email_from_token
from models import SignupModel, LoginModel, PasswordEntry
from encryption import encrypt_password, decrypt_password
from database import passwords_collection
from dotenv import load_dotenv
import os
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY").encode()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/signup")
def signup(data: SignupModel):
    create_user(data.email, data.password)
    return {"message": "Signup successful"}

@app.post("/login")
def login(data: LoginModel):
    token = verify_user(data.email, data.password)
    if not token:
        return {"error": "Invalid credentials"}
    return {"token": token}

@app.post("/add-password")
def add_password(data: PasswordEntry, Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    email = get_email_from_token(token)

    encrypted_pw = encrypt_password(ENCRYPTION_KEY, data.password)

    passwords_collection.insert_one({
        "user_email": email,
        "site": data.site,
        "username": data.username,
        "password_encrypted": encrypted_pw,
        "created_at": datetime.utcnow()
    })

    return {"message": "Password stored successfully"}

@app.get("/get-passwords")
def get_passwords(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    email = get_email_from_token(token)

    user_passwords = []
    records = passwords_collection.find({"user_email": email})

    for item in records:
        decrypted_pw = decrypt_password(ENCRYPTION_KEY, item["password_encrypted"])
        user_passwords.append({
            "site": item["site"],
            "username": item["username"],
            "password": decrypted_pw
        })

    return user_passwords
