from fastapi import FastAPI
from routers import convert, history
from db_helpers.database import engine, Base

app = FastAPI(title="IP Range to CIDR Converter API")

Base.metadata.create_all(bind=engine)

app.include_router(convert.router)
app.include_router(history.router)

@app.get("/")
def root():
    return {"message": "IP Range to CIDR API running"}
