# Component Contract Specification

```typescript
interface PAIOSComponent<TInput, TOutput> {
  id: string;
  version: string;
  execute(input: TInput, ctx: ExecutionContext): Promise<TOutput>;
  emits: EventDescriptor[];
  requiredPermissions: Permission[];
}
```

## References
- [../docs/01-architecture/component-model.md](../docs/01-architecture/component-model.md)
