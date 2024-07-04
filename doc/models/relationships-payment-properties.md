
# Relationships Payment Properties

## Structure

`RelationshipsPaymentProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | The payment associated with this query |
| `mtype` | `str` | Required, Constant | **Default**: `'payments'` |

## Example (as JSON)

```json
{
  "id": "00001186-0000-0000-0000-000000000000",
  "type": "payments"
}
```

