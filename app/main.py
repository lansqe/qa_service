from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.api.endpoints import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="QA Service API", version="1.0.0")

app.include_router(router, prefix="/api/v1", tags=["api"])

@app.get("/")
def read_root():
    return {"message": "QA Service API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}