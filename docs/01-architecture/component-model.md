# Component Model

## Executive Summary
Every PAIOS component conforms to a standard contract: a typed input schema, a typed output schema, an idempotency key, and an emitted set of events.

## Standard Component Interface

```typescript
interface PAIOSComponent<TInput, TOutput> {
  id: string;
  version: string;
  execute(input: TInput, ctx: ExecutionContext): Promise<TOutput>;
  emits: EventDescriptor[];
  requiredPermissions: Permission[];
}
```

## Design Rationale
Standardizing the component contract enables the [Plugin SDK](../16-plugin-sdk/README.md) to treat first-party and third-party components identically.

## References
- [communication.md](communication.md)
