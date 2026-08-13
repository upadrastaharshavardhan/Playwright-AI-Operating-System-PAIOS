"""
PAIOS - Playwright AI Operating System
Main FastAPI Application Entry Point
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from src.core.config import settings
from src.core.database import init_db
from src.core.event_bus import EventBus
from src.core.scheduler import KernelScheduler
from src.routers import (
    agents, auth, dashboard, executions, knowledge_graph,
    memory, plugins, releases, requirements, templates,
    test_packs, workflows,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    app.state.event_bus = EventBus()
    app.state.scheduler = KernelScheduler(app.state.event_bus)
    await app.state.scheduler.start()
    yield
    await app.state.scheduler.stop()

app = FastAPI(
    title="PAIOS API",
    description="AI-Native OS for Quality Engineering",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(agents.router, prefix="/api/v1/agents", tags=["Layer 3: Agent Framework"])
app.include_router(requirements.router, prefix="/api/v1/requirements", tags=["Layer 5: Domain Intelligence"])
app.include_router(templates.router, prefix="/api/v1/templates", tags=["Layer 5: Domain Intelligence"])
app.include_router(test_packs.router, prefix="/api/v1/test-packs", tags=["Layer 5: Domain Intelligence"])
app.include_router(executions.router, prefix="/api/v1/executions", tags=["Layer 1: Kernel / Layer 9: Playwright"])
app.include_router(knowledge_graph.router, prefix="/api/v1/knowledge-graph", tags=["Layer 4: Knowledge & Memory"])
app.include_router(memory.router, prefix="/api/v1/memory", tags=["Layer 4: Knowledge & Memory"])
app.include_router(releases.router, prefix="/api/v1/releases", tags=["Layer 6: Release Intelligence"])
app.include_router(workflows.router, prefix="/api/v1/workflows", tags=["Layer 6: Workflow Engine"])
app.include_router(plugins.router, prefix="/api/v1/plugins", tags=["Layer 7: Plugin SDK"])
app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["Observability"])

@app.get("/health")
async def health_check():
    return {"status": "healthy", "system": "PAIOS", "layers": 8}

@app.get("/")
async def root():
    return {
        "name": "PAIOS - Playwright AI Operating System",
        "version": "1.0.0",
        "tagline": "From Automation to Autonomy",
        "layers": [
            "Layer 1: Kernel",
            "Layer 2: AI Runtime",
            "Layer 3: Agent Framework",
            "Layer 4: Knowledge & Memory",
            "Layer 5: Domain Intelligence",
            "Layer 6: Workflow & Release Intelligence",
            "Layer 7: Marketplace & Plugin SDK",
            "Layer 8: Enterprise Integration",
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
