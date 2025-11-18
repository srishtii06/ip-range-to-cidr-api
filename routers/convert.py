from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db_helpers.schemas import IPRangeRequest, CIDRResponse
from utils.ip_helper import convert_range_to_cidr
from db_helpers.database import SessionLocal
from db_helpers.models import ConversionHistory

router = APIRouter(prefix="/convert", tags=["Convert"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CIDRResponse)
def convert_ip_range(payload: IPRangeRequest, db: Session = Depends(get_db)):
    try:
        cidrs = convert_range_to_cidr(str(payload.start_ip), str(payload.end_ip))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    db_entry = ConversionHistory(
        start_ip=str(payload.start_ip),
        end_ip=str(payload.end_ip),
        cidrs=",".join(cidrs)
    )
    db.add(db_entry)
    db.commit()

    return CIDRResponse(cidrs=cidrs)
