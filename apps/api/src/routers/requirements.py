from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RequirementCreate(BaseModel):
    title: str
    description: str
    source: str = "manual"

@router.post("/")
async def create_requirement(req: RequirementCreate):
    return {"id": "req-123", "title": req.title, "status": "created"}

@router.get("/")
async def list_requirements():
    return [
        {"id": "REQ-1021", "title": "Add 2FA for User Login", "status": "active", "tests": 2},
        {"id": "REQ-1102", "title": "Checkout with 3D Secure", "status": "active", "tests": 5},
    ]
