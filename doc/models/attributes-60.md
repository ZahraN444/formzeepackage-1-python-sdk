
# Attributes 60

## Structure

`Attributes60`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheme_status_code` | `str` | Optional | Scheme-specific status code. Refer to scheme documentation where available. |
| `status` | [`RecallSubmissionStatusEnum`](../../doc/models/recall-submission-status-enum.md) | Optional | [Status](http://draft-api-docs.form3.tech/api.html#enumerations-payment-status-codes-payment-submission-status) of the submission |
| `status_reason` | `str` | Optional | Reason for submission failure if submission status is `delivery_failed` |
| `submission_datetime` | `datetime` | Optional | Date and time of the submission |

## Example (as JSON)

```json
{
  "scheme_status_code": "RR04",
  "status": "accepted",
  "status_reason": "Gateway failure",
  "submission_datetime": "03/12/2018 14:11:48"
}
```

