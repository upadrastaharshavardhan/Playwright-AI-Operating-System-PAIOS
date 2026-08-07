# Workflow DSL — Formal Specification

## Grammar (EBNF, simplified)
```
workflow    ::= "name:" STRING "trigger:" TRIGGER "steps:" step+
step        ::= "id:" STRING ("agent:" AGENT_REF)? "action:" ACTION ("dependsOn:" "[" STRING* "]")? ("condition:" EXPR)?
trigger     ::= "pull_request.merged" | "schedule.cron" | "manual" | "api.invoked"
```

Full worked examples in [docs/13-workflow-engine/workflow-dsl.md](../docs/13-workflow-engine/workflow-dsl.md).

## References
- [../docs/13-workflow-engine/workflow-dsl.md](../docs/13-workflow-engine/workflow-dsl.md)
