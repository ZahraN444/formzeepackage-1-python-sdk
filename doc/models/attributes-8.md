
# Attributes 8

## Structure

`Attributes8`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Optional | Further explanation of the reason given in reason_code. Only evaluated for certain reason codes. |
| `reason_code` | `str` | Optional | The reason for the recall. Has to be a valid [recall reason code](http://api-docs.form3.tech/api.html#enumerations-recall-reason-codes). |
| `status` | [`RecallStatusEnum`](../../doc/models/recall-status-enum.md) | Optional | The status of the recall, can either be `pending`, `confirmed`, or `failed`. |

## Example (as JSON)

```json
{
  "reason": "Payment was a duplicate",
  "reason_code": "DUPL",
  "status": "confirmed"
}
```

