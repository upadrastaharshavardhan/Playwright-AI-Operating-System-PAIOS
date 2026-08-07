# Security Model

## Executive Summary
Security is enforced at every architectural layer: kernel-level task authentication, agent-level RBAC, and policy-engine-level governance of autonomous actions, with an immutable audit trail spanning all three.

## Diagram

```mermaid
graph TB
    REQ[Incoming Request/Task] --> AUTH[Authentication]
    AUTH --> AUTHZ[Authorization / RBAC]
    AUTHZ --> POL[Policy Engine]
    POL --> EXEC[Execution]
    EXEC --> AUDIT[Audit Log]
```

## References
- [rbac.md](rbac.md)
- [policy-engine.md](policy-engine.md)
