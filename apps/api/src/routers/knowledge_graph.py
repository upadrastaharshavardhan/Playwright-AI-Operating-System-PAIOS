from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class QueryRequest(BaseModel):
    query_type: str
    parameters: dict = {}

@router.post("/query")
async def query_knowledge_graph(req: QueryRequest):
    queries = {
        "under_tested_requirements": {
            "description": "Requirements with insufficient test coverage",
            "cypher": "MATCH (r:Requirement) OPTIONAL MATCH (r)-[:COVERS]->(t:Test) WITH r, count(t) as tc WHERE tc < 3 RETURN r, tc",
            "results": []
        },
        "failure_prone_modules": {
            "description": "Components with highest failure rates",
            "cypher": "MATCH (c:Component)<-[:AFFECTS]-(f:Failure) RETURN c.name, count(f) ORDER BY count(f) DESC",
            "results": []
        },
        "test_failure_trend": {
            "description": "Failure trend over last 30 days",
            "cypher": "MATCH (f:Failure) WHERE f.detected > datetime() - duration('P30D') RETURN f",
            "results": []
        }
    }

    return {
        "query": req.query_type,
        "result": queries.get(req.query_type, {"error": "Unknown query"})
    }

@router.get("/schema")
async def get_schema():
    return {
        "nodes": ["Requirement", "Test", "Execution", "Failure", "Component", "Owner", "AgentOutput"],
        "relationships": [
            {"type": "COVERS", "from": "Requirement", "to": "Test"},
            {"type": "EXECUTED_AS", "from": "Test", "to": "Execution"},
            {"type": "RESULTED_IN", "from": "Execution", "to": "Failure"},
            {"type": "AFFECTS", "from": "Failure", "to": "Component"},
            {"type": "OWNED_BY", "from": "Component", "to": "Owner"},
            {"type": "DETECTED_IN", "from": "Failure", "to": "Execution"},
            {"type": "IMPACTS_PERF_OF", "from": "PerformanceMetric", "to": "Component"},
            {"type": "CONTRIBUTES_TO", "from": "AgentOutput", "to": "RiskReport"}
        ]
    }
