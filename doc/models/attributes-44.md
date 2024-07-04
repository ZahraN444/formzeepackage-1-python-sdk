
# Attributes 44

## Structure

`Attributes44`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheme_references` | [`List[TransactionFileSubmissionSchemeReference]`](../../doc/models/transaction-file-submission-scheme-reference.md) | Optional | Summary of scheme-specific references submission to the scheme |
| `status` | [`TransactionFileSubmissionStatusEnum`](../../doc/models/transaction-file-submission-status-enum.md) | Optional | Status of the transaction file submission |
| `status_reason` | `str` | Optional | Plain-text description of the status attribute |
| `submission_datetime` | `datetime` | Optional | Time when the Form3 system begins processing of the submission |
| `transaction_start_datetime` | `datetime` | Optional | Time the submission request was received by Form3. Used to compute the total transaction time |

## Example (as JSON)

```json
{
  "status": "accepted",
  "status_reason": "transaction_files.data.attributes.transaction_count does not match file",
  "submission_datetime": "03/13/2019 14:48:29",
  "transaction_start_datetime": "03/13/2019 14:48:29",
  "scheme_references": [
    {
      "clearing_id": "clearing_id4",
      "file_identifier": "file_identifier4",
      "file_number": "file_number8",
      "transaction_count": 98,
      "transaction_sum": "transaction_sum0"
    },
    {
      "clearing_id": "clearing_id4",
      "file_identifier": "file_identifier4",
      "file_number": "file_number8",
      "transaction_count": 98,
      "transaction_sum": "transaction_sum0"
    }
  ]
}
```

