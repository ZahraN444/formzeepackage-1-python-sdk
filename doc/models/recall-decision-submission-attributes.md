
# Recall Decision Submission Attributes

## Structure

`RecallDecisionSubmissionAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto` | `bool` | Optional | Indicates if the submission was created automatically by the system (`true`) or manually (`false`).<br>**Default**: `False` |
| `status` | [`RecallDecisionSubmissionStatusEnum`](../../doc/models/recall-decision-submission-status-enum.md) | Optional | [Status](http://draft-api-docs.form3.tech/api.html#enumerations-payment-status-codes-payment-submission-status) of the submission |
| `status_reason` | `str` | Optional | Reason for submission failure if status is `delivery_failed` |
| `submission_datetime` | `datetime` | Optional | Date and time of the submission |

## Example (as JSON)

```json
{
  "auto": false,
  "status": "accepted",
  "status_reason": "recall does not exist",
  "submission_datetime": "03/12/2018 14:11:48"
}
```

