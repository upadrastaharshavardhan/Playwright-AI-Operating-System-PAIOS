import os
import uuid
import asyncio
from typing import List
from playwright.async_api import async_playwright

class PlaywrightRunner:
    """Layer 9: Playwright Execution Engine"""

    def __init__(self):
        self.results_dir = "./test-results"
        os.makedirs(self.results_dir, exist_ok=True)

    async def execute(self, payload: dict) -> dict:
        tests = payload.get("tests", [])
        browser_type = payload.get("browser", "chromium")
        headless = payload.get("headless", True)

        results = []
        async with async_playwright() as p:
            browser = await getattr(p, browser_type).launch(headless=headless)
            context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                record_video_dir=f"{self.results_dir}/videos"
            )

            for test in tests:
                result = await self._run_single_test(context, test)
                results.append(result)

            await context.close()
            await browser.close()

        return {
            "execution_id": str(uuid.uuid4()),
            "total": len(results),
            "passed": sum(1 for r in results if r["status"] == "passed"),
            "failed": sum(1 for r in results if r["status"] == "failed"),
            "results": results
        }

    async def _run_single_test(self, context, test: dict) -> dict:
        page = await context.new_page()
        test_id = test.get("id", str(uuid.uuid4()))
        start_time = asyncio.get_event_loop().time()

        try:
            steps = test.get("steps", [])
            for step in steps:
                await self._execute_step(page, step)

            duration = (asyncio.get_event_loop().time() - start_time) * 1000
            screenshot_path = f"{self.results_dir}/{test_id}-passed.png"
            await page.screenshot(path=screenshot_path)
            await page.close()

            return {
                "test_id": test_id,
                "status": "passed",
                "duration_ms": int(duration),
                "screenshot": screenshot_path
            }
        except Exception as e:
            duration = (asyncio.get_event_loop().time() - start_time) * 1000
            screenshot_path = f"{self.results_dir}/{test_id}-failed.png"
            try:
                await page.screenshot(path=screenshot_path)
            except:
                pass
            await page.close()
            return {
                "test_id": test_id,
                "status": "failed",
                "duration_ms": int(duration),
                "error": str(e),
                "screenshot": screenshot_path,
                "failure_type": self._classify_error(str(e))
            }

    async def _execute_step(self, page, step: dict):
        action = step.get("action")
        selector = step.get("selector")
        value = step.get("value", "")

        if action == "goto":
            await page.goto(value)
        elif action == "fill":
            await page.locator(selector).fill(value)
        elif action == "click":
            await page.locator(selector).click()
        elif action == "expect_visible":
            from playwright.async_api import expect
            await expect(page.locator(selector)).toBeVisible()
        elif action == "expect_text":
            from playwright.async_api import expect
            await expect(page.locator(selector)).toHaveText(value)

    def _classify_error(self, error: str) -> str:
        error_lower = error.lower()
        if "timeout" in error_lower and "locator" in error_lower:
            return "locator_drift"
        elif "net::" in error_lower or "err_" in error_lower:
            return "environment_issue"
        elif "strict mode" in error_lower:
            return "locator_drift"
        elif "expect" in error_lower:
            return "regression"
        return "unknown"
