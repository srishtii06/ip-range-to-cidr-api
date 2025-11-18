from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
""" engine is the core connection to the database.
    connect_args={"check_same_thread": False} is required for SQLite, because SQLite is single-threaded by default. This allows multiple threads (like FastAPI requests) to share the same connection safely."""
SessionLocal = sessionmaker(bind=engine, autoflush=False)
""" SessionLocal is a factory for database sessions.
    Each session represents a “working connection” with the database.
    autoflush=False means SQLAlchemy will not automatically send changes to the database until you call commit()"""
Base = declarative_base()
