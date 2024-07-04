
# Attributes 30

## Structure

`Attributes30`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `destination_gateway` | `str` | Optional | - |
| `scheme_status_code` | `str` | Optional | Scheme-specific status (if submission has been submitted to a scheme) |
| `status` | [`DirectDebitRecallSubmissionStatusEnum`](../../doc/models/direct-debit-recall-submission-status-enum.md) | Optional | - |
| `status_reason` | `str` | Optional | Reason for submission failure if status is `delivery_failed` |
| `submission_datetime` | `datetime` | Optional | Date and time of the submission |

## Example (as JSON)

```json
{
  "scheme_status_code": "0000",
  "status_reason": "direct debit does not exist",
  "submission_datetime": "03/12/2018 14:11:48",
  "destination_gateway": "destination_gateway8",
  "status": "accepted"
}
```

