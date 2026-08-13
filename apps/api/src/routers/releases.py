from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

class ReleaseAssessmentRequest(BaseModel):
    version: str
    change_set: List[dict]
    pr_id: str = ""

@router.post("/assess")
async def assess_release(req: ReleaseAssessmentRequest):
    from src.services.release_intelligence import ReleaseIntelligence
    ri = ReleaseIntelligence()
    return await ri.assess(req.dict())

@router.get("/history")
async def get_release_history():
    return [
        {"version": "v1.24.0-rc.3", "risk_score": 72, "go_no_go": "NO-GO", "date": "2025-05-20"},
        {"version": "v1.23.5", "risk_score": 24, "go_no_go": "GO", "date": "2025-05-15"},
        {"version": "v1.23.4", "risk_score": 45, "go_no_go": "CONDITIONAL", "date": "2025-05-10"},
    ]
