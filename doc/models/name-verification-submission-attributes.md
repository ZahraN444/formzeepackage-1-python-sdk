
# Name Verification Submission Attributes

## Structure

`NameVerificationSubmissionAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `actual_name` | `str` | Optional | - |
| `answer` | [`NameVerificationSubmissionAnswerEnum`](../../doc/models/name-verification-submission-answer-enum.md) | Optional | - |
| `reason` | `str` | Optional | - |
| `reason_code` | [`NameVerificationSubmissionReasonCodeEnum`](../../doc/models/name-verification-submission-reason-code-enum.md) | Optional | - |
| `status` | [`NameVerificationSubmissionStatusEnum`](../../doc/models/name-verification-submission-status-enum.md) | Required | - |
| `status_reason` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "actual_name": "actual_name4",
  "answer": "confirmed",
  "reason": "reason0",
  "reason_code": "BAMM",
  "status": "delivery_confirmed",
  "status_reason": "status_reason6"
}
```

