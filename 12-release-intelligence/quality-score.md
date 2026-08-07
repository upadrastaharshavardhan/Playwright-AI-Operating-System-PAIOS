# Quality Score

## Executive Summary
A quantified 0–100 score representing release confidence, explainable by construction: every point deducted is traceable to a specific piece of evidence (a failing test, an unresolved historical failure signature, an uncovered requirement).

## Scoring Factors

| Factor | Weight |
|---|---|
| Test pass rate (risk-weighted) | 40% |
| Requirement coverage | 20% |
| Historical failure pattern recurrence | 20% |
| Code-change risk score | 20% |

## References
- [go-no-go.md](go-no-go.md)
