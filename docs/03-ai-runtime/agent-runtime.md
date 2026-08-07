# Agent Runtime

## Executive Summary
Defines the isolated execution context each agent runs within: its own memory retrieval scope, tool access list, and LLM routing configuration.

## Context Structure
Each agent session carries: `role`, `scope` (product area / domain), `permissions` (from [RBAC](../17-security/rbac.md)), `memoryContext` (relevant retrieved memory), and `toolset` (allowed tool calls, see [tool-execution.md](tool-execution.md)).

## References
- [../04-agent-framework/agent-lifecycle.md](../04-agent-framework/agent-lifecycle.md)
