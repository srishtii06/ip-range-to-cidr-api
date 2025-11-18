from pydantic import BaseModel, IPvAnyAddress
from typing import List

class IPRangeRequest(BaseModel):
    start_ip: IPvAnyAddress
    end_ip: IPvAnyAddress

class CIDRResponse(BaseModel):
    cidrs: List[str]

class HistoryResponse(BaseModel):
    id: int
    start_ip: str
    end_ip: str
    cidrs: str
    created_at: str

class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    password: str
    role: str = "guest"  # optional
