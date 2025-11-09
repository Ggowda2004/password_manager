🛡️ Password Manager (FastAPI + MongoDB)

A secure web-based password manager built using FastAPI, MongoDB, and AES encryption.
Users can safely sign up, log in, store, view, and manage passwords — with encryption and authentication.

🚀 Tech Stack

Frontend: HTML, CSS, JavaScript
Backend: FastAPI (Python)
Database: MongoDB Atlas
Authentication: JWT (JSON Web Tokens)
Encryption: AES (Fernet) + bcrypt hashing

⚙️ Features
    User signup & login (JWT-based authentication)
    AES-encrypted password storage
    Show/Hide passwords
    Delete saved credentials
    Logout functionality

🧩 Project Structure
password-manager|
│
├── backend/
│   ├── main.py                # FastAPI entry point
│   ├── auth.py                # User authentication & token logic
│   ├── database.py            # MongoDB connection
│   ├── encryption.py          # AES encryption/decryption
│   ├── models.py              # Data models using Pydantic
│   ├── .env                   # Environment variables (not in Git)
│   ├── requirements.txt       # Dependencies
│
├── frontend/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── app.js
│   ├── styles.css
│
└── README.md

🧠 Environment Variables (.env)

Create a .env file inside /backend with:

MONGO_URI = "your_mongodb_connection_string"
JWT_SECRET = "your_secret_key"
ENCRYPTION_KEY = "your_fernet_key"

***To generate a Fernet key:
run in terminal :
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())


▶️ Running Locally
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Then open frontend/login.html in your browser.


**Deployment**

Deployment (to Vercel) will be added soon.

👨‍💻 Author
Gangadhar Gowda K M
