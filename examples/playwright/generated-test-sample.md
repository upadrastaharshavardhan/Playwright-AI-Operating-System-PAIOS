# Example: PAIOS-Generated Playwright Test

```typescript
import { test, expect } from '@playwright/test';

test('guest user can complete checkout with a valid card', async ({ page }) => {
  await page.goto('/checkout');
  await page.getByRole('button', { name: 'Continue as Guest' }).click();
  await page.getByLabel('Email').fill('guest@example.com');
  await page.getByLabel('Card Number').fill('4242424242424242');
  await page.getByRole('button', { name: 'Place Order' }).click();
  await expect(page.getByText('Order Confirmed')).toBeVisible();
});
```

Generated using accessible-role locators per the [Locator Engine](../../docs/09-playwright-engine/locator-engine.md) priority order.
