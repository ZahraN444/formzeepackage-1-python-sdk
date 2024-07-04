
# Attributes 15

## Structure

`Attributes15`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assignee` | [`ReversalAdmissionTaskAssigneeEnum`](../../doc/models/reversal-admission-task-assignee-enum.md) | Optional | Helps to identify the owner of the task |
| `name` | `str` | Optional | Identifies the reversal admission task to be executed |
| `output` | `Dict[str, object]` | Optional | Key Value map that contains the Task result. |
| `status` | [`ReversalAdmissionTaskStatusEnum`](../../doc/models/reversal-admission-task-status-enum.md) | Optional | status of the task |

## Example (as JSON)

```json
{
  "assignee": "form3",
  "name": "account_check",
  "output": {
    "outcome": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "status": "completed"
}
```

