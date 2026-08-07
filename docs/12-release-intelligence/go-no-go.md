# Go/No-Go Recommendation

## Executive Summary
The final human-facing output: a Go, No-Go, or Go-with-conditions recommendation, always accompanied by the evidence chain from the [Knowledge Graph](../06-knowledge-graph/README.md) supporting the recommendation.

## Example Output
```json
{
  "recommendation": "GO_WITH_CONDITIONS",
  "qualityScore": 82,
  "conditions": ["Manual verification of payment-retry flow recommended — historical flakiness detected"],
  "evidenceRefs": ["failure:sig-4471", "test:checkout-retry-003"]
}
```

## References
- [quality-score.md](quality-score.md)
