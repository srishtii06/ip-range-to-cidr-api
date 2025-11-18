import jwt
from fastapi import HTTPException, Header
from config import JWT_SECRET, JWT_ALGO

def create_token(username: str, role: str):
    return jwt.encode({"user": username, "role": role}, JWT_SECRET, algorithm=JWT_ALGO)

def verify_token(token: str = Header(...)):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

def admin_required(token_data):
    if token_data.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin-only route")
