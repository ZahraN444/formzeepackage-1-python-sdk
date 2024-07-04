
# Attributes 49

## Structure

`Attributes49`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file_identifier` | `str` | Optional | **Constraints**: *Pattern*: `^[0-9a-zA-Z]+$` |
| `file_number` | `str` | Optional | **Constraints**: *Pattern*: `^[0-9]+$` |
| `last_payment_date` | `date` | Optional | - |
| `status` | [`MandateSubmissionStatusEnum`](../../doc/models/mandate-submission-status-enum.md) | Optional | - |
| `status_reason` | `str` | Optional | - |
| `submission_datetime` | `datetime` | Optional | - |
| `submission_reason` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "file_identifier": "file_identifier4",
  "file_number": "file_number6",
  "last_payment_date": "2016-03-13",
  "status": "queued_for_delivery",
  "status_reason": "status_reason4"
}
```

