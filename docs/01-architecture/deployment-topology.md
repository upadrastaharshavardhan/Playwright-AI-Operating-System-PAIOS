# Deployment Topology

## Executive Summary
Reference topologies for small teams, mid-size organizations, and large enterprises.

## Topology Tiers

| Tier | Kernel Nodes | Worker Pools | Notes |
|---|---|---|---|
| Small Team | 1 (HA optional) | 1 | Single-cluster, single-region |
| Mid-Size Org | 3 (HA) | Per product area | Multi-namespace Kubernetes |
| Enterprise | 3+ per region | Per team, per region | Multi-region with memory federation (Horizon 2) |

See [docs/15-enterprise/kubernetes.md](../15-enterprise/kubernetes.md) for manifests and Helm chart references.

## References
- [availability.md](availability.md)
