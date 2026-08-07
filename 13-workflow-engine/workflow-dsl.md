# Workflow DSL

## Executive Summary
A declarative YAML-based DSL for defining quality workflows, referenced throughout this documentation set.

## Example

```yaml
name: pre-release-gate
trigger: pull_request.merged
steps:
  - id: risk-analysis
    agent: director:functional
    action: analyze_risk
  - id: targeted-regression
    agent: squad:*
    action: execute_targeted_suite
    dependsOn: [risk-analysis]
  - id: score
    action: compute_quality_score
    dependsOn: [targeted-regression]
  - id: approval
    type: human_approval
    condition: "score < 85"
    dependsOn: [score]
```

## References
- [human-approval.md](human-approval.md)
