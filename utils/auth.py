import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Header
from passlib.context import CryptContext
from config import JWT_SECRET, JWT_ALGO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Create JWT token
def create_token(username: str, role: str):
    payload = {
        "user": username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=12)  # expires in 12 hours
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)

# Verify JWT token
def verify_token(authorization: str = Header(...)):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid auth scheme")
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        return payload
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

# Admin check
def admin_required(token_data):
    if token_data.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin-only route")

