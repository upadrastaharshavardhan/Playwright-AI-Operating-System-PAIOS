from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from typing import List

router = APIRouter()

class TestPackParseResponse(BaseModel):
    test_cases: List[dict]
    count: int
    module_breakdown: dict

@router.post("/upload")
async def upload_test_pack(file: UploadFile = File(...)):
    from src.services.test_generator import TestGeneratorService
    content = await file.read()
    gen = TestGeneratorService()
    test_cases = await gen.parse_test_pack(content, file.filename)

    module_breakdown = {}
    for tc in test_cases:
        mod = tc.get("module", "Unknown")
        module_breakdown[mod] = module_breakdown.get(mod, 0) + 1

    return TestPackParseResponse(
        test_cases=test_cases,
        count=len(test_cases),
        module_breakdown=module_breakdown
    )

@router.post("/generate")
async def generate_from_pack(payload: dict):
    from src.services.test_generator import TestGeneratorService
    gen = TestGeneratorService()
    return await gen.generate(payload)
