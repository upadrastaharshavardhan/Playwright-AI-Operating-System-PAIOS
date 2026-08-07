# Worker Layer

## Executive Summary
Worker agents execute single, well-defined tasks: generate one test, execute one suite, analyze one failure, repair one broken locator. Workers are stateless between tasks and always operate within a Squad's delegated scope.

## Example Worker Tasks
- `GenerateTestFromRequirement`
- `ExecuteSuite`
- `AnalyzeFailure`
- `RepairLocator`

## References
- [squad-layer.md](squad-layer.md)
- [../09-playwright-engine/locator-engine.md](../09-playwright-engine/locator-engine.md)
