import json
from typing import Dict, List
from datetime import datetime

class ReleaseIntelligence:
    """Layer 6: Release Intelligence - Risk scoring and go/no-go decisions"""

    def __init__(self, llm_router=None, knowledge_graph=None):
        self.llm = llm_router
        self.kg = knowledge_graph

    async def assess(self, payload: dict) -> dict:
        change_set = payload.get("change_set", [])
        version = payload.get("version", "unknown")

        component_scores = await self._calculate_component_risk(change_set)
        total_score = sum(c["score"] * c["weight"] for c in component_scores)
        total_weight = sum(c["weight"] for c in component_scores)
        risk_score = total_score / total_weight if total_weight > 0 else 50

        go_no_go = self._determine_go_no_go(risk_score, component_scores)

        return {
            "version": version,
            "risk_score": round(risk_score, 2),
            "go_no_go": go_no_go["decision"],
            "confidence": go_no_go["confidence"],
            "component_breakdown": component_scores,
            "recommendations": self._generate_recommendations(component_scores),
            "timestamp": datetime.utcnow().isoformat()
        }

    async def calculate_risk(self, payload: dict) -> dict:
        return await self.assess(payload)

    async def _calculate_component_risk(self, change_set: List[dict]) -> List[dict]:
        scores = []
        for change in change_set:
            module = change.get("module", "unknown")
            files_changed = change.get("files_changed", 0)
            lines_changed = change.get("lines_changed", 0)
            hist_failure_rate = 0.3
            coverage = change.get("coverage", 0.5)
            coverage_gap = 1 - coverage
            criticality = change.get("criticality", 0.5)

            change_impact = min((files_changed * 0.1) + (lines_changed * 0.001), 1.0)
            score = (change_impact * 0.30 + hist_failure_rate * 0.40 + coverage_gap * 0.20 + criticality * 0.10) * 100

            scores.append({
                "module": module,
                "score": round(score, 2),
                "weight": files_changed + 1,
                "factors": {
                    "change_impact": round(change_impact, 2),
                    "historical_failure_rate": hist_failure_rate,
                    "coverage_gap": round(coverage_gap, 2),
                    "business_criticality": criticality
                }
            })

        return sorted(scores, key=lambda x: x["score"], reverse=True)

    def _determine_go_no_go(self, risk_score: float, components: List[dict]) -> dict:
        if risk_score < 30:
            return {"decision": "GO", "confidence": 0.9}
        elif risk_score < 60:
            return {"decision": "CONDITIONAL", "confidence": 0.7}
        elif risk_score < 80:
            return {"decision": "NO-GO", "confidence": 0.8}
        else:
            return {"decision": "NO-GO", "confidence": 0.95}

    def _generate_recommendations(self, components: List[dict]) -> List[str]:
        recs = []
        high_risk = [c for c in components if c["score"] > 70]
        if high_risk:
            recs.append(f"Fix failing tests in: {', '.join(c['module'] for c in high_risk[:3])}")

        low_coverage = [c for c in components if c["factors"]["coverage_gap"] > 0.5]
        if low_coverage:
            recs.append(f"Add tests for: {', '.join(c['module'] for c in low_coverage[:3])}")

        if not recs:
            recs.append("All signals green. Proceed with standard validation.")

        return recs
