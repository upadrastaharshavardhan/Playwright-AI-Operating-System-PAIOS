from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ExecuteRequest(BaseModel):
    tests: List[dict]
    browser: str = "chromium"
    headless: bool = True

@router.post("/run")
async def run_tests(req: ExecuteRequest):
    task = {
        "task_type": "execute_playwright",
        "payload": req.dict(),
        "priority": 5
    }
    return {
        "status": "scheduled",
        "message": "Execution task submitted to kernel scheduler",
        "task": task
    }

@router.get("/{execution_id}")
async def get_execution(execution_id: str):
    return {
        "execution_id": execution_id,
        "status": "completed",
        "results": []
    }
