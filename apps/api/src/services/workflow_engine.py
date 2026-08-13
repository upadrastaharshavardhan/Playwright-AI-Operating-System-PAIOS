import uuid
from typing import Dict, List
from enum import Enum

class WorkflowStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class WorkflowEngine:
    """Layer 6: Workflow Engine - DSL-driven orchestration"""

    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.workflows: Dict[str, dict] = {}

    async def execute(self, payload: dict) -> dict:
        workflow_def = payload.get("workflow")
        variables = payload.get("variables", {})

        workflow_id = str(uuid.uuid4())
        self.workflows[workflow_id] = {
            "id": workflow_id,
            "status": WorkflowStatus.RUNNING,
            "steps_completed": [],
            "results": {}
        }

        steps = workflow_def.get("steps", [])
        for step in steps:
            result = await self._execute_step(step, variables)
            self.workflows[workflow_id]["steps_completed"].append(step["id"])
            self.workflows[workflow_id]["results"][step["id"]] = result

            if result.get("status") == "failed" and not step.get("continue_on_error"):
                self.workflows[workflow_id]["status"] = WorkflowStatus.FAILED
                return self.workflows[workflow_id]

        self.workflows[workflow_id]["status"] = WorkflowStatus.COMPLETED
        return self.workflows[workflow_id]

    async def _execute_step(self, step: dict, variables: dict) -> dict:
        step_type = step.get("type")

        if step_type == "agent":
            return {"status": "completed", "agent": step.get("agent"), "output": {}}
        elif step_type == "test_execution":
            from src.services.playwright_runner import PlaywrightRunner
            runner = PlaywrightRunner()
            return await runner.execute(step.get("payload", {}))
        elif step_type == "risk_assessment":
            from src.services.release_intelligence import ReleaseIntelligence
            ri = ReleaseIntelligence()
            return await ri.assess(step.get("payload", {}))
        elif step_type == "condition":
            return {"status": "completed", "condition_result": True}
        elif step_type == "parallel":
            import asyncio
            branches = step.get("branches", [])
            tasks = [self._execute_step(b, variables) for b in branches]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return {"status": "completed", "branch_results": results}

        return {"status": "completed", "step_type": step_type}
