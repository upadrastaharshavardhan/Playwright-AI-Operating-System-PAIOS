# Task Manager

## Executive Summary
Manages the task queue, including dependency graphs between tasks (e.g., "generate test" must complete before "execute test").

## Dependency Model
Tasks form a DAG; the Task Manager topologically evaluates readiness before handing candidates to the [Scheduler](scheduler.md).

## References
- [scheduler.md](scheduler.md)
