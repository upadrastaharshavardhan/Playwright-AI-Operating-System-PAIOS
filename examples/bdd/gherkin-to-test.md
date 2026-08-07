# Example: Gherkin to Playwright Test

```gherkin
Feature: Guest Checkout
  Scenario: Successful order with valid card
    Given a guest user is on the checkout page
    When they enter valid payment details
    Then their order is confirmed
```

PAIOS's Planner decomposes this into a generation task, producing the Playwright test shown in [playwright/generated-test-sample.md](../playwright/generated-test-sample.md).
