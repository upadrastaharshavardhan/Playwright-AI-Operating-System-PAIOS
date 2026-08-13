from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class WorkflowExecute(BaseModel):
    workflow: dict
    variables: dict = {}

@router.post("/execute")
async def execute_workflow(req: WorkflowExecute):
    from src.services.workflow_engine import WorkflowEngine
    from src.core.event_bus import EventBus
    engine = WorkflowEngine(EventBus())
    return await engine.execute(req.dict())
