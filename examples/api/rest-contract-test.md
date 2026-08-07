# Example: REST Contract Test

```typescript
test('POST /api/orders returns 201 with valid schema', async ({ request }) => {
  const response = await request.post('/api/orders', { data: validOrderPayload });
  expect(response.status()).toBe(201);
  expect(await response.json()).toMatchSchema(orderResponseSchema);
});
```

See [docs/11-api-intelligence/contract-testing.md](../../docs/11-api-intelligence/contract-testing.md).
