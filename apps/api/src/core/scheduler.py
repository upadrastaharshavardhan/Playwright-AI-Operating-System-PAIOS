import asyncio
import uuid
from typing import Dict, Optional
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "pending"
    SCHEDULED = "scheduled"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class KernelTask:
    """Layer 1: Kernel - Process scheduling and resource arbitration"""
    def __init__(self, task_type: str, payload: dict, priority: int = 5):
        self.id = str(uuid.uuid4())
        self.task_type = task_type
        self.payload = payload
        self.priority = priority
        self.status = TaskStatus.PENDING
        self.created_at = datetime.utcnow()
        self.started_at: Optional[datetime] = None
        self.completed_at: Optional[datetime] = None
        self.result: Optional[dict] = None

class KernelScheduler:
    """PAIOS Kernel Scheduler - manages execution of all quality engineering tasks"""
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.tasks: Dict[str, KernelTask] = {}
        self._queue = asyncio.PriorityQueue()
        self._running = False
        self._workers = []

    async def start(self):
        self._running = True
        for i in range(4):
            worker = asyncio.create_task(self._worker_loop(f"worker-{i}"))
            self._workers.append(worker)
        await self.event_bus.publish(PAIEvent(
            layer="L1", agent="KernelScheduler",
            event_type="kernel.started", payload={"workers": 4}
        ))

    async def stop(self):
        self._running = False
        for w in self._workers:
            w.cancel()

    async def submit(self, task: KernelTask) -> str:
        self.tasks[task.id] = task
        await self._queue.put((task.priority, task.created_at.timestamp(), task.id))
        task.status = TaskStatus.SCHEDULED
        return task.id

    async def _worker_loop(self, worker_id: str):
        while self._running:
            try:
                _, _, task_id = await asyncio.wait_for(self._queue.get(), timeout=1.0)
                task = self.tasks[task_id]
                task.status = TaskStatus.RUNNING
                task.started_at = datetime.utcnow()
                result = await self._execute_task(task)
                task.status = TaskStatus.COMPLETED
                task.completed_at = datetime.utcnow()
                task.result = result
                await self.event_bus.publish(PAIEvent(
                    layer="L1", agent=worker_id,
                    event_type=f"task.completed.{task.task_type}",
                    payload={"task_id": task.id, "result": result}
                ))
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                if task_id in self.tasks:
                    self.tasks[task_id].status = TaskStatus.FAILED
                    self.tasks[task_id].result = {"error": str(e)}

    async def _execute_task(self, task: KernelTask) -> dict:
        handlers = {
            "generate_tests": self._handle_generate,
            "execute_playwright": self._handle_execution,
            "analyze_failure": self._handle_failure_analysis,
            "assess_release": self._handle_release_assessment,
            "run_workflow": self._handle_workflow,
        }
        handler = handlers.get(task.task_type, self._default_handler)
        return await handler(task)

    async def _handle_generate(self, task: KernelTask) -> dict:
        from src.services.test_generator import TestGeneratorService
        gen = TestGeneratorService()
        return await gen.generate(task.payload)

    async def _handle_execution(self, task: KernelTask) -> dict:
        from src.services.playwright_runner import PlaywrightRunner
        runner = PlaywrightRunner()
        return await runner.execute(task.payload)

    async def _handle_failure_analysis(self, task: KernelTask) -> dict:
        from src.services.failure_analyzer import FailureAnalyzer
        analyzer = FailureAnalyzer()
        return await analyzer.analyze(task.payload)

    async def _handle_release_assessment(self, task: KernelTask) -> dict:
        from src.services.release_intelligence import ReleaseIntelligence
        ri = ReleaseIntelligence()
        return await ri.assess(task.payload)

    async def _handle_workflow(self, task: KernelTask) -> dict:
        from src.services.workflow_engine import WorkflowEngine
        engine = WorkflowEngine(self.event_bus)
        return await engine.execute(task.payload)

    async def _default_handler(self, task: KernelTask) -> dict:
        return {"status": "unknown_task_type", "task_type": task.task_type}

from src.core.event_bus import PAIEvent
