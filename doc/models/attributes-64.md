
# Attributes 64

## Structure

`Attributes64`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `output` | `Dict[str, object]` | Optional | Key Value map that contains the Task result. |
| `status` | [`ReturnSubmissionTaskStatusEnum`](../../doc/models/return-submission-task-status-enum.md) | Optional | status of the return submission task |

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

