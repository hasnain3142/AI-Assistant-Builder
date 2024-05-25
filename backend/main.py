from fastapi import FastAPI
from routes import query

app = FastAPI()

app.include_router(query.router, prefix="/query", tags=["query"])

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Assistant Builder root route."}