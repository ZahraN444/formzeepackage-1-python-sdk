
# Attributes 43

## Structure

`Attributes43`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admission_datetime` | `datetime` | Optional | Time when the Form3 system begins processing of the admission |
| `status` | [`TransactionFileAdmissionStatusEnum`](../../doc/models/transaction-file-admission-status-enum.md) | Optional | Status of the transaction file admission |
| `status_reason` | `str` | Optional | Plain-text description of the status attribute |
| `transaction_start_datetime` | `datetime` | Optional | Time the admission request was received by Form3. Used to compute the total transaction time |

## Example (as JSON)

```json
{
  "admission_datetime": "03/13/2019 14:48:29",
  "status": "confirmed",
  "status_reason": "accepted",
  "transaction_start_datetime": "03/13/2019 14:48:29"
}
```

