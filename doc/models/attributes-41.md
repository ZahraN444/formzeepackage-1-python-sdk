
# Attributes 41

## Structure

`Attributes41`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_datetime` | `datetime` | Optional | Time the submission request was received by Form3. Used to compute the total processing time |
| `status` | [`SchemeFileSubmissionStatusEnum`](../../doc/models/scheme-file-submission-status-enum.md) | Optional | Status of the scheme file submission |
| `status_reason` | `str` | Optional | Plain-text description of the status attribute |
| `submission_datetime` | `datetime` | Optional | Time when the Form3 system begins processing of the submission |

## Example (as JSON)

```json
{
  "start_datetime": "03/13/2019 14:48:29",
  "status": "accepted",
  "submission_datetime": "03/13/2019 14:48:29",
  "status_reason": "status_reason6"
}
```

