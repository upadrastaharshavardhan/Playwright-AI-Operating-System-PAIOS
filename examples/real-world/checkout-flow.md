# Example: Checkout Flow Quality Validation

## Scenario
An e-commerce team merges a change to the guest checkout flow. This walks through what PAIOS does end to end.

## Steps
1. PR merge triggers the `pre-release-gate` [workflow](../../docs/13-workflow-engine/workflow-dsl.md).
2. [Risk Analysis](../../docs/12-release-intelligence/risk-analysis.md) determines the diff touches `checkout-service` and `payment-widget`.
3. The Squad agent owning Guest Checkout is delegated the targeted regression task.
4. Worker agents execute the existing suite and generate one new test for the changed validation logic.
5. A [Quality Score](../../docs/12-release-intelligence/quality-score.md) of 91 is computed; a [Go recommendation](../../docs/12-release-intelligence/go-no-go.md) is posted to the PR.

## References
- [../../docs/04-agent-framework/squad-layer.md](../../docs/04-agent-framework/squad-layer.md)
