# Agent Permissions

## Executive Summary
Defines the capability boundary per agent tier, enforced by the kernel Security Manager and RBAC system.

## Permission Matrix

| Capability | Worker | Squad | Director | CQO |
|---|---|---|---|---|
| Generate test | ✅ | ✅ | ❌ | ❌ |
| Execute suite | ✅ | ✅ | ✅ | ❌ |
| Modify quality gate thresholds | ❌ | ❌ | ✅ | ✅ |
| Approve autonomous release | ❌ | ❌ | ❌ | ✅ (if policy allows) |

## References
- [../17-security/rbac.md](../17-security/rbac.md)
