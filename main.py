from fastapi import FastAPI
from routers import convert, history,auth
from db_helpers.database import engine, Base

app = FastAPI(title="IP Range to CIDR Converter API")

Base.metadata.create_all(bind=engine)
""" It creates all database tables defined in your SQLAlchemy models in the connected database if they don't already exist. """

app.include_router(convert.router)
app.include_router(history.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "IP Range to CIDR API running"}
