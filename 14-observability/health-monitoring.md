# Health Monitoring

## Executive Summary
Every service exposes `/healthz` (liveness) and `/readyz` (readiness) endpoints; the Resource Manager consumes readiness signals when making scheduling decisions.

## References
- [../02-kernel/resource-manager.md](../02-kernel/resource-manager.md)
