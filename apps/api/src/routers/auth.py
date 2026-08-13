from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login():
    return {"token": "mock-jwt-token", "user": "qa_engineer"}

@router.get("/me")
async def me():
    return {"id": "1", "name": "QA Engineer", "role": "admin"}
