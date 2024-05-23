from fastapi import FastAPI
from routes import query

app = FastAPI()

app.include_router(query.router, prefix="/query", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI project"}