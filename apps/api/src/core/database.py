from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, JSON, Integer, Float, Text
from datetime import datetime
from src.core.config import settings

Base = declarative_base()
engine = create_async_engine(settings.DATABASE_URL, echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class MemoryEntry(Base):
    __tablename__ = "memory_entries"
    id = Column(String, primary_key=True)
    type = Column(String, index=True)
    content = Column(JSON)
    embedding_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class ExecutionRecord(Base):
    __tablename__ = "executions"
    id = Column(String, primary_key=True)
    test_id = Column(String, index=True)
    status = Column(String)
    duration_ms = Column(Integer)
    trace_path = Column(String, nullable=True)
    screenshot_path = Column(String, nullable=True)
    failure_reason = Column(Text, nullable=True)
    root_cause = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class TestCase(Base):
    __tablename__ = "test_cases"
    id = Column(String, primary_key=True)
    module = Column(String, index=True)
    scenario = Column(Text)
    test_data = Column(JSON)
    template_id = Column(String)
    generated_code = Column(Text)
    status = Column(String, default="draft")

class Requirement(Base):
    __tablename__ = "requirements"
    id = Column(String, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    source = Column(String)
    metadata = Column(JSON)
    coverage_score = Column(Float, default=0.0)

class ReleaseAssessment(Base):
    __tablename__ = "release_assessments"
    id = Column(String, primary_key=True)
    version = Column(String)
    risk_score = Column(Float)
    go_no_go = Column(String)
    impacted_modules = Column(JSON)
    recommendations = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with async_session() as session:
        yield session
