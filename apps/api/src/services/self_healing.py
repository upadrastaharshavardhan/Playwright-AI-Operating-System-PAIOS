import json

class SelfHealingEngine:
    """Layer 5: Self-Healing Engine - DOM snapshot analysis and locator repair"""

    def __init__(self, llm_router):
        self.llm = llm_router

    async def heal(self, payload: dict) -> dict:
        failed_locator = payload.get("failed_locator")
        dom_snapshot = payload.get("dom_snapshot", "")
        error_message = payload.get("error_message", "")

        heuristic_result = self._heuristic_heal(failed_locator, dom_snapshot, error_message)
        if heuristic_result["confidence"] > 0.85:
            return heuristic_result

        return await self._llm_heal(failed_locator, dom_snapshot, error_message)

    def _heuristic_heal(self, locator: str, dom: str, error: str) -> dict:
        suggestions = []
        confidence = 0.0

        if locator.startswith("#"):
            element_name = locator[1:]
            suggestions.append(f'[data-testid="{element_name}"]')
            suggestions.append(f'text="{element_name}"')
            confidence = 0.75
        elif locator.startswith("."):
            class_name = locator[1:]
            suggestions.append(f"[class*='{class_name}']")
            confidence = 0.70
        elif "has-text" in locator:
            text = locator.split("has-text(")[1].split(")")[0].strip("'"")
            suggestions.append(f'text="{text}"')
            suggestions.append(f'role=button[name="{text}"]')
            confidence = 0.80

        return {
            "original_locator": locator,
            "suggested_locator": suggestions[0] if suggestions else locator,
            "alternatives": suggestions[1:],
            "confidence": confidence,
            "method": "heuristic",
            "change_log": {"timestamp": "auto", "reason": error, "approved": False}
        }

    async def _llm_heal(self, locator: str, dom: str, error: str) -> dict:
        model = self.llm.get_model()
        prompt = f"""You are the PAIOS Self-Healing Engine. A Playwright test failed because a locator broke.
Failed Locator: {locator}
Error: {error}
DOM Snapshot (truncated): {dom[:3000]}
Suggest the best replacement Playwright locator. Respond with JSON:
{{"suggested_locator": "...", "confidence": 0.0-1.0, "reasoning": "..."}}"""

        response = await model.ainvoke(prompt)
        try:
            result = json.loads(response.content)
            result["original_locator"] = locator
            result["method"] = "llm"
            result["change_log"] = {"timestamp": "auto", "reason": error, "approved": False}
            return result
        except:
            return {
                "original_locator": locator,
                "suggested_locator": locator,
                "confidence": 0.0,
                "method": "llm_failed",
                "raw_response": response.content
            }
