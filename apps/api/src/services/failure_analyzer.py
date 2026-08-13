import json
from typing import List, Dict

class FailureAnalyzer:
    """Layer 5: Root Cause Intelligence Agent v1"""

    CLASSIFICATION_RULES = [
        {"name": "locator_drift", "patterns": ["timeout waiting for selector", "strict mode violation", "element not found", "element not attached"], "weight": 1.0},
        {"name": "environment_issue", "patterns": ["net::err_", "connection_reset", "503 service unavailable", "dns failure", "timeout exceeded"], "weight": 0.9},
        {"name": "regression", "patterns": ["expect(", "toBeTruthy", "toHaveText", "toBeVisible", "assertion failed", "validation error"], "weight": 0.95},
        {"name": "flaky_test", "patterns": ["intermittent", "unstable", "passed on retry"], "weight": 0.8},
    ]

    def __init__(self, llm_router=None):
        self.llm = llm_router

    async def analyze(self, payload: dict) -> dict:
        failure = payload.get("failure", {})
        history = payload.get("history", [])
        classification = self._classify_heuristic(failure.get("error", ""))
        historical_match = self._match_history(failure, history)

        return {
            "failure_id": failure.get("id"),
            "classification": classification["type"],
            "confidence": classification["confidence"],
            "root_cause": classification["description"],
            "historical_pattern": historical_match,
            "suggested_action": self._suggest_action(classification["type"]),
            "is_recurring": historical_match["count"] > 0
        }

    def _classify_heuristic(self, error_message: str) -> dict:
        error_lower = error_message.lower()
        scores = []

        for rule in self.CLASSIFICATION_RULES:
            score = 0
            for pattern in rule["patterns"]:
                if pattern in error_lower:
                    score += rule["weight"]
            scores.append((rule["name"], score))

        scores.sort(key=lambda x: x[1], reverse=True)
        best_match = scores[0]

        descriptions = {
            "locator_drift": "UI element locator is stale or changed. DOM structure may have evolved.",
            "environment_issue": "Network or service instability. Not a product bug.",
            "regression": "Functional assertion failed. Likely real product regression.",
            "flaky_test": "Test is unstable. Needs hardening or environment fix."
        }

        return {"type": best_match[0], "confidence": min(best_match[1], 1.0), "description": descriptions.get(best_match[0], "Unknown")}

    def _match_history(self, failure: dict, history: List[dict]) -> dict:
        test_id = failure.get("test_id", "")
        matching = [h for h in history if h.get("test_id") == test_id]
        return {"count": len(matching), "last_occurrence": matching[-1] if matching else None, "trend": "increasing" if len(matching) > 2 else "stable"}

    def _suggest_action(self, classification: str) -> str:
        actions = {
            "locator_drift": "Run Self-Healing Engine to suggest updated locator",
            "environment_issue": "Check service health and retry. Escalate if persistent.",
            "regression": "File bug ticket. Assign to feature owner.",
            "flaky_test": "Add waits, stabilize test data, or refactor test."
        }
        return actions.get(classification, "Manual investigation required")

    async def classify(self, payload: dict) -> dict:
        return await self.analyze(payload)
