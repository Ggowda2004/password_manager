# models.py
from pydantic import BaseModel

class SignupModel(BaseModel):
    email: str
    password: str

class LoginModel(BaseModel):
    email: str
    password: str

class PasswordEntry(BaseModel):
    site: str
    username: str
    password: str
