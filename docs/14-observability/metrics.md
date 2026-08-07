# Metrics Catalog

## Executive Summary
Key metrics exposed via a Prometheus-compatible endpoint.

| Metric | Type | Description |
|---|---|---|
| `paios_task_duration_seconds` | Histogram | Kernel task execution time |
| `paios_agent_confidence_score` | Gauge | Per-decision confidence |
| `paios_test_flakiness_score` | Gauge | Per-test flakiness |
| `paios_quality_score` | Gauge | Latest release quality score |

## References
- [dashboards.md](dashboards.md)
