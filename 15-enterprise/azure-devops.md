# Azure DevOps Integration

## Executive Summary
PAIOS integrates with Azure DevOps Pipelines as both a trigger source (pipeline runs invoke PAIOS workflows) and a reporting target (quality scores and go/no-go recommendations post back as pipeline check results), and links to Azure Boards work items for requirement traceability.

## Integration Points
- Pipeline task: `paios-run` invokes a [Workflow DSL](../13-workflow-engine/workflow-dsl.md) workflow.
- Work item linking: [Requirement Memory](../05-memory-engine/requirement-memory.md) syncs with Azure Boards.
- Self-hosted agent pool compatibility for on-premises browser executor pools.

## References
- [../13-workflow-engine/workflow-dsl.md](../13-workflow-engine/workflow-dsl.md)
