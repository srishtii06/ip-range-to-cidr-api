from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from db_helpers.database import Base

class ConversionHistory(Base):
    __tablename__ = "conversion_history"

    id = Column(Integer, primary_key=True, index=True)
    start_ip = Column(String, nullable=False)
    end_ip = Column(String, nullable=False)
    cidrs = Column(Text, nullable=False)
    user = Column(String, default="guest")
    created_at = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # store hashed password
    role = Column(String, default="guest")  # admin or guest
    created_at = Column(DateTime, default=datetime.utcnow)
