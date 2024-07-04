
# Attributes 38

## Structure

`Attributes38`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file_identifier` | `str` | Optional | **Constraints**: *Pattern*: `^[0-9a-zA-Z]+$` |
| `file_number` | `str` | Optional | **Constraints**: *Pattern*: `^[0-9]+$` |
| `scheme_status_code` | `str` | Optional | Scheme-specific status (if submission has been submitted to a scheme) |
| `scheme_status_code_description` | `str` | Optional | [Description](http://api-docs.form3.tech/api.html#enumerations-scheme-status-codes-for-bacs) of `scheme_status_code` |
| `status` | [`DirectDebitSubmissionStatusEnum`](../../doc/models/direct-debit-submission-status-enum.md) | Optional | - |
| `status_reason` | `str` | Optional | Description of the submission status |
| `submission_datetime` | `datetime` | Optional | Date of the submission |
| `transaction_start_datetime` | `datetime` | Optional | Time the request was received by Form3. Used to compute the total transaction time of an operation. |

## Example (as JSON)

```json
{
  "scheme_status_code": "0000",
  "scheme_status_code_description": "Field 1 (destination sorting code) was invalid",
  "status_reason": "Accepted without qualification",
  "submission_datetime": "03/12/2018 14:11:48",
  "transaction_start_datetime": "03/12/2018 14:11:49",
  "file_identifier": "file_identifier8",
  "file_number": "file_number4",
  "status": "delivery_confirmed"
}
```

