from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

class AgentRole(str, Enum):
    CHIEF_QA_OFFICER = "chief_qa_officer"
    REQUIREMENT_ANALYZER = "requirement_analyzer"
    TEST_DESIGNER = "test_designer"
    SELF_HEALING = "self_healing"
    ROOT_CAUSE = "root_cause"
    RELEASE_RISK = "release_risk"
    PERFORMANCE = "performance"
    ACCESSIBILITY = "accessibility"
    SECURITY = "security"

@dataclass
class AgentContract:
    role: AgentRole
    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]
    permissions: List[str]
    kg_write_nodes: List[str]

class AgentOrchestrator:
    """Layer 3: Multi-Agent Orchestrator (MCP)

    Hierarchical multi-agent system mirroring a real QA organization:
    Chief QA Officer -> Directors -> Departments -> Squads -> Workers
    """
    def __init__(self, event_bus, llm_router, knowledge_graph):
        self.event_bus = event_bus
        self.llm = llm_router
        self.kg = knowledge_graph
        self.agents: Dict[AgentRole, AgentContract] = self._init_agents()
        self._state = {}

    def _init_agents(self) -> Dict[AgentRole, AgentContract]:
        return {
            AgentRole.CHIEF_QA_OFFICER: AgentContract(
                role=AgentRole.CHIEF_QA_OFFICER,
                input_schema={"objective": str, "context": dict},
                output_schema={"plan": list, "risk_assessment": dict},
                permissions=["delegate", "read_all", "approve_release"],
                kg_write_nodes=["Strategy", "Decision"]
            ),
            AgentRole.REQUIREMENT_ANALYZER: AgentContract(
                role=AgentRole.REQUIREMENT_ANALYZER,
                input_schema={"requirement_text": str, "source": str},
                output_schema={"structured_req": dict, "test_scenarios": list},
                permissions=["read_requirements", "write_tests"],
                kg_write_nodes=["Requirement", "TestScenario"]
            ),
            AgentRole.TEST_DESIGNER: AgentContract(
                role=AgentRole.TEST_DESIGNER,
                input_schema={"scenarios": list, "template_id": str},
                output_schema={"test_cases": list, "coverage_map": dict},
                permissions=["read_templates", "write_tests"],
                kg_write_nodes=["Test", "Coverage"]
            ),
            AgentRole.SELF_HEALING: AgentContract(
                role=AgentRole.SELF_HEALING,
                input_schema={"failure": dict, "dom_snapshot": str, "screenshot": str},
                output_schema={"suggested_locator": str, "confidence": float, "change_log": dict},
                permissions=["read_tests", "write_tests"],
                kg_write_nodes=["HealingEvent", "LocatorChange"]
            ),
            AgentRole.ROOT_CAUSE: AgentContract(
                role=AgentRole.ROOT_CAUSE,
                input_schema={"failure": dict, "history": list},
                output_schema={"classification": str, "root_cause": str, "confidence": float},
                permissions=["read_executions", "read_failures"],
                kg_write_nodes=["Failure", "RootCause"]
            ),
            AgentRole.RELEASE_RISK: AgentContract(
                role=AgentRole.RELEASE_RISK,
                input_schema={"change_set": list, "history": dict},
                output_schema={"risk_score": float, "factors": list, "recommendation": str},
                permissions=["read_all"],
                kg_write_nodes=["RiskReport", "Release"]
            ),
        }

    async def orchestrate(self, objective: str, context: dict) -> dict:
        plan = await self.llm.plan(objective, context)
        results = {}
        for step in plan:
            agent_role = AgentRole(step.get("agent", "requirement_analyzer"))
            result = await self._execute_agent_step(agent_role, step["payload"])
            results[agent_role.value] = result
            await self.kg.persist_result(agent_role, result)

        return {
            "objective": objective,
            "plan": plan,
            "agent_results": results,
            "final_assessment": await self._aggregate_assessment(results)
        }

    async def _execute_agent_step(self, role: AgentRole, payload: dict) -> dict:
        if role == AgentRole.REQUIREMENT_ANALYZER:
            return await self._run_requirement_agent(payload)
        elif role == AgentRole.TEST_DESIGNER:
            return await self._run_test_designer(payload)
        elif role == AgentRole.SELF_HEALING:
            return await self._run_self_healing(payload)
        elif role == AgentRole.ROOT_CAUSE:
            return await self._run_root_cause(payload)
        elif role == AgentRole.RELEASE_RISK:
            return await self._run_release_risk(payload)
        return {"status": "not_implemented", "role": role.value}

    async def _run_requirement_agent(self, payload: dict) -> dict:
        model = self.llm.get_model()
        prompt = f"""Analyze this requirement and extract structured test scenarios.
Requirement: {payload.get('requirement_text')}
Source: {payload.get('source', 'manual')}
Return JSON with: scenarios (list), entities (list), relationships (list)"""
        response = await model.ainvoke(prompt)
        import json
        try:
            return json.loads(response.content)
        except:
            return {"scenarios": [], "raw": response.content}

    async def _run_test_designer(self, payload: dict) -> dict:
        from src.services.test_generator import TestGeneratorService
        gen = TestGeneratorService()
        return await gen.generate_from_scenarios(payload.get("scenarios", []))

    async def _run_self_healing(self, payload: dict) -> dict:
        from src.services.self_healing import SelfHealingEngine
        engine = SelfHealingEngine(self.llm)
        return await engine.heal(payload)

    async def _run_root_cause(self, payload: dict) -> dict:
        from src.services.failure_analyzer import FailureAnalyzer
        analyzer = FailureAnalyzer(self.llm)
        return await analyzer.classify(payload)

    async def _run_release_risk(self, payload: dict) -> dict:
        from src.services.release_intelligence import ReleaseIntelligence
        ri = ReleaseIntelligence(self.llm, self.kg)
        return await ri.calculate_risk(payload)

    async def _aggregate_assessment(self, results: dict) -> dict:
        model = self.llm.get_model()
        prompt = f"""Synthesize these agent outputs into a final release assessment.
Results: {results}
Provide: overall_risk_score (0-100), go_no_go (GO/NO-GO/CONDITIONAL), key_concerns (list), next_actions (list)"""
        response = await model.ainvoke(prompt)
        import json
        try:
            return json.loads(response.content)
        except:
            return {"raw_assessment": response.content, "risk_score": 50}
