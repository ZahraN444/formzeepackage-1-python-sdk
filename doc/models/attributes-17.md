
# Attributes 17

## Structure

`Attributes17`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assignee` | [`PaymentSubmissionTaskAssigneeEnum`](../../doc/models/payment-submission-task-assignee-enum.md) | Optional | Helps to identify the owner of the task |
| `name` | `str` | Optional | Identifies the payment submission task to be executed |
| `output` | `Dict[str, object]` | Optional | Key Value map that contains the Task result. |
| `status` | [`PaymentSubmissionTaskStatusEnum`](../../doc/models/payment-submission-task-status-enum.md) | Optional | status of the submission task |

## Example (as JSON)

```json
{
  "assignee": "form3",
  "name": "fraud_check",
  "output": {
    "outcome": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "status": "completed"
}
```

