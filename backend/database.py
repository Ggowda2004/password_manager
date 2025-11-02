# database.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)

db = client["password_manager_db"]
users_collection = db["users"]
passwords_collection = db["passwords"]
