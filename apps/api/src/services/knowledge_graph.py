from neo4j import AsyncGraphDatabase
from src.core.config import settings

class KnowledgeGraphService:
    """Layer 4: Knowledge Graph - Neo4j implementation"""
    def __init__(self):
        self.driver = AsyncGraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
        )

    async def init_schema(self):
        async with self.driver.session() as session:
            await session.run("CREATE CONSTRAINT requirement_id IF NOT EXISTS FOR (r:Requirement) REQUIRE r.id IS UNIQUE")
            await session.run("CREATE CONSTRAINT test_id IF NOT EXISTS FOR (t:Test) REQUIRE t.id IS UNIQUE")
            await session.run("CREATE CONSTRAINT component_id IF NOT EXISTS FOR (c:Component) REQUIRE c.id IS UNIQUE")

    async def create_requirement(self, req_id: str, title: str, metadata: dict):
        async with self.driver.session() as session:
            await session.run("""
                MERGE (r:Requirement {id: $id})
                SET r.title = $title, r.metadata = $metadata, r.updated = datetime()
            """, id=req_id, title=title, metadata=metadata)

    async def create_test(self, test_id: str, module: str, scenario: str, req_id: str = None):
        async with self.driver.session() as session:
            await session.run("""
                MERGE (t:Test {id: $id})
                SET t.module = $module, t.scenario = $scenario, t.updated = datetime()
            """, id=test_id, module=module, scenario=scenario)
            if req_id:
                await session.run("""
                    MATCH (r:Requirement {id: $req_id}), (t:Test {id: $test_id})
                    MERGE (r)-[:COVERS]->(t)
                """, req_id=req_id, test_id=test_id)

    async def record_execution(self, exec_id: str, test_id: str, result: str, failure_id: str = None):
        async with self.driver.session() as session:
            await session.run("""
                MERGE (e:Execution {id: $id})
                SET e.result = $result, e.run_at = datetime()
            """, id=exec_id, result=result)
            await session.run("""
                MATCH (t:Test {id: $test_id}), (e:Execution {id: $exec_id})
                MERGE (t)-[:EXECUTED_AS]->(e)
            """, test_id=test_id, exec_id=exec_id)
            if failure_id:
                await session.run("""
                    MERGE (f:Failure {id: $failure_id})
                    SET f.detected = datetime()
                    WITH f
                    MATCH (e:Execution {id: $exec_id})
                    MERGE (e)-[:RESULTED_IN]->(f)
                """, failure_id=failure_id, exec_id=exec_id)

    async def query_under_tested_requirements(self):
        async with self.driver.session() as session:
            result = await session.run("""
                MATCH (r:Requirement)
                OPTIONAL MATCH (r)-[:COVERS]->(t:Test)
                WITH r, count(t) as test_count
                WHERE test_count < 3
                RETURN r.id as req_id, r.title as title, test_count
                ORDER BY test_count ASC
            """)
            return [record.data() async for record in result]

    async def query_failure_prone_modules(self):
        async with self.driver.session() as session:
            result = await session.run("""
                MATCH (c:Component)<-[:AFFECTS]-(f:Failure)
                RETURN c.name as component, count(f) as failure_count
                ORDER BY failure_count DESC
                LIMIT 10
            """)
            return [record.data() async for record in result]

    async def persist_result(self, agent_role, result: dict):
        import uuid
        async with self.driver.session() as session:
            node_id = str(uuid.uuid4())
            await session.run("""
                MERGE (a:AgentOutput {id: $id})
                SET a.agent = $agent, a.result = $result, a.created = datetime()
            """, id=node_id, agent=agent_role.value if hasattr(agent_role, 'value') else str(agent_role), result=result)

    async def close(self):
        await self.driver.close()
