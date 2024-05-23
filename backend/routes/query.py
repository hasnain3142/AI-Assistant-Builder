from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def query():
    return [{"username": "Alice"}, {"username": "Bob"}]