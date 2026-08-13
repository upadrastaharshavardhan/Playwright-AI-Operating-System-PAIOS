from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from src.core.config import settings

class LLMRouter:
    """Layer 2: AI Runtime - LLM routing, planning, and reasoning"""
    def __init__(self):
        self._models = {}
        if settings.OPENAI_API_KEY:
            self._models["gpt-4o"] = ChatOpenAI(model="gpt-4o", api_key=settings.OPENAI_API_KEY)
            self._models["gpt-4o-mini"] = ChatOpenAI(model="gpt-4o-mini", api_key=settings.OPENAI_API_KEY)
        if settings.ANTHROPIC_API_KEY:
            self._models["claude-3-5-sonnet"] = ChatAnthropic(
                model="claude-3-5-sonnet-20240620", api_key=settings.ANTHROPIC_API_KEY)

    def get_model(self, model_id: Optional[str] = None):
        if model_id and model_id in self._models:
            return self._models[model_id]
        return self._models.get("gpt-4o") or list(self._models.values())[0]

    async def plan(self, objective: str, context: dict, model_id: Optional[str] = None):
        model = self.get_model(model_id)
        prompt = f"""You are the PAIOS AI Runtime Planner. Decompose this quality engineering objective into structured tasks.
Objective: {objective}
Context: {context}
Respond with JSON array of tasks: [{{"task_type": "...", "payload": {{...}}, "priority": 1-10}}]"""
        response = await model.ainvoke(prompt)
        import json
        try:
            return json.loads(response.content)
        except:
            return [{"task_type": "generate_tests", "payload": {"requirement": objective}, "priority": 5}]

    async def reason(self, question: str, evidence: dict, model_id: Optional[str] = None):
        model = self.get_model(model_id)
        prompt = f"""Analyze this quality engineering evidence and answer the question.
Question: {question}
Evidence: {evidence}
Provide a structured reasoning response with confidence score."""
        return await model.ainvoke(prompt)

    async def reflect(self, execution_result: dict, model_id: Optional[str] = None):
        model = self.get_model(model_id)
        prompt = f"""Reflect on this test execution result. What patterns, failures, or insights should be remembered?
Result: {execution_result}"""
        return await model.ainvoke(prompt)
