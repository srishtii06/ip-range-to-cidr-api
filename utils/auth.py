import jwt
import bcrypt
from datetime import datetime, timedelta
from fastapi import HTTPException, Header
from config import JWT_SECRET, JWT_ALGO

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt with a randomly generated salt
    """
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt(rounds=12)  # default 12 rounds
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")  # store as string in DB


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password
    """
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def create_token(username: str, role: str) -> str:
    payload = {
        "user": username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=12)  # expires in 12 hours
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)


def verify_token(authorization: str = Header(...)):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid auth scheme")
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

def admin_required(token_data):
    if token_data.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin-only route")
