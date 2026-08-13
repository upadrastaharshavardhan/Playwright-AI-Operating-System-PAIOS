from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_memory():
    return {"entries": 1247, "types": ["test", "failure", "requirement", "execution"]}
