from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.auth import verify_token, admin_required
from db_helpers.database import SessionLocal
from db_helpers.models import ConversionHistory

router = APIRouter(prefix="/history", tags=["History"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_history(token = Depends(verify_token), db: Session = Depends(get_db)):
    admin_required(token)
    return db.query(ConversionHistory).all()
