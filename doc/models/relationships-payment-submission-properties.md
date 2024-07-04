
# Relationships Payment Submission Properties

## Structure

`RelationshipsPaymentSubmissionProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | The payment submission associated with this query |
| `mtype` | `str` | Required, Constant | **Default**: `'payment_submissions'` |

## Example (as JSON)

```json
{
  "id": "00000472-0000-0000-0000-000000000000",
  "type": "payment_submissions"
}
```

