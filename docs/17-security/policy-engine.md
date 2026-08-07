# Policy Engine

## Executive Summary
Governs what autonomous actions agents may take without human approval, evaluated against organization-defined policy rules (e.g., "no autonomous production release approval for services tagged `pci-scope`").

## Example Policy

```yaml
policy: restrict-autonomous-release
match:
  serviceTag: pci-scope
action: require_human_approval
```

## References
- [rbac.md](rbac.md)
- [../13-workflow-engine/human-approval.md](../13-workflow-engine/human-approval.md)
