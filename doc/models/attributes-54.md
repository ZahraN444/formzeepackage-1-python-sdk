
# Attributes 54

## Structure

`Attributes54`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `output` | `Dict[str, object]` | Optional | Key Value map that contains the Task result. |
| `status` | [`PaymentSubmissionTaskStatusEnum`](../../doc/models/payment-submission-task-status-enum.md) | Optional | status of the submission task |

## Example (as JSON)

```json
{
  "output": {
    "outcome": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "status": "completed"
}
```

