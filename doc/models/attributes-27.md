
# Attributes 27

## Structure

`Attributes27`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto` | `bool` | Optional | Indicates if the submission was created automatically by the system (`true`) or manually (`false`).<br>**Default**: `False` |
| `scheme_status_code` | `str` | Optional | Scheme-specific status (if submission has been submitted to a scheme) |
| `status` | [`DirectDebitDecisionSubmissionStatusEnum`](../../doc/models/direct-debit-decision-submission-status-enum.md) | Optional | - |
| `status_reason` | `str` | Optional | Reason for submission failure if status is `delivery_failed` |
| `submission_datetime` | `datetime` | Optional | Date and time of the submission |

## Example (as JSON)

```json
{
  "auto": false,
  "scheme_status_code": "0000",
  "status_reason": "direct debit does not exist",
  "submission_datetime": "03/12/2018 14:11:48",
  "status": "delivery_confirmed"
}
```

