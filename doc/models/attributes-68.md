
# Attributes 68

## Structure

`Attributes68`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheme_status_code` | `str` | Optional | Scheme-specific status code, refer to scheme documentation |
| `scheme_status_code_description` | `str` | Optional | Description of `scheme_status_code` |
| `status` | [`ReversalSubmissionStatusEnum`](../../doc/models/reversal-submission-status-enum.md) | Optional | [Status of the reversal submission](http://draft-api-docs.form3.tech/api.html#enumerations-reversal-submission-status) |
| `status_reason` | `str` | Optional | Description of the reversal submission status |
| `submission_datetime` | `datetime` | Optional | Date of the reversal submission |
| `transaction_start_datetime` | `datetime` | Optional | Time the request was received by Form3. Used to compute the total transaction time of a payment. |

## Example (as JSON)

```json
{
  "scheme_status_code": "E",
  "scheme_status_code_description": "Field 1 (destination sorting code) was invalid",
  "status": "accepted",
  "status_reason": "Accepted without qualification",
  "submission_datetime": "05/09/2018 10:49:13",
  "transaction_start_datetime": "05/09/2018 10:49:13"
}
```

