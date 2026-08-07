# Layered Architecture

## Executive Summary
PAIOS's 8-layer model (Kernel → AI Runtime → Agent Framework → Knowledge/Memory → Domain Intelligence → Workflow/Release → Marketplace/SDK → Enterprise Integration) enforces strict downward-only dependency direction: higher layers depend on lower layers, never the reverse.

## Purpose
Prevent architectural erosion as the system grows by giving every engineer a clear rule for where new code belongs.

## Layer Contracts

| Layer | May Depend On | May NOT Depend On |
|---|---|---|
| Kernel | Nothing (foundation) | Any higher layer |
| AI Runtime | Kernel | Agent Framework and above |
| Agent Framework | AI Runtime, Kernel | Domain Intelligence internals |
| Knowledge/Memory | Kernel | Agent Framework (agents depend on it, not vice versa) |
| Domain Intelligence | Kernel, Playwright Engine | Workflow/Release |
| Workflow/Release | All lower layers | Marketplace/SDK |
| Marketplace/SDK | All lower layers | Enterprise Integration |
| Enterprise Integration | All lower layers | — |

## Design Rationale
This mirrors the layered-kernel design pattern used in Linux (syscalls → VFS → drivers) and in Kubernetes (API server → controllers → kubelet), where strict layering prevents circular dependencies and enables independent evolution and testing of each layer.

## Anti-Patterns
- A Domain Intelligence engine calling directly into the Workflow Engine (layer violation — should emit an event instead).
- An Enterprise Connector reading Kernel state directly instead of through the Agent Framework API.

## References
- [system-overview.md](system-overview.md)
- [component-model.md](component-model.md)
