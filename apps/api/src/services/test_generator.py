import uuid
from typing import List
from jinja2 import Template

class TestGeneratorService:
    """Layer 5 + 9: Domain Intelligence + Playwright Engine - Test generation"""

    DEFAULT_TEMPLATE = '''
import { test, expect } from '@playwright/test';

test('{{scenario}}', async ({ page }) => {
  {% if url %}await page.goto('{{url}}');{% endif %}
  {% for step in steps %}
  {% if step.action == 'fill' %}
  await page.locator('{{step.selector}}').fill('{{step.value}}');
  {% elif step.action == 'click' %}
  await page.locator('{{step.selector}}').click();
  {% elif step.action == 'expect_visible' %}
  await expect(page.locator('{{step.selector}}')).toBeVisible();
  {% elif step.action == 'expect_text' %}
  await expect(page.locator('{{step.selector}}')).toHaveText('{{step.value}}');
  {% endif %}
  {% endfor %}
});
'''

    MODULE_FIELD_MAP = {
        "Login": {
            "Username": "input[name='username']",
            "Password": "input[name='password']",
            "LoginButton": "button[type='submit']",
            "Expected": ".dashboard"
        },
        "Search": {
            "SearchBox": "input[placeholder*='Search']",
            "SearchButton": "button:has-text('Search')",
            "Expected": ".results"
        },
        "Checkout": {
            "CardNumber": "input[name='card']",
            "Expiry": "input[name='expiry']",
            "PayButton": "button:has-text('Pay')",
            "Expected": ".confirmation"
        }
    }

    async def generate(self, payload: dict) -> dict:
        test_cases = payload.get("test_cases", [])
        template_str = payload.get("template", self.DEFAULT_TEMPLATE)
        template = Template(template_str)

        generated = []
        for tc in test_cases:
            code = self._render_test(template, tc)
            generated.append({
                "id": str(uuid.uuid4()),
                "module": tc.get("module", "Unknown"),
                "scenario": tc.get("scenario", ""),
                "code": code,
                "filename": f"{tc.get('module', 'test').lower()}_{tc.get('tc_id', 'tc')}.spec.ts"
            })

        return {"generated_tests": generated, "count": len(generated)}

    async def generate_from_scenarios(self, scenarios: List[dict]) -> dict:
        test_cases = []
        for sc in scenarios:
            tc = {
                "tc_id": sc.get("id", str(uuid.uuid4())),
                "module": sc.get("module", "General"),
                "scenario": sc.get("name", ""),
                "url": sc.get("url", "/"),
                "steps": sc.get("steps", [])
            }
            test_cases.append(tc)
        return await self.generate({"test_cases": test_cases})

    def _render_test(self, template: Template, tc: dict) -> str:
        module = tc.get("module", "")
        field_map = self.MODULE_FIELD_MAP.get(module, {})

        steps = []
        for key, value in tc.get("test_data", {}).items():
            if key in ["URL", "url"]:
                continue
            selector = field_map.get(key, f"[data-testid='{key.lower()}']")
            steps.append({"action": "fill", "selector": selector, "value": value})

        expected = tc.get("expected", field_map.get("Expected", "body"))
        steps.append({"action": "expect_visible", "selector": expected, "value": ""})

        return template.render(
            scenario=tc.get("scenario", "Test"),
            url=tc.get("url", tc.get("test_data", {}).get("URL", "/")),
            steps=steps
        )

    async def parse_test_pack(self, file_content: bytes, filename: str) -> List[dict]:
        import pandas as pd
        if filename.endswith('.csv'):
            df = pd.read_csv(pd.io.common.BytesIO(file_content))
        else:
            df = pd.read_excel(pd.io.common.BytesIO(file_content))

        records = df.to_dict('records')
        test_cases = []
        for i, row in enumerate(records):
            test_data = {k: v for k, v in row.items() if k not in ["TC_ID", "Module", "Test Scenario", "Expected"]}
            test_cases.append({
                "tc_id": str(row.get("TC_ID", f"TC_{i+1}")),
                "module": row.get("Module", "General"),
                "scenario": row.get("Test Scenario", ""),
                "test_data": test_data,
                "expected": row.get("Expected", "")
            })
        return test_cases
