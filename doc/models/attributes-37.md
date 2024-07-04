
# Attributes 37

## Structure

`Attributes37`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `destination_gateway` | `str` | Optional | - |
| `scheme_status_code` | `str` | Optional | - |
| `scheme_status_code_description` | `str` | Optional | - |
| `status` | [`DirectDebitReversalSubmissionStatusEnum`](../../doc/models/direct-debit-reversal-submission-status-enum.md) | Optional | - |
| `status_reason` | `str` | Optional | - |
| `submission_datetime` | `datetime` | Optional | - |
| `transaction_start_datetime` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "destination_gateway": "destination_gateway8",
  "scheme_status_code": "scheme_status_code4",
  "scheme_status_code_description": "scheme_status_code_description8",
  "status": "limit_check_passed",
  "status_reason": "status_reason6"
}
```

